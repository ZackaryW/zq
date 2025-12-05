import click
from .setup import setup

@click.group()
def main():
    """ZQ Command Line Interface"""
    pass

main.add_command(setup)