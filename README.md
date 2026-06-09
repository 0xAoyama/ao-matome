# ao-matome (matrix-ao)

アニメ・AI・生活防衛の公式情報をまとめる静的サイト。

**公開URL:** https://matrix-ao.pages.dev/

## カテゴリ

- `/anime/` — アニメ・ゲーム・推し活（予約、配信、イベント、グッズ、特典比較）
- `/ai/` — 生成AIツール（公式更新、料金差分、使い方、比較表）
- `/life/` — 生活防衛（値上げ、セール、ポイント、ふるさと納税、税制変更）

## ローカル確認

```bash
# サイトビルド
cd site && npm install && npm run build

# 開発サーバー
cd site && npm run dev

# Python pipeline
pip install pyyaml
python -m matome_pipeline db init
python -m matome_pipeline sources validate
python -m matome_pipeline qa
python -m matome_pipeline run
```

## デプロイ

GitHub Actionsで `main` ブランチにpushすると自動的にCloudflare Pagesへデプロイされます。

必要なGitHub Secrets:
- `CLOUDFLARE_ACCOUNT_ID`
- `CLOUDFLARE_API_TOKEN`

## 安全方針

- `risk_level=low` の記事のみ自動公開
- `medium/high` は人間レビュー後に公開
- YMYL（医療・税・金融）記事は自動公開しない
- 本文転載・画像転載はしない
- 全記事に一次ソースURL・確認日・免責を掲載
