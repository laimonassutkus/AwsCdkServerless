import logging
import os

from b_aws_testing_framework.credentials import Credentials
from b_aws_testing_framework.tools.cdk_testing.cdk_tool_config import CdkToolConfig
from b_aws_testing_framework.tools.cdk_testing.testing_manager import TestingManager

CDK_PATH = os.path.dirname(os.path.abspath(__file__))
MANAGER = TestingManager(Credentials(), CdkToolConfig(CDK_PATH))

# Override global prefix.
GLOBAL_PREFIX = os.environ.get('GLOBAL_PREFIX')
if GLOBAL_PREFIX: MANAGER.set_global_prefix(f'Testing{GLOBAL_PREFIX[:10]}')


# Set up logging.
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def pytest_sessionstart(session):
    MANAGER.prepare_infrastructure()


def pytest_sessionfinish(session, exitstatus):
    MANAGER.destroy_infrastructure()
