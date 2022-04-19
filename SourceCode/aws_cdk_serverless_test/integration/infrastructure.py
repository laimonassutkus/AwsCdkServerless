from aws_cdk.core import Construct
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from aws_cdk_serverless.aws_cdk_serverless_stack import AwsCdkServerlessStack


class Infrastructure(TestingStack):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope=scope)

        AwsCdkServerlessStack(
            scope,
            construct_id=self.global_prefix() + 'TestingStack',
            stack_name=self.global_prefix() + 'TestingStack'
        )
