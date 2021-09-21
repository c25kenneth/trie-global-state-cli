import typer
import requests

typerApp = typer.Typer()
url = 'https://global-trie-cli.herokuapp.com/updatetrie/'
@typerApp.command()
def list():
    response = requests.get(url+'list')
    typer.echo(response.text)

@typerApp.command()
def check(word: str):
    response = requests.get(url + 'check/'+word)
    typer.echo(response.text)

@typerApp.command()
def recommend(prefix: str):
    response = requests.get(url+'recommend/'+prefix)
    typer.echo(response.text)

@typerApp.command()
def remove(word: str):
    try:
        response = requests.get(url+'remove/'+word)
        typer.echo(response.text)
    except:
        typer.echo('Word does not exist in Trie!')


@typerApp.command()
def add(word: str):
    response = requests.get(url+'add/'+word)
    typer.echo(response.text)
if __name__ == '__main__':
    typerApp()