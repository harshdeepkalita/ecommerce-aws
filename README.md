# Ecommerce Data Pipeline

![Image 20-09-2024 at 19 46](https://github.com/user-attachments/assets/832cdc68-b1b6-4ed7-a152-e2415bb457e1)


## Ingestion Pipeline

This Python script transforms data from a CSV dataset into JSON format, which is then sent as the HTTP POST message body to an AWS API Gateway. The API Gateway triggers a Lambda function called ⁠ `writeKinesis` ⁠, which forwards the data to a Kinesis stream named ⁠ `APIData` ⁠.


## Kinesis Stream to S3 Pipeline

The Lambda function ⁠`write-kinesis-to-s3` ⁠ processes records from the Kinesis stream. These records are base64-encoded, and the function decodes them, concatenates the records, and stores them as a text file in an S3 bucket `s3-bucket-de`, naming the file with a unique timestamp.


## DynamoDB Pipeline 

The Lambda function ⁠`write-to-dynamodb` ⁠ processes data from the Kinesis stream to update two DynamoDB tables: *customers* and *invoices*. It decodes the base64-encoded data into a dictionary. For each record, the function updates the customers table using ⁠ CustomerID ⁠ as the primary key and adds information related to the specific ⁠InvoiceNo ⁠. Then, it updates the invoices table with stock details using ⁠InvoiceNo ⁠ as the key. After processing, the function confirms the number of successfully processed records.


## Redshift Visualization Pipeline

This pipeline transfers real-time data from the **Kinesis Stream** ⁠ `APIData` ⁠ to an **Amazon Redshift** table ⁠ `firehose_transactions`⁠ for analysis and visualization.

1.⁠ ⁠**Kinesis Stream**: Data is ingested from the Kinesis stream.

2.⁠ ⁠**Kinesis Firehose**: Manages and buffers the data, then writes it to an intermediate S3 bucket `fire-hose-redshift`.

3.⁠ ⁠**S3 Storage**: Temporarily stores the data.

4.⁠ ⁠**Redshift Table**: The data is copied from S3 into a Redshift table.

5.⁠ ⁠**Analysis and Visualization**: The data in Redshift can be queried and visualized using tools like **LookerStudio*.


This pipeline automates real-time data ingestion into Redshift for easy analytics and reporting.
