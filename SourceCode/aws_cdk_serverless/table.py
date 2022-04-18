from aws_cdk.aws_dynamodb import Table, Attribute, AttributeType, TableEncryption
from aws_cdk.core import Stack


class CatTable(Table):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id='CatTable',
            table_name='CatTable',
            partition_key=Attribute(name='name', type=AttributeType.STRING),
            encryption=TableEncryption.DEFAULT
        )

    @property
    def region(self) -> str:
        return self.stack.region
