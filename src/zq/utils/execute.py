

def execute_cmd(command : str, watch_non_zero : bool = False):
    # first try pwsh then fallback to powershell, then cmd
    import os
    try:
        ret = os.system("pwsh -Command " + command)
    except Exception:
        try:
            ret = os.system("powershell -Command " + command)
        except Exception:
            raise Exception("No PowerShell found in PATH")
        
    if ret != 0 and watch_non_zero:
        raise Exception(f"Command failed with exit code {ret}: {command}")
    
    return ret