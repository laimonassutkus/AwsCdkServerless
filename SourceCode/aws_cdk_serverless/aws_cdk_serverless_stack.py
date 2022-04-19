from aws_cdk.aws_lambda import Code
from aws_cdk.core import Stack, Construct

from aws_cdk_serverless.api import CatApi
from aws_cdk_serverless.backend import Backend
from aws_cdk_serverless.crud import crud_root
from aws_cdk_serverless.table import CatTable
from aws_cdk_serverless_layer.layer import Layer


class AwsCdkServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = CatTable(scope=self)
        layer = Layer(scope=self)

        # Create function.
        create = Backend(
            scope=self,
            id='Create',
            function_name='Create',
            code=Code.from_asset(f'{crud_root}/create'),
            cat_table=table,
            layers=[layer]
        ).grant_read().grant_write()

        # Read function.
        read = Backend(
            scope=self,
            id='Read',
            function_name='Read',
            code=Code.from_asset(f'{crud_root}/read'),
            cat_table=table,
            layers=[layer]
        ).grant_read()

        # Update function.
        update = Backend(
            scope=self,
            id='Update',
            function_name='Update',
            code=Code.from_asset(f'{crud_root}/update'),
            cat_table=table,
            layers=[layer]
        ).grant_read().grant_write()

        # Delete function.
        delete = Backend(
            scope=self,
            id='Delete',
            function_name='Delete',
            code=Code.from_asset(f'{crud_root}/delete'),
            cat_table=table,
            layers=[layer]
        ).grant_read().grant_write()

        # Create the actual API!
        self.api = CatApi(
            scope=self,
            create_backend=create,
            read_backend=read,
            update_backend=update,
            delete_backend=delete
        )
