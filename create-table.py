import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table

TableName = input("Enter table Name:")
table = dynamodb.create_table(
    TableName= TableName,
    KeySchema=[
        {
            'AttributeName': 'userid',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'userid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print("table created at",table.creation_date_time)
