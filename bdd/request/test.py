import requests
import json
from interceptor.interceptor import Interceptor
from map.config import get_yml_variable,get_env_variable


def faz_requisicao(interceptor:Interceptor):
    
    endpoint = monta_endpoint(interceptor)
    
    headers = get_headers()
    if interceptor.operation == 'GET':
        #response = requests.get(url=endpoint,headers=headers)
        #print(response)
        print('fez um GET')
        
    elif interceptor.operation == 'POST':
        payload = monta_payload(interceptor)
        print(payload)
        #requests.post(url=endpoint,payload=payload)
        #print(response)    
        print('fez um POST')
    
def monta_endpoint(interceptor:Interceptor) -> str:
    BASE_URL = get_env_variable('API_BASE_URL')
    variable = interceptor.csv_files[0]
    yml_endpoint = get_yml_variable(variable)
    print(yml_endpoint)
    #if you like to add more rules here to change parameters like {test} use this method below
    #return replace_variable(yml_endpoint)
    return BASE_URL + yml_endpoint
    
    

def get_headers():
    pass


def replace_variable(variable:str) -> str:
    # here there's nothing we can do ...,just using if and elifs /test/{zipcode} using replace {zipcode} from the scenario
    pass

def monta_payload(interceptor:Interceptor):
    # its required depending of the scenarios wether we need to use response from other requests
    
    return json.dumps(interceptor.source['json'])