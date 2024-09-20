import base64
import json
from datetime import datetime
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    datetimeObj = datetime.now()
    timestampStr = datetimeObj.strftime("%d-%b-%Y-%H%M%S")
    
    kinesisRecords = []

    # Process each record from Kinesis
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        kinesisRecords.append(payload.decode('utf-8'))  # Decoding bytes to string
    
    ex_string = '\n'.join(kinesisRecords)
    my_key = 'output-' + timestampStr + '.txt'
    
    response = s3_client.put_object(Body=ex_string, Bucket='s3-bucket-de', Key=my_key)
    
    return 'Successfully processed {} records.'.format(len(event['Records']))
