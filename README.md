# ao-matome (matrix-ao)

アニメの配信・グッズ予約・特典比較を公式情報だけでまとめる推し活ナビ。

**公開URL:** https://matrix-ao.pages.dev/

> 2026-06-12 にジャンルを「アニメ・推し活」単一バーティカルへ再構築（[docs/genre-pivot-2026-06-12.md](docs/genre-pivot-2026-06-12.md)）。
> 旧3カテゴリ構成（anime/ai/life）は `v0.0.1` タグに残っています。

## サイト構造

- `/streaming/` — 配信どこで見れるDB（作品×サービス対応表）← **主力マネーページ**
- `/streaming/[slug]/` — 作品別 配信サービス比較（料金・無料期間・CTA）
- `/goods/` — グッズ予約・店舗別特典比較 ← **補助マネーページ**
- `/goods/[slug]/` — 商品別 価格・特典比較
- `/news/` — ニュース・トレンド記事（集客エンジン → DBページへ送客）

## データ

- `data/public/streaming.json` — 配信対応表データ。`sample: true` はデモデータ（UIにデモ表示が出る）
- `data/public/goods.json` — 予約・特典比較データ（締切昇順で表示）
- `site/src/config/affiliates.ts` — **アフィリエイトリンク管理**。ASP承認後にURLを設定すると全ページのCTAが差し替わり、PR表記も自動で付く。null の間は公式リンクにフォールバック

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

## 収益化の手順（運用メモ）

1. 楽天アフィリエイト登録（審査なし）→ `affiliates.ts` の `rakuten` に設定
2. もしもアフィリエイト登録 → Amazon / Yahoo の提携 → `amazon` に設定
3. A8.net / afb 登録 → VOD案件（U-NEXT・DMM TV等）の提携申請 → `VOD_AFFILIATE_URLS` に設定
4. デモデータ（`sample: true`）を実データに差し替えてから集客を開始する

## 安全方針

- `risk_level=low` の記事のみ自動公開、`medium/high` は人間レビュー後に公開
- YMYL（医療・税・金融）記事は扱わない
- 本文転載・画像転載はしない
- 全記事・全DBページに一次ソースURL・確認日・免責を掲載
- アフィリエイトリンクにはPR表記（`rel="nofollow sponsored"` 付き）
