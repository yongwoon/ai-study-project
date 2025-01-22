# Python 3.13.1 を使用するために Poetry を再設定する手順です：

1. まず Poetry 自体を再インストール:

```bash
# Poetry をアンインストール
curl -sSL https://install.python-poetry.org | python3 - --uninstall

# Poetry を再インストール
curl -sSL https://install.python-poetry.org | python3 -
```

2. Poetry の設定で Python のパスを明示的に指定:

```bash
# pyenv で Python 3.13.1 を使用している場合のパスを指定
poetry config virtualenvs.prefer-active-python true
```

3 プロジェクトの設定を更新:

```bash
# pyproject.toml の python バージョンを確認・更新
# [tool.poetry.dependencies] セクションで
# python = "^3.13.1" となっているか確認

# 既存の仮想環境を削除
rm -rf .venv
rm -rf ~/Library/Application\ Support/pypoetry/venv

# プロジェクトの依存関係を再インストール
poetry install
```

正しい Python バージョンが使用されているか確認:

```bash
poetry run python --version
```

もし特定のエラーが発生する場合は、エラーメッセージを共有していただければ、より具体的な解決方法をご案内できます。
