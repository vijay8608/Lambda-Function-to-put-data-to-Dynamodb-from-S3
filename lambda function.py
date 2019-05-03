import json
import boto3
import random
import string

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # print(str(event))
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    # print(bucket)
    # print(json_file_name)
    
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    jsonDict['source']='twitter'
    # make random isrescued
    jsonDict['isrescued']='false' 
    # make random
    jsonDict['location']='San Jose'
    
    random_str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    
    jsonDict['id']=random_str
    
    if ('fire' in jsonDict['text']){
        jsonDict['category']='fire'
    }
    
     if ('medical' in jsonDict['text']){
        jsonDict['category']='medical'
    }
    
     if ('shelter' in jsonDict['text']){
        jsonDict['category']='shelter'
    }
    
     if ('food' in jsonDict['text']){
        jsonDict['category']='food'
    }
    
    print(jsonDict)
    
    # table = dynamodb.Table('messages')
    # table.put_item(Item = jsonDict)
    
    
    return 'Hello from lambda'
