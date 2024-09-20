import pandas as pd
import requests


# url of api gateway endpoint
url = 'https://e4b2pmqr3m.execute-api.us-east-1.amazonaws.com/Production/hello'


df = pd.read_csv('TestSample.csv',sep=',')

for i in df.index:
    export = df.iloc[i].to_json() # converted to json string
    response = requests.post(url,data=export)  # sending this json string in request body POST METHOD to the API gateway
    print(response)  




    
