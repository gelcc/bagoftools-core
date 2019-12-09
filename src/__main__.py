import click;
from file_system import read_text_file;
from tokenizer import tokenize_words;

@click.group()
def cli():
    pass;

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def tokenize(file_path):

    file = click.format_filename(file_path);
    file_content = read_text_file(file)['content'];
    tokens = tokenize_words(file_content);
    click.echo(tokens);

cli();