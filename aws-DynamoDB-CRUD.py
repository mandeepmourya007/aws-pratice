import json

import boto3


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('quick-photos')
items = []

data = {"PK": "USER#test1", "SK": "#METADATA#test1", "address": " amritsar \punjab, AZ 66619",
"birthdate": "1916-09-06", "email": "test1@gmail.com", "name": "mandeep", "username": "test1", 
"status": "Resource scientist reduce value according well.",
"interests": ["billion", "third", "green"], "followers": 0, "following": 0, "pinnedImage": "PHOTO#mandeepk#2018-06-09T15:00:24"}



def Creat(data):
    
    res = table.put_item(Item = data)
    
    print(data,res)

def Read(username):
    pk="USER#{}".format(username)
    sk="#METADATA#{}".format(username)
    
    res = table.get_item(
        
        # Key={'PK': 'USER#{}'.format("mandeep") ,'SK': '#METADATA#{}'.format("mandeep")   }  
       Key={'PK': pk ,'SK': sk  }  
       
        )
    print(res)    

def Update(username,address):
    pk="USER#{}".format(username)
    sk="#METADATA#{}".format(username)
    
    res = table.update_item(
        Key={'PK': pk ,'SK': sk  }  ,
         UpdateExpression = "SET address = :a",
        ExpressionAttributeValues = {":a": address }
        )

def Delete(username):
    pk="USER#{}".format(username)
    sk="#METADATA#{}".format(username)
    table.delete_item(
        Key = { "PK" : pk, "SK" : sk }
        )

# Update("test1","update address")
# Delete("test1")
Read("test1")

# Creat(data)















# def Read(username):
#     u="USER#{}".format(username)
#     resp = table.get_item(
    
#         Key = {
#             "PK" : u
          
#         }
        
#         )
#     print("hi",resp)
    
# def Update(user,address):
#     resp = dynamodb.transact_write_items(
        
#     TransactItems = [  
        
#         {
#               "Update": {
#                         "TableName": "quick-photos",
#                         "Key": {"PK": {"S": user}, "SK": {"S":  "METADATA{}".format(user)}},
#                         "UpdateExpression": "SET address = :a",
                        
#                         "ExpressionAttributeValues": {":a": {"S":  address}},
#                         "ReturnValuesOnConditionCheckFailure": "ALL_OLD",
#                     }
    
#         }
#         ])
    

# def create(name,address,email,usermame):
    
#     pass


# 
# Update("mandeep","testing")
# Read("mandeep")
# items.append(a)

# with table.batch_writer() as batch:
#     for item in items:
#         batch.put_item(Item=item)
