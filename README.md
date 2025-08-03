# streamlit-llm-app
# 🤖 streamlit-llm-app

LLM を活用し、育児や栄養に関する質問に対して専門家ロールのアドバイザーからアドバイスを受けられる対話型 Streamlit アプリです。

## 🔍 主な機能

- Streamlit による Web UI
- LangChain + OpenAI API を活用した LLM 応答
- 「栄養アドバイザー」または「育児アドバイザー」をラジオボタンで選択
- 入力した質問に対し、選択されたアドバイザーとして LLM が回答
- 生成中スピナー表示あり
- `.env` に APIキーを安全に管理
- GitHub に `.env` をアップしない `.gitignore` 対応済み

## 🖼️ 使用イメージ

```text
[ 栄養アドバイザー ] [ 育児アドバイザー ]
質問を入力してください： 子どもの好き嫌いを改善するには？
→ 栄養アドバイザーとして LLM が回答
```

## 🚀 起動方法（ローカル）

1. リポジトリを clone

```bash
git clone https://github.com/tanabe1995/streamlit-llm-app.git
cd streamlit-llm-app
```

2. 仮想環境を作成して起動（任意）

```bash
python3 -m venv env
source env/bin/activate
```

3. 依存ライブラリをインストール

```bash
pip install -r requirements.txt
```

4. `.env` を作成し、OpenAI API キーを記述

```env
OPENAI_API_KEY=sk-xxxxxxx
```

5. アプリを起動

```bash
streamlit run app.py
```

## 📦 主なライブラリ

- `streamlit`
- `langchain`
- `langchain_openai`
- `openai`
- `python-dotenv`

## 🌐 デプロイ

Streamlit Cloud 上に簡単にデプロイ可能です。`.env` を Cloud 上の「Secrets」機能で管理してください。

---

## 📄 ライセンス

MIT License

---

## 🙋‍♂️ 作成者

- [tanabe1995](https://github.com/tanabe1995)