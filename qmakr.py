import click
from functions import generate


@click.command()
@click.option('--number', '-n', help='Number of questions to generate.', required=True)
@click.option('--target', '-t', help='Target URL address used to generate response questions.', required=True)
@click.option('--intro', '-a', type=bool, default=True, help='Turns on the program introduction. (defaults to True)')
def qmakr(number, target, intro):
    '''
    qmakr is a fast and easy question making CLI tool using only two arguments.
    '''
    if intro == True:
        click.echo(click.style("""
                  _       
  __ _ _ __  __ _| |___ _ 
 / _` | '  \/ _` | / / '_|
 \__, |_|_|_\__,_|_\_\_|  
    |_|                   
""", fg='green'))
        click.echo(click.style("Welcome to qmakr! Your lightweight and easy to use question generator.", fg='green'))
        click.echo(f'Below are your {number} questions from {target}:\n')
    click.echo(generate(number, target), nl=False)

