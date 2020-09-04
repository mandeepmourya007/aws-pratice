import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.table("students")

# table.update_table()