import click
import os
from zq.utils.obsidian import get_config, get_vault_id, get_vault_id2, open_vault

@click.group("obsidian")
def obsidian():
    """Obsidian Commands group"""
    pass

@obsidian.command()
def list():
    config = get_config()
    vaults = config.get("vaults", {})
    for vault_id, vault in vaults.items():
        path = vault.get("path", None)
        if not path:
            continue
        if not os.path.exists(path):
            continue

        click.echo(f"Vault ID: {vault_id}")
       
        name = path.split(os.sep)[-1]
        click.echo(f"  Name: {name}")
        click.echo(f"  Path: {path}")
        click.echo("")
        
@obsidian.command("open")
@click.argument("vault_name", required=False)
def open_(vault_name):
    """
    opens the obsidian vault with the given name.
    """
    if not vault_name:
        click.echo("Please select a vault to open:")
        ctx = click.get_current_context()
        ctx.invoke(list)

        # at the end we need the id
        # select by index
        vault_name = click.prompt("Enter the name or index of the vault to open", type=str)
    if vault_name.isdigit():
        id = get_vault_id2(int(vault_name))
    else:
        id = get_vault_id(vault_name)
        
    if not id:
        click.echo(f"Vault '{vault_name}' not found.")
        return
    
    open_vault(id)