# Bag Of Tools - Core
# módulo para gerenciamento de arquivos.

# função para obter nomes de arquivos.
from os.path import basename;

# função para ler um único arquivo apartir de um enderço no disco.
def read_text_file(file_path):
  
  # abrir arquivo.
  file = open(file_path,'r');
  
  # utilizar função para pegar o nome do arquivo.
  file_name = basename(file_path);
  
  # ler conteúdo do arquivo aberto.
  file_content = file.read();
  
  # fechar arquivo após a leitura para liberar memória.
  file.close();
  
  # dicionário para ser retornado contendo informações do arquivo e seu conteúdo.
  result = {
  
    "name":file_name,
    "path":file_path,
    "content":file_content
  
  }

  # retornar dicionário com resultados.
  return result;