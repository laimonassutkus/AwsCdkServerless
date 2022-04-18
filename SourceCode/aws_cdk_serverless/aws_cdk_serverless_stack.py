from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack, Construct

from aws_cdk_serverless.crud import crud_root
from aws_cdk_serverless.layer.layer import Layer


class AwsCdkServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        layer = Layer(self)

        # Create function.
        Function(
            scope=self,
            id='Create',
            function_name='Create',
            code=Code.from_asset(f'{crud_root}/create'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler',
            layers=[layer]
        )

        # Read function.
        Function(
            scope=self,
            id='Read',
            function_name='Read',
            code=Code.from_asset(f'{crud_root}/read'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler',
            layers=[layer]
        )

        # Update function.
        Function(
            scope=self,
            id='Update',
            function_name='Update',
            code=Code.from_asset(f'{crud_root}/update'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler',
            layers=[layer]
        )

        # Delete function.
        Function(
            scope=self,
            id='Delete',
            function_name='Delete',
            code=Code.from_asset(f'{crud_root}/delete'),
            runtime=Runtime.PYTHON_3_9,
            handler='index.handler',
            layers=[layer]
        )
