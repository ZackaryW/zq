
from functools import cache
import os


# go to roaming app data/obsidian folder
def get_obsidian_config_dir():
    appdata = os.getenv("APPDATA")
    obsidian_path = os.path.join(appdata, "Obsidian")
    return obsidian_path

@cache
def get_config():
    config_dir = get_obsidian_config_dir()
    config_file = os.path.join(config_dir, "obsidian.json")
    if os.path.exists(config_file):
        import json
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def open_vault(id):
    import subprocess
    import platform
    if platform.system() == "Windows":
        subprocess.run(["cmd", "/c", "start", f"obsidian://open?vault={id}"], shell=False)  
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", f"obsidian://open?vault={id}"])
        
def get_vault_id(name : str):
    for vault_id, vault in get_config().get("vaults", {}).items():
        path = vault.get("path", None)
        if not path:
            continue
        vault_name = path.split(os.sep)[-1]
        if vault_name == name:
            return vault_id
        
def get_vault_id2(index : int):
    vaults = list(get_config().get("vaults", {}).items())
    if index < 0 or index >= len(vaults):
        return None
    vault_id, vault = vaults[index]
    return vault_id