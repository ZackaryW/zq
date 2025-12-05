import re

with open('pyproject.toml', 'r') as f:
    content = f.read()

match = re.search(r'version = "(\d+)\.(\d+)\.(\d+)"', content)
if match:
    major, minor, patch = map(int, match.groups())
    new_version = f"{major}.{minor}.{patch + 1}"
    new_content = re.sub(r'version = "\d+\.\d+\.\d+"', f'version = "{new_version}"', content)
    
    with open('pyproject.toml', 'w') as f:
        f.write(new_content)
    
    print(f"Version bumped to {new_version}")
