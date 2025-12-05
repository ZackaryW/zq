from pathlib import Path

# path to ~/.zq

ZQ_HOME = Path.home() / ".zq"
if not ZQ_HOME.exists():
    ZQ_HOME.mkdir()

    