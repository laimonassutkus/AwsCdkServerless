from aws_cdk.aws_iam import PolicyStatement
from aws_cdk.aws_lambda import Function, Code, Runtime, CfnPermission
from aws_cdk.core import Stack

from aws_cdk_serverless.table import CatTable


class Backend(Function):
    def __init__(
            self,
            scope: Stack,
            id: str,
            function_name: str,
            code: Code,
            cat_table: CatTable,
            *args,
            **kwargs
    ) -> None:
        super().__init__(
            scope=scope,
            id=id,
            code=code,
            handler='index.handler',
            runtime=Runtime.PYTHON_3_9,
            function_name=function_name,
            *args,
            **kwargs
        )

        self.__cat_table = cat_table

        CfnPermission(
            scope=scope,
            id=f'{function_name}InvokePermission',
            action='lambda:InvokeFunction',
            function_name=self.function_name,
            principal='apigateway.amazonaws.com',
        )

        self.add_environment(
            key='TableName',
            value=cat_table.table_name
        )

        self.add_environment(
            key='TableRegion',
            value=cat_table.region
        )

    def grant_read(self) -> 'Backend':
        self.add_to_role_policy(
            PolicyStatement(
                actions=[
                    'dynamodb:DescribeTable',
                    'dynamodb:GetItem',
                    'dynamodb:Scan',
                    'dynamodb:Query'
                ],
                resources=[self.__cat_table.table_arn]
            )
        )

        return self

    def grant_write(self) -> 'Backend':
        self.add_to_role_policy(
            PolicyStatement(
                actions=[
                    'dynamodb:PutItem',
                    'dynamodb:DeleteItem',
                    'dynamodb:UpdateItem',
                    'dynamodb:BatchWriteItem'
                ],
                resources=[self.__cat_table.table_arn]
            )
        )

        return self
