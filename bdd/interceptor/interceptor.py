from typing import List

class Interceptor:
    def __init__(self,massa:dict,scenario:str,operacao:str,csv_files:List[str],response:dict) -> None:
        self.__massa = massa
        self.__operacao = operacao
        self.__csv_files = csv_files
        self.__scenario = scenario
        self.__response = response
    
    @property
    def set_massa(self,massa):
        self.__massa = massa
    
    @property
    def get_massa(self):
        return self.__massa
    
    @property
    def set_scenario(self,scenario:str):
        self.__scenario = scenario
    
    @property
    def set_operacao(self,operacao):
        self.__operacao = operacao
    
    @property
    def get_operacao(self):
        return self.__operacao
    
    @property
    def set_endpoint(self,endpoint):
        self.__endpoint = endpoint
        
    @property
    def set_csv_file(self,csv_file:str):
        self.__csv_files.append(csv_file)
    
    @property
    def set_csv_files(self,csv_files:List[str]):
        self.__csv_files = csv_files
    
    @property
    def get_csv_files(self):
        return self.__csv_files
    
    @property
    def set_response(self,response):
        self.__response = response
        
    @property
    def get_response(self):
        return self.__response    
        
    def ajusta_csv(self):
        self.get_csv_files.remove(0)
    