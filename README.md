# Getting Start

## Use virtual env

- Install pyenv

```bash
brew update
brew install pyenv
```

- set venv

```bash
python3.11 -m venv myaienv
```

- virtual env コマンド

```bash
# activate env
source myaienv/bin/activate

# deactivate
deactivate
```

## Poetry Command

```bash
# Add package
poetry install

# update package
poetry update

# check current env
poetry env info

# Add package
poetry add <package_name>

# Add package with version
poetry add <package_name>==<version>

# Add package with version
poetry add <package_name>==<version>
```
