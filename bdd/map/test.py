from csv import reader
import os

def find_project_file(filename):
    current_dir = os.getcwd()
    data_folder = os.path.join(current_dir, '..','data')
    if os.path.exists(data_folder):
        return f'{data_folder}/{filename}'
    else:
        raise FileNotFoundError(f"The file '{filename}' does not  not found within the 'bdd/data' folder or not found in the directory structure.")

def ler_csv_cenario(massa:str,cenario:str) -> dict:
    caminho = find_project_file(f'{massa}.csv')
   
    print("File path:", caminho) 
    try:
        with open(caminho) as csv:
            leitor_csv = reader(csv,delimiter=';')
            header = next(leitor_csv)
            for linha in leitor_csv:
                    if linha[0] == cenario:
                            result_map = {header[i]: linha[i] for i in range(1,len(header))}
                            return result_map
    except FileNotFoundError:
        print(f"File '{caminho}' not found.")            