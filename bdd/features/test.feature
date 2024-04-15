Feature: Listar - Simular

Scenario Outline: Listar alunos
    Given seleciono a massa "listar"
    When executo um "GET" no cenario <scenario>
    Then retorna uma lista de alunos
Examples:
    | scenario |
    | CENARIO |

Scenario Outline: Simulo mensalidade
Given seleciono os arquivos <csv_files>
When executo um "GET" no cenario <cenario>
When executo um "POST" no cenario <cenario>
Then retorna uma simulacao de mensalidade
Examples:
    |   csv_files     | cenario |
    | listar,simular  | SIMULAR |