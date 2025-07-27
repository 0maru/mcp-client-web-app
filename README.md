# MCP Client Web App

MCP (Model Context Protocol) クライアントのWebアプリケーション

## セットアップ

### LiteLLMの起動

1. 環境変数の設定
```bash
cp .env.example .env
# .envファイルを編集してAPIキーを設定
```

2. Docker Composeで起動
```bash
docker-compose up -d
```

3. LiteLLMプロキシにアクセス
- URL: http://localhost:4000
- Master Key: `.env`で設定した`LITELLM_MASTER_KEY`

### 開発

#### フロントエンド
```bash
cd apps/client
npm install
npm run dev
```

#### バックエンド
```bash
cd apps/server
uv sync
uv run uvicorn main:app --reload
```