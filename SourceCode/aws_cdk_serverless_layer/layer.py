from aws_cdk.aws_lambda import Runtime
from aws_cdk.core import Stack
from b_cfn_lambda_layer.lambda_layer import LambdaLayer
from b_cfn_lambda_layer.package_version import PackageVersion

from aws_cdk_serverless_layer import layer_root


class Layer(LambdaLayer):
    def __init__(self, scope: Stack) -> None:
        super().__init__(
            scope=scope,
            name='ExampleLayer',
            source_path=layer_root,
            code_runtimes=[
                Runtime.PYTHON_3_9
            ],
            dependencies={
                'pynamodb': PackageVersion.from_string_version('5.2.1')
            }
        )
