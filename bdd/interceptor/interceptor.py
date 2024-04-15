from typing import List

class Interceptor:
    def __init__(self, source: dict = {}, scenario: str = '', operation: str = '', csv_files: List[str] = [], response: dict = {}) -> None:
        self.__source = source
        self.__operation = operation
        self.__csv_files = csv_files
        self.__scenario = scenario
        self.__response = response
    
    @property
    def source(self):
        return self.__source
    
    @source.setter
    def source(self, source):
        self.__source = source
    
    @property
    def scenario(self):
        return self.__scenario
    
    @scenario.setter
    def scenario(self, scenario: str):
        self.__scenario = scenario
    
    @property
    def operation(self):
        return self.__operation
    
    @operation.setter
    def operation(self, operation):
        self.__operation = operation
    
    @property
    def csv_files(self):
        return self.__csv_files
    
    @csv_files.setter
    def csv_files(self, csv_files: List[str]):
        self.__csv_files = csv_files
    
    @property
    def response(self):
        return self.__response
    
    @response.setter
    def response(self, response):
        self.__response = response
        
    def adjust_csv(self):
        if self.__csv_files:
            self.__csv_files.pop(0)
            
    def add_csv_file(self, csv_file: str):
        self.__csv_files.append(csv_file)
