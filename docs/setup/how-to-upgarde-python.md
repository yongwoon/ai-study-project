Python 버전 변경 방법 (pyenv + poetry)

1. pyenv로 Python 설치

```bash
# 설치 가능한 버전 확인
pyenv install --list

# 원하는 버전 설치 (예: 3.9.13)
pyenv install 3.9.13
```

2. 프로젝트 Python 버전 변경

```bash
# 프로젝트 디렉토리에서
pyenv local 3.9.13

# 버전 확인
python --version
```

3. Poetry 환경 변경

```bash
# 기존 가상환경 제거
poetry env remove current

# 새로운 Python 버전으로 가상환경 생성
poetry env use python3.9

# 의존성 패키지 재설치
poetry install
```

4. pyproject.toml 수정

```toml
[tool.poetry.dependencies]
python = "^3.9" # 변경한 버전에 맞게 수정
```

5. 확인 단계

```bash
# Python 버전 확인
pyenv version
python --version

# Poetry 환경 확인
poetry env info
```

Note: 위 단계들을 순서대로 진행하면 pyenv로 Python 버전을 관리하면서 Poetry 환경도 함께 변경할 수 있습니다.
