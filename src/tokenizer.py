from nltk import word_tokenize;

def tokenize_words(string):

    tokens = word_tokenize(string,language='portuguese');
    
    result = { 'tokens': tokens };

    return result;