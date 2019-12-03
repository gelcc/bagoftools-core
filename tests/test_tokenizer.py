import unittest;
from src import tokenizer;

class Test(unittest.TestCase):

    def test_word_tokenizer(self):
        
        sentence = 'testando tokenizador do sistema.    Esse conteúdo simplismente tem o propósito de testar essa funcionalidade.';
        expected_tokens = ['testando', 'tokenizador', 'do', 'sistema', '.', 'Esse', 'conteúdo', 'simplismente', 'tem','o', 'propósito', 'de', 'testar', 'essa', 'funcionalidade', '.']
        
        result = tokenizer.tokenize_words(sentence);
        
        self.assertEqual(result['tokens'],expected_tokens);


if __name__ == '__main__':
    unittest.main();
