import click

@click.group()
def setup():
    """Setup Command Line Interface"""
    pass

@setup.command()
def winenv():
    """Setup Windows environment for zq"""
    click.echo("Setting up Windows environment...")
    