# Bag Of Tools - Core
# módulo principal para a definição dos comandos.

# biblioteca utilizada para definir os comandos.
import click;

# função para ler um arquivo de texto.
import src.file_system;

# módulo tokenizador.
import src.tokenizer;

# definir grupo de comandos.
@click.group()
def cli():
    pass;

# comando para tokenizar um arquivo de texto.
@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def tokenize(file_path):

    # função para receber o local do arquivo.
    formated_file_path = click.format_filename(file_path);

    # ler arquivo de texto.
    file = read_text_file(formated_file_path);

    # receber conteúdo do arquivo de texto.
    file_content = file['content'];

    # tokenizar palavras.
    tokens = tokenize_words(file_content);
    
    # exibir tokens.
    click.echo(tokens);

@cli.command()
def hello():
    click.echo('olá');