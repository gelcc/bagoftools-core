# Bag of Tools - Core

CLI (Command Line Interface) que compila as principais funcionalidades que serão oferecidas pelo programa Bag Of Tools.

## Requisitos

- [Python 3](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)

## Instalação

Instalar **setuptools**:

`$ pip install setuptools`

Executar o comando para instalar a última distribuição:

`$ pip install https://github.com/gelcc/bagoftools-core/blob/master/dist/bagoftools_core-0.1-py3-none-any.whl?raw=true`

Verifique se tudo foi instalado com sucesso:

`$ bagoftools -v`

## Tokenizador

A aplicação inclui o tokenizador disponibilizado pelo módulo [nltk](https://www.nltk.org/).

O seguinte comando realiza a tokenização de de um texto salvo em um arquivo (.txt).

`$ bagoftools tokenize -w doc.txt`

Ao utilizar a opção (`-w`) ou (`--words`), a tokenização de palavras e pontuações será realizada. Todavia, como se trata da opção *default*, essa *flag* pode ser omitida:

`$ bagoftools tokenize doc.txt`

Caso seja desejável separar as sentenças de um texto, a opção (`-s`) ou (`--sents`) pode ser utilizada.

`$ bagoftools tokenize -s doc.txt`

Para salvar os resultados, pode-se utilizar:

`$ bagoftools tokenize doc.txt > tokens.txt`

---
GELC - Grupo de Estudo em Linguística Computacional
