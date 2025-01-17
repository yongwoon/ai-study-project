# Getting Start

## Use virtual env

- Install pyenv

```bash
brew update
brew install pyenv

# install python with version (ex: 3.11.11)
pyenv install 3.11.11

# set python version in local
pyenv local 3.11.11

pyenv versions
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

## stury memo

- Load template from yaml (part2-ch01-02)
  - 02-Promot/01-PromptTemplate.ipynb

## LINKS

- [테디노트의 RAG 비법노트 안내서](https://docs.google.com/document/d/1xf4M5ZJjs3TGy6YkwZV2_I1YbJNAC1p9CL81Fap63pY/edit?tab=t.0)
- [taddy notes](https://wikidocs.net/book/14314)
- [taddy notes MAC 환경 설정](<https://teddynote.com/10-RAG%EB%B9%84%EB%B2%95%EB%85%B8%ED%8A%B8/%ED%99%98%EA%B2%BD%20%EC%84%A4%EC%A0%95%20(Mac)/>)
- [[부록] 파이썬 필수 문법 & 백엔드의 이해 GitHub](https://github.com/fastcampus-plan1/Online-Backend-Python/tree/main/fundamental#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B8%B0%EC%B4%88%EA%B0%95%EC%9D%98-%EC%BD%94%EB%93%9C-%EB%AA%A8%EC%9D%8C)

### Github

- [langchain-teddynote](https://github.com/teddylee777/langchain-teddynote)
