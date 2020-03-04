# Bag Of Tools - Core
# módulo principal para a definição dos comandos.

# biblioteca utilizada para definir os comandos.
import click;

# módulo tokenizador.
from src.tokenizer import word_tokenize, sent_tokenize;

# definir grupo de comandos.
@click.group(context_settings={'help_option_names':['-h','--help']})
@click.version_option('0.1 (Alpha)','-v','--version')
def cli():
    ''' 
        GELC - Bag Of Tools Core\n
        Project Repository: https://github.com/gelcc/bagoftools-core
    '''
    pass;

# comando para tokenizar um arquivo de texto.
@cli.command('tokenize', short_help='Tokenize text.')
@click.argument('file', type=click.File(encoding='utf8'))
@click.option('-w', '--words','tokenization_type', flag_value='words', help='Tokenize words with punctuations.')
@click.option('-s', '--sents','tokenization_type', flag_value='sentences', help='Tokenize sentences.')
def tokenize(file, tokenization_type):

    # receber conteúdo do arquivo.
    file_content = file.read();

    # tokenizar conteúdo.
    if(tokenization_type == 'sentences'):
        tokens = sent_tokenize(file_content);

    else:
        tokens = word_tokenize(file_content);

    # formatar saída.
    output = '\n'.join(tokens).encode('utf8');

    # exibir resultado;
    click.echo(output);

# executar cli em shell.
if __name__ == '__main__':
    cli();