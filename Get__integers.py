from http.client import HTTPSConnection
from json import dumps, loads
import pickle

# Before starting, i am create 4 API keys
# So if you go link https://api.random.org/dashboard  sign up and create your own API keys,replace it in dict,it will be work!
tokens = ['013e6c64-22c8-4ffe-a084-fc5538d978d6',
          '91977ce9-468c-4ebd-b7e1-c4b633ccb766',
          '32094f29-d015-4454-a3f4-64ef0102f1c8',
          'be76f336-5387-46db-9269-352b4eb588c8']
# For each of this token allow 250000 bytes per day, so for each key we can get 250k zeros and units
# Because of limitation in 1 request 10000 bytes i had to put my code in 25 steps loop
# And for 1 million digits this code worked 25*4 times(not so fast,but strictly on assignment)
for API_TOKEN in tokens:
    response_data = 0
    quarter_of_million = list()
    for i in range(1, 26):
        request_data = {  # Request body
            'jsonrpc': '2.0',
            'method': 'generateIntegers',
            'params': {
                'apiKey': API_TOKEN,
                'min': 0, # digits range
                'max': 1,
                'n': 10000,  # Numbers Amount
            },
            'id': 1, # this may be default 1 or you cant itterate in for each step
        }
        encoded_data = dumps(request_data)

        headers = {
            'Content-Type': 'application/json',  # Request type
        }

        encoded_headers = dumps(headers)

        connection = HTTPSConnection('api.random.org')
        connection.request('POST', '/json-rpc/2/invoke', encoded_data, headers)

        response = connection.getresponse()

        response_data = loads(response.read().decode())
        response_data = response_data['result']['random']['data']

        quarter_of_million += response_data  # put numbers for each loop in 1 list,then write it

    with open("numbers.dat", "ab") as file:
        pickle.dump(quarter_of_million, file)
        file.close()
