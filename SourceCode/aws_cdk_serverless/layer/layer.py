from aws_cdk.aws_lambda import Runtime
from aws_cdk.core import Stack
from b_cfn_lambda_layer.lambda_layer import LambdaLayer

from aws_cdk_serverless.layer import layer_root


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
                # Don't need to specify here, because this dependency
                # is already in requirements.txt file (in the layer source code).
                # 'pynamodb': PackageVersion.from_string_version('5.2.1')
            }
        )
