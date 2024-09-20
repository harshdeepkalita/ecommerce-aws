# Ecommerce Data Pipeline

## Ingestion Pipeline

I have developed a Python script that transforms data from a CSV dataset into JSON format. This JSON data is then sent as the HTTP POST message body to an API Gateway created in AWS. Upon receiving the data, the API Gateway triggers a Lambda function named `writeKinesis`, which subsequently sends the data to a Kinesis stream named `APIData`.


