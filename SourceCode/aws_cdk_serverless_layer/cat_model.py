import os

from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model

TABLE_NAME = os.environ['TableName']
TABLE_REGION = os.environ['TableRegion']


class CatModel(Model):
    class Meta:
        table_name = TABLE_NAME
        region = TABLE_REGION

    name = UnicodeAttribute(hash_key=True)
    age = NumberAttribute(null=False)
    color = UnicodeAttribute(null=False)
