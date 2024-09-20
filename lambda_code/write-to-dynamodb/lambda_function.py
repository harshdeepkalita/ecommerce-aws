import json
import boto3
import base64

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    
    for record in event['Records']:
        rec = base64.b64decode(record['kinesis']['data'])
        str_rec = str(rec, 'utf-8')
        dict_rec = json.loads(str_rec)
        
        # Customer update
        customer_key = {"customerID": {"N": str(dict_rec["CustomerID"])}}
        
        ex_customer = {
            str(dict_rec['InvoiceNo']): {
                'Value': {"S": 'Some data'},
                "Action": "PUT"
            }
        }
        
        response = client.update_item(
            TableName='customers', 
            Key=customer_key, 
            AttributeUpdates=ex_customer
        )
        
        # Inventory update
        inventory_key = {'invoiceNo': {"N": str(dict_rec['InvoiceNo'])}}
        
        # Prepare stock data, remove InvoiceNo and StockCode from stock_dict
        stock_dict = dict(dict_rec)
        stock_dict.pop('InvoiceNo', None)
        stock_dict.pop('StockCode', None)
        stock_json = json.dumps(stock_dict)
        
        ex_dynamoRecord = {
            str(dict_rec['StockCode']): {'Value': {'S': stock_json}, "Action": "PUT"}
        }
        
        response = client.update_item(
            TableName='invoices', 
            Key=inventory_key, 
            AttributeUpdates=ex_dynamoRecord
        )
    
    return 'Successfully processed {} records.'.format(len(event['Records']))
