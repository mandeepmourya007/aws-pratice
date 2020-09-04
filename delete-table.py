import boto3



# Get the service resource.
dynamodb = boto3.resource('dynamodb')
tableName = input("Enter table Name you want to delete:")
try:
    table = dynamodb.Table(tableName)
    print("table was create on ",table.creation_date_time)

except:
    print("Table not found")
    # print(e)
try:
    table.delete()
    print("table deleted successfully")    

except:
    print("table not deleted")
    # print(e)
