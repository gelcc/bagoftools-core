# Bag Of Tools - Core
# módulo de tokenização.

# importar funções do módulo nltk
from nltk import tokenize, data, download;

# verificar se as dependências estão instaladas, caso não, realizar o download.
try:

    data.find('tokenizers/punkt');

except LookupError:

    download('punkt');

# função para tokenizar palavras incluindo pontuações.
def word_tokenize(text):

    tokens = tokenize.word_tokenize(text,language='portuguese');
    return tokens;

# função para tokenizar sentenças.
def sent_tokenize(text):
    
    tokens = tokenize.sent_tokenize(text,language='portuguese');
    return tokens;