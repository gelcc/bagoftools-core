import unittest;
from src import file_system;
import os;

class Test(unittest.TestCase):

    def test_text_file_reader(self):
        
        new_file_name = 'test_file.txt';
        new_file_content = 'conteúdo do arquivo de teste a ser verificado!';

        new_file = open(new_file_name,'w+');
        new_file.write(new_file_content);
        new_file.close();
        
        result = file_system.read_text_file(new_file_name);
        
        self.assertEqual(result['name'],new_file_name);
        self.assertEqual(result['content'],new_file_content);

        os.remove(new_file_name);

if __name__ == '__main__':
    unittest.main();
