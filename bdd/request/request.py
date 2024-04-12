import requests
import json
from bdd.interceptor.interceptor import Interceptor

def faz_requisicao(interceptor:Interceptor):
    endpoint = monta_endpoint()
    headers = get_headers()
    if interceptor.get_operacao() == 'GET':
        response = requests.get(url=endpoint,headers=headers)
        print(response)
        
    elif interceptor.get_operacao == 'POST':
        payload = monta_payload()
        print(payload)
        requests.post(url=endpoint,payload=payload)
        print(response)    
    
    
def monta_endpoint(interceptor:Interceptor) -> str:
    yml_endpoint = get_yml_variable(interceptor.get_csv_files().index(0))
    return replace_variable(yml_endpoint)
    

def get_headers():
    pass

def get_yml_variable(variable:str) -> str:
    pass

def replace_variable(variable:str) -> str:
    # here there's nothing we can do ...,just using if and elifs /test/{zipcode} using replace {zipcode} from the scenario
    pass

def monta_payload(interceptor:Interceptor):
    # its required depending of the scenarios wether we need to use response from other requests
    return json.loads(interceptor.get_massa().index(0))