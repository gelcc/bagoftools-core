import unittest;
import tokenizer;

class Test(unittest.TestCase):

    def test_tokenizer(self):
        sentence = 'testando tokenizador do sistema. Esse conteúdo simplismente o propósito de testar essa funcionalidade.'
        result = tokenizer.tokenizeWords(sentence);
        print(result);

if __name__ == '__main__':
    unittest.main()
