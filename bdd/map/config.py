import os
import yaml

def get_yml_variable(variable:str):
    current_dir = os.getcwd()
    file = os.path.join(current_dir,'..','application.yml')
    
    if os.path.exists(file):
        with open(file, 'r') as file:
            config = yaml.safe_load(file)
            
        yml_variable = config['endpoints'][variable]
        
        if yml_variable == '':
            raise Exception('the variable {variable} does not found in yml file')
        
        return yml_variable
    else:
        raise FileNotFoundError(f"The yml file does not  not found within the bdd folder or not found in the directory structure.")

def get_env_variable(variable:str):
    env = os.getenv(variable)
    if env =='':
        raise Exception(f'the {variable} doesnt found in env file')
    return env
