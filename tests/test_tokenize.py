# Bag Of Tools - Core
# arquivo de testes da função de tokenização.

import unittest;
from click.testing import CliRunner;
from src.__main__ import tokenize;

class TestTokenizer(unittest.TestCase):

    # testar comando de tokenização padrão.
    def test_word_tokenizer(self):

        runner = CliRunner();
        result_1 = runner.invoke(tokenize,['-w','tests/text.txt']);
        result_2 = runner.invoke(tokenize,['--words','tests/text.txt']);
        self.assertEqual(result_1.exit_code,0);
        self.assertEqual(result_2.exit_code,0);
        self.assertEqual(result_1.output, result_2.output);

    # testar tokenização de sentenças.
    def test_sent_tokenize(self):

        runner = CliRunner();
        result_1 = runner.invoke(tokenize,['-s','tests/text.txt']);
        result_2 = runner.invoke(tokenize,['--sents','tests/text.txt']);
        self.assertEqual(result_1.exit_code,0);
        self.assertEqual(result_2.exit_code,0);
        self.assertEqual(result_1.output, result_2.output);

if __name__ == '__main__':
    unittest.main();