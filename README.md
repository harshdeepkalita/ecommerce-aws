# Ecommerce Data Pipeline

## Ingestion Pipeline

I have developed a Python script that transforms data from a CSV dataset into JSON format. This JSON data is then sent as the HTTP POST message body to an API Gateway created in AWS. Upon receiving the data, the API Gateway triggers a Lambda function named `writeKinesis`, which subsequently sends the data to a Kinesis stream named `APIData`.

## Kinesis Stream to S3 Pipeline

The Lambda function, `write-kinesis-to-s3` processes records from a Kinesis stream which are provided to it in base64-encoded format. It decodes the base64-encoded data, concatenates the records, and stores them as a text file in an S3 bucket. The file is named with a timestamp for uniqueness.

## DynamoDB Pipeline 

The Lambda function `write-to-dynamodb` processes data from Kinesis streams to update two DynamoDB tables: *customers* and *invoices*. The function first decodes the base64-encoded data from the stream and converts it into a dictionary. For each record, it updates the ⁠ customers ⁠ table using the ⁠CustomerID ⁠ as the primary key, adding information related to a specific ⁠ InvoiceNo ⁠. It then updates the ⁠ invoices ⁠ table using ⁠InvoiceNo ⁠ as the key and stores stock details. After processing all records, the function returns a message confirming the number of records processed successfully.
