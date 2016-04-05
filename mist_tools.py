#mist-tools v0.1
#author: ravi sheth, wang lab, columbia university
#last updated 4/5/2016
import click

@click.group()
def cli():
    pass

@cli.command()
def process():
	 """process seq files"""
	 click.echo('Initialized the database')