import pytest
from behave import given,when,then
from interceptor.interceptor import Interceptor

interceptor = Interceptor()

@given('seleciono a massa "{massa}"')
def step_seleciono_a_massa(context,massa:str):
    interceptor.set_csv_file(csv_file=massa)
    

@then('retorna uma lista de alunos')
def step_retorna_uma_lista_de_alunos(context):
    pass


@given('seleciono os arquivos {csv_files}')
def step_seleciono_os_arquivos(context,csv_files:str):
    interceptor.set_csv_files(csv_files.split(','))
    

@pytest.mark.timeout(5) # set timeout request 5 seconds
@when('executo um "{metodoHttp}" no cenario {cenario}')
def step_executo_um_metodo_http_com_cenario(context,metodoHttp,cenario):
    interceptor.set_operacao = metodoHttp
    interceptor.set_scenario = cenario
    from request.request import faz_requisicao
    response = faz_requisicao()
    interceptor.set_response(response)
    


@then('retorna uma simulacao de mensalidade')
def step_retorna_uma_simulacao_de_mensalidade(context):
    assert interceptor.get_response().status_code == 200