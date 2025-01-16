# Getting Start

## Use virtual env

- Install pyenv

```bash
brew update
brew install pyenv

# install python with version (ex: 3.13.1)
pyenv install 3.13.1

# set python version in local
pyenv local 3.13.1

pyenv version
```

- set venv

```bash
python3.13 -m venv myaienv
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
