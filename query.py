import boto3


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("students")

# we need to pass both pk and sk
def get(pk,sk):
    resp = table.get_item(
        Key = {
            
            # pk
            "userid" : pk
            ,
            # sk
            "name":sk
         
        }
        )
    print((resp))
    
# get(2,"Corliss Zuk")

def update():

    
    table.update_item(
        Key={
               "userid": 11,
                "name" : 'Marcus Blohm'
            },
        UpdateExpression="set #nam = :n",
        ExpressionAttributeValues={
                ':n': "mandeep"                       
            }, ExpressionAttributeNames= {"#nam": "s"},
        ReturnValues="UPDATED_NEW"
        )


update()                                                 
# get(2,"Corliss Zuk")


def delete_student():
  
    response = table.delete_item(
        Key={
            'userid': 11,
                "name" : 'Marcus Blohm'
            }
    )


# delete_student()

from boto3.dynamodb.conditions import Key, Attr



def query():    
    response = table.query(
        KeyConditionExpression=Key('userid').eq(3)
        
       
    )
    items = response['Items']
    print(items)

def scan():    
    response = table.scan(
        FilterExpression=Attr('userid').lt(27)
    )
    items = response['Items']
    for item in items:
        print(item)
scan()