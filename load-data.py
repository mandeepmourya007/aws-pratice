import boto3
import json

from decimal import Decimal
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("students")

items = []

with open("myScript/students.json") as f:
    for row in f:
       items.append(json.loads(row, parse_float=Decimal))
with table.batch_writer() as batch:
    for item in items:
        
        batch.put_item(item)