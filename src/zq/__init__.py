import click
from .setup import setup
from .self import selfc
@click.group()
def main():
    """ZQ Command Line Interface"""
    pass

main.add_command(setup)
main.add_command(selfc)