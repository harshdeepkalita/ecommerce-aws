import json
import boto3

def lambda_handler(event, context):
    
    print(event)
    
    try:
        method = event['context']['http-method']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Bad Request: Missing httpMethod in context')
        }

    

    if method == 'POST':
        try:
            req_body = event['body-json']  
        except KeyError:
            return {
                'statusCode': 400,
                'body': json.dumps('Bad Request: Missing body-json in event')
            }
            
        extracted_data = json.dumps(req_body) #Kinesis client expects a byte string, hence convert from json object to json string
        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='APIData',  # Kinesis stream name
            Data=extracted_data,   # Data to be sent to Kinesis
            PartitionKey='string'  # Partition key for sharding
            )
        
        return {
                'statusCode': 200,
                'body': json.dumps('Data sent to Kinesis!')
            }
            
            
    elif method == 'GET':
        
        client = boto3.client('dynamodb')
        im_invoiceID = event['params']['querystring']['InvoiceNo'] # extracting the invoiceNo from req parameter
        print(im_invoiceID)
        response = client.get_item(TableName = 'invoices', Key = {'invoiceNo':{'N': im_invoiceID}})
        print(response['Item'])
        
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }
        
        
    else:
            
        return {
                'statusCode': 501,
                'body': json.dumps('Method Not Allowed')
            }


