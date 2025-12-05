import os
import click

@click.group()
def setup():
    """Setup Commands group"""
    pass

@setup.command()
def crack():
    """crack"""
    from zq.utils.my_win_env import MY_WIN_ENV
    os.system(MY_WIN_ENV / 'scripts' / 'crack.ps1')

@setup.command()
def debloat():
    """debloat"""
    from zq.utils.my_win_env import MY_WIN_ENV
    os.system(MY_WIN_ENV / 'scripts' / 'debloat.ps1')

@setup.command()
def defaults():
    """set defaults"""
    from zq.utils.my_win_env import MY_WIN_ENV
    os.system(MY_WIN_ENV / 'scripts' / 'setup.ps1')

@setup.command()
def devenv():
    """setup development environment"""
    from zq.utils.my_win_env import MY_WIN_ENV
    os.system(MY_WIN_ENV / 'scripts' / 'devenv.ps1')
