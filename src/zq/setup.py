import click

from zq.utils.execute import execute_cmd

@click.group(invoke_without_command=True)
@click.option("--force-update", "-f", is_flag=True, help="Force update the my_win_env repository")
@click.option("--reset", "-r", is_flag=True, help="Reset my_win_env to original state")
@click.pass_context
def setup(ctx, force_update, reset):
    """Setup Commands group"""
    from zq.utils.my_win_env import update_repo, MY_WIN_ENV
    update_repo()   
    if force_update:
        update_repo(force=True)
    if reset:
        if MY_WIN_ENV.exists():
            import shutil
            shutil.rmtree(MY_WIN_ENV)
        update_repo(force=True)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@setup.command()
def crack():
    """crack"""
    from zq.utils.my_win_env import MY_WIN_ENV
    execute_cmd(str(MY_WIN_ENV / 'scripts' / 'crack.ps1'), watch_non_zero=False)

@setup.command()
def debloat():
    """debloat"""
    from zq.utils.my_win_env import MY_WIN_ENV
    execute_cmd(str(MY_WIN_ENV / 'scripts' / 'debloat.ps1'))
@setup.command()
def defaults():
    """set defaults"""
    from zq.utils.my_win_env import MY_WIN_ENV
    execute_cmd(str(MY_WIN_ENV / 'scripts' / 'setup.ps1'), watch_non_zero=False)

@setup.command()
def devenv():
    """setup development environment"""
    from zq.utils.my_win_env import MY_WIN_ENV
    execute_cmd(str(MY_WIN_ENV / 'scripts' / 'devenv.ps1'), watch_non_zero=False)
