

import click


@click.group("self")
def selfc():
    """Self Commands group"""
    pass

@selfc.command()
def update():
    """Update zq"""
    import os
    import sys
    os.system(f"{sys.executable} -m pip install --upgrade git+https://github.com/ZackaryW/zq.git")