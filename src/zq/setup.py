import os
import click

from zq.utils.my_win_env import MY_WIN_ENV

@click.group()
def setup():
    """Setup Commands group"""
    pass

@setup.command()
def crack():
    """crack"""
    os.system(MY_WIN_ENV / 'scripts' / 'crack.ps1')

    