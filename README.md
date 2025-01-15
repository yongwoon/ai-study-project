# Getting Start

### Use virtual env

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

- Install poetry (virtual env 가 activated 된 상태에서 진행하기)

```bash
pip3 install poetry

# 파이썬 가상환경 설정
poetry shell

# 파이썬 패키지 일괄 업데이트
poetry update
```
