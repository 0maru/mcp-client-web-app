# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

MCP (Model Context Protocol) クライアントのWebアプリケーション。Nxモノレポ構造で、React フロントエンドとPython FastAPIバックエンドで構成。

### 技術スタック
- **フロントエンド**: React 19 + TypeScript 5.8 + Vite 7
- **バックエンド**: Python 3.12+ + FastAPI
- **ビルドシステム**: Nx (モノレポ管理)
- **パッケージマネージャー**: npm (frontend), uv (backend)

## アーキテクチャ

### ディレクトリ構造
```
apps/
├── client/          # React フロントエンドアプリケーション
│   ├── src/         # ソースコード
│   │   ├── App.tsx  # メインアプリコンポーネント
│   │   └── main.tsx # エントリーポイント
│   └── public/      # 静的アセット
└── server/          # Python バックエンドサーバー
    └── main.py      # FastAPI エントリーポイント
```

### 主要な設定ファイル
- `nx.json`: Nx ワークスペース設定
- `apps/client/vite.config.ts`: Vite ビルド設定
- `apps/client/tsconfig.json`: TypeScript 設定
- `apps/server/pyproject.toml`: Python プロジェクト設定

## 開発コマンド

### フロントエンド開発
```bash
# クライアントディレクトリに移動
cd apps/client

# 開発サーバー起動
npm run dev

# プロダクションビルド
npm run build

# ビルド結果のプレビュー
npm run preview

# リント実行
npm run lint
```

### バックエンド開発
```bash
# サーバーディレクトリに移動
cd apps/server

# 依存関係インストール (uvを使用)
uv sync

# FastAPIサーバー起動 (実装後)
uv run uvicorn main:app --reload
```

## 環境設定

### フロントエンド
- Vite開発サーバー: http://localhost:5173 (デフォルト)
- TypeScript strict mode 有効
- ESLint設定済み

### バックエンド
- FastAPIサーバー: http://localhost:8000 (一般的な設定)
- Python 3.12以上が必要
- uvパッケージマネージャー使用

## 現在の実装状況

- フロントエンド: React + Viteの基本テンプレート（カウンターサンプル）
- バックエンド: main.pyに最小限のコードのみ
- MCP プロトコルの実装は未着手

## 今後の実装予定

1. FastAPIサーバーの基本構造実装
2. MCPプロトコルハンドリングロジック
3. フロントエンドUI構築
4. フロントエンド・バックエンド間の通信実装
5. テストフレームワーク導入（Jest/Vitest、pytest）