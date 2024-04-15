import pytest
from behave import given,when,then
from interceptor.interceptor import Interceptor
from request.test import faz_requisicao
from map.test import ler_csv_cenario

interceptor = Interceptor()

@given('seleciono a massa "{variable}"')
def step_seleciono_a_source(context,variable:str):
    interceptor.add_csv_file(csv_file=variable)
    

@then('retorna uma lista de alunos')
def step_retorna_uma_lista_de_alunos(context):
    interceptor.adjust_csv()
    


@given('seleciono os arquivos {csv_files}')
def step_seleciono_os_arquivos(context,csv_files:str):
    files = csv_files.split(',')
    for _,item  in enumerate(files):
        interceptor.add_csv_file(item)
    

@pytest.mark.timeout(5) # set timeout request 5 seconds
@when('executo um "{httpMethod}" no cenario {scenario}')
def step_executo_um_metodo_http_com_cenario(context,httpMethod,scenario):
    interceptor.operation = httpMethod
    interceptor.scenario = scenario
    interceptor.source = ler_csv_cenario(interceptor.csv_files[0],scenario)
  
    response = faz_requisicao(interceptor)
    interceptor.adjust_csv()
    #interceptor.response({'test':123})
    


@then('retorna uma simulacao de mensalidade')
def step_retorna_uma_simulacao_de_mensalidade(context):
    pass
    #assert interceptor.get_response().status_code == 200