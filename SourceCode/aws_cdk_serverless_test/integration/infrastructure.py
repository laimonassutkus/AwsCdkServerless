from aws_cdk.core import Construct
from b_aws_testing_framework.tools.cdk_testing.testing_stack import TestingStack

from aws_cdk_serverless.aws_cdk_serverless_stack import AwsCdkServerlessStack


class Infrastructure(TestingStack):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope=scope)

        stack = AwsCdkServerlessStack(
            scope,
            construct_id='TestingServerlessStack',
            stack_name='TestingServerlessStack'
        )

        self.add_output(
            key='ApiUrl',
            value=stack.api.full_url
        )

    @staticmethod
    def api_url() -> str:
        return Infrastructure.get_output('ApiUrl')
