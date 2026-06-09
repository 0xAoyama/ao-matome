# まとめサイト3本 運営戦略 2026-06-09

## 結論

短期流入、中期収益、長期資産化、自動化容易性、法務/SEOリスクのバランスで、まず運営する3本は以下を推奨する。

1. アニメ・ゲーム・推し活：予約、配信、イベント、グッズ、特典比較DB
2. 生成AIツール：公式更新、料金差分、使い方、業務テンプレ、比較表
3. 生活防衛：値上げ、セール、ポイント、ふるさと納税/税制変更カレンダー

避ける、または人間レビュー必須にすべき領域：芸能炎上、健康医療、投資断定、給付金/補助金の申請助言。

## 根拠として確認したURL

- Google Trends 日本 Daily Search Trends RSS: https://trends.google.co.jp/trending/rss?geo=JP
  - 確認時点で「安達祐実」「えなこ」「ティアフォー」「フランス」「ソフトバンクグループ」「ピーチ」「クイズ ドレミファドン」「趣里」「arte refact」など。短期流入は人物、テレビ、企業、スポーツ、作品/イベントが強い。
- Google Year in Search 日本: https://trends.google.co.jp/trends/yis/2025/JP/
- Google 検索スパムポリシー: https://developers.google.com/search/docs/essentials/spam-policies?hl=ja
- Google 2024年3月コアアップデート/スパムポリシー: https://developers.google.com/search/blog/2024/03/core-update-spam-policies?hl=ja
- 文化庁 著作権: https://www.bunka.go.jp/seisaku/chosakuken/
- JNTO 訪日外客統計: https://www.jnto.go.jp/statistics/data/visitors-statistics/
- 総務省統計局 消費者物価指数: https://www.stat.go.jp/data/cpi/
- 国税庁: https://www.nta.go.jp/
- 総務省 ふるさと納税: https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/furusato/
- OpenAI News: https://openai.com/news/
- Google AI Blog: https://blog.google/technology/ai/
- Anthropic News: https://www.anthropic.com/news

## 評価表

| 領域 | 短期流入 | 中期収益 | 長期資産性 | 自動化 | リスク | 推奨度 |
|---|---:|---:|---:|---:|---:|---:|
| アニメ・ゲーム・推し活 | 5 | 4 | 4 | 5 | 3 | 5 |
| 生成AIツール/業務活用 | 4 | 5 | 4 | 5 | 3 | 5 |
| 生活防衛/値上げ/セール/ポイント | 4 | 5 | 4 | 4 | 4 | 4 |
| 旅行・イベント・季節カレンダー | 4 | 4 | 3 | 4 | 3 | 3 |
| 補助金・給付金・自治体制度 | 3 | 4 | 4 | 3 | 5 | 2 |
| 芸能・炎上・人物まとめ | 5 | 2 | 1 | 2 | 5 | 1 |
| 健康・感染症・医療 | 4 | 3 | 3 | 3 | 5 | 1 |

## サイトA：アニメ・ゲーム・推し活 予約/配信/イベントDB

### 狙うクエリ

- 作品名 + グッズ予約 + 特典比較
- 作品名 + 配信どこ + 何時から
- ライブ名 + セトリ + 持ち物 + 会場アクセス
- ゲーム名 + ガチャ + 当たり + いつまで
- コラボカフェ + 予約 + グッズ
- 声優名 + イベント + チケット

### 差別化

ただのニュース転載ではなく、DB/表にする。

- 発売日カレンダー
- 店舗別特典比較
- 予約受付中/終了ステータス
- 配信サービス別対応表
- 会場アクセス、ホテル、遠征チェックリスト
- 公式発表へのリンク

### 収益化

Amazon、楽天、Yahooショッピング、アニメイト、DMM、電子書籍、VOD、チケット、ライブ配信、Adsense。

### 自動化パイプライン

1. 公式RSS、PR、EC API、Google Trends RSS、YouTube公式チャンネルを収集
2. 作品名、商品名、発売日、価格、店舗、特典、公式URLを抽出
3. 既存DBと照合し、新規/変更/終了を判定
4. 記事テンプレートに差し込み
5. 著作権リスクがある画像・SNS引用・ネタバレを検知したら人間レビュー
6. 公開後、X/Threads用の短文を生成

### 注意

画像、漫画コマ、歌詞、動画、SNS投稿本文の無断転載は避ける。公式リンク、OGP、商品リンク、短い引用に留める。

## サイトB：生成AIツール比較・ニュース・業務テンプレ

### 狙うクエリ

- ChatGPT 新機能 使い方
- Gemini と ChatGPT 比較
- Claude 料金 日本円
- Sora 使い方 日本
- AIツール 無料 比較
- 業務別 AIプロンプト
- AIエージェント 使い方
- 〇〇 API 料金 変更

### 差別化

速報翻訳だけではなく、実用差分を出す。

- 公式発表の要点
- 日本ユーザー向けの料金表
- できること/できないこと
- UI手順スクショまたは再現手順
- 業務別テンプレ
- プロンプト例
- 類似ツール比較表
- API料金の変更履歴

### 収益化

AI SaaSアフィリエイト、法人リード、講座/教材、テンプレ販売、有料メルマガ、広告。

### 自動化パイプライン

1. OpenAI、Google AI、Anthropic、主要AI SaaSのニュース/ブログ/Docs/料金ページを監視
2. diffを取り、料金、モデル名、機能名、提供地域を抽出
3. 変更種別を分類：新機能、料金、廃止、障害、API、事例
4. 要約、比較表、FAQ、SNS投稿を生成
5. 実測が必要な記事だけ人間が確認
6. 週次で「今週のAI更新まとめ」を自動生成

### 注意

架空機能、誤訳、誇大な副業訴求は避ける。Googleのスパムポリシー上、独自価値のない大量生成記事に見えないよう、比較表、実測、手順、更新履歴を入れる。

## サイトC：生活防衛ニュース 値上げ/セール/ポイント/税制カレンダー

### 狙うクエリ

- 2026年 値上げ 一覧
- 今月 値上げ 食品
- Amazon セール いつ
- 楽天 スーパーセール いつ
- ポイント還元 キャンペーン 一覧
- ふるさと納税 改正 2026
- 年末調整 変更点
- 住民税 いつから

### 差別化

「今月/今週/締切」の更新型DBにする。

- 値上げカレンダー
- 食品/日用品カテゴリ別一覧
- セール日程カレンダー
- ポイント還元率比較
- ふるさと納税変更点の公式リンク集
- 期限切れ記事の自動アーカイブ

### 収益化

EC、クレジットカード、ポイントサイト、ふるさと納税、家計簿アプリ、通信回線、広告。

### 自動化パイプライン

1. 企業プレスリリース、ECセールページ、総務省/国税庁/統計局の公式情報を監視
2. 商品名、カテゴリ、変更日、変更率、公式URLを抽出
3. 古い情報を自動で非表示または「過去情報」に移動
4. YMYL判定がある記事は下書き止め
5. 公式リンク、確認日、免責、広告表記を自動挿入

### 注意

税、金融、保険、投資はYMYL。断定的な助言ではなく、公式情報への導線と比較表に留める。専門家監修がない場合は「一般情報」と明記する。

## 共通の自動化設計

### データモデル

最低限、以下を持つ。

- source_url: 一次情報URL
- source_name: 発表元
- fetched_at: 取得日時
- published_at: 発表日時
- topic: 主題
- entities: 作品名、商品名、人物名、企業名、自治体名など
- event_date: 発売日、開始日、終了日、締切日
- risk_level: low / medium / high
- ymyl: true / false
- copyright_risk: true / false
- generated_status: draft / review / published / archived
- canonical_key: 重複排除キー

### 処理フロー

| 工程 | 自動化内容 | 人間確認が必要な条件 |
|---|---|---|
| 収集 | RSS、サイトマップ、API、公式ページ、Google Trends RSS | スクレイピング禁止/robots不明 |
| 正規化 | 日付、URL、固有名詞、カテゴリ抽出 | 発表元が不明 |
| 重複排除 | canonical_key、URL、タイトル類似度、埋め込み類似度 | 同名別イベントの可能性 |
| 要約 | 公式発表の要点化 | 人物、炎上、医療、税、金融 |
| 独自価値付与 | 表、カレンダー、FAQ、チェックリスト、比較 | 主観評価が必要 |
| 品質ゲート | 引用量、公式URL、広告表記、YMYL判定 | 高リスク記事 |
| 公開 | CMS APIで予約投稿 | リスクmedium以上 |
| 配信 | X/Threads/RSS/メール | 炎上・人物系 |
| 計測 | GSC、GA4、クリック、CV、順位 | 急落/警告検知時 |

## 推奨スタック

小さく始めるなら以下。

- 収集: blogwatcher-cli、Python feedparser、Playwright、サイトマップ取得
- DB: SQLite または Postgres
- 生成: LLM API + 固定テンプレート + JSON Schema
- 類似度: embeddings + pgvector または sqlite-vss
- CMS: WordPress REST API または Astro/Next.js静的生成
- 配信: X API、Threadsは手動/半自動、RSS、メール
- 計測: Google Search Console API、GA4、アフィリエイト管理画面CSV
- 実行: cron、GitHub Actions、またはHermes cronjob

## 30/90/180日ロードマップ

### 0-30日

- 3サイト共通の収集DBと記事テンプレを作る
- まず各サイト50記事相当のDBページ/一覧ページを作る
- 全記事に一次ソース、更新日、広告表記、免責を入れる
- Google Trends RSSと公式RSSだけで毎日ネタ候補を出す
- 公開は人間承認にする

KPI:
- 公開記事: 各30-50本
- インデックス: 50%以上
- GSC表示回数: 合計1,000以上
- SNS投稿: 1日3-10本

### 31-90日

- 勝ちクエリが見えた領域に集中
- 一覧/カレンダー/比較表ページを強化
- 内部リンクを自動生成
- 古い記事の自動更新/アーカイブを実装
- 収益リンクを設置

KPI:
- GSC表示回数: 月10万
- 月間PV: 1万-5万
- 収益: 月1万-5万円の兆し
- 自動生成下書き採用率: 60%以上

### 91-180日

- データベース型ページを増やす
- メルマガ/RSS/LINEなどリピート導線を作る
- API差分監視、価格差分監視を増やす
- 人間レビュー対象をリスク判定で絞る
- 収益性の低い記事タイプを停止

KPI:
- 月間PV: 10万以上
- 収益: 月10万円以上を狙う
- 下書きから公開までの人間作業: 1記事5分未満

## やらないこと

- ニュース本文の転載
- SNS投稿の大量転載
- 画像/漫画コマ/歌詞の無断転載
- 炎上見出しの自動公開
- 医療/投資/税金の断定助言
- 公式ソースがない記事の公開
- 内容が薄いAI記事の量産

## URLで読める状態まで持っていく具体MVP

ここが最初の実装ゴール。単にローカルでMarkdownを生成するだけではなく、実際にブラウザで読めるURLを出すところまでをMVPの完了条件にする。

### MVPの完成URL

既存GitHubリポジトリは `git@github.com:0xAoyama/ao-matome.git` だが、GitHub Pagesだと `0xaoyama.github.io` が表に出る。MVPの標準公開先は Cloudflare Pages にする。

想定URL:

- ポータル: `https://matrix-ao.pages.dev/`
- アニメ・ゲーム・推し活: `https://matrix-ao.pages.dev/anime/`
- 生成AIツール: `https://matrix-ao.pages.dev/ai/`
- 生活防衛: `https://matrix-ao.pages.dev/life/`
- 個別記事例: `https://matrix-ao.pages.dev/ai/2026-06-09-example-update/`

独自ドメインはMVP後でよい。最初はCloudflare Pagesの `pages.dev` URLで「読める」「共有できる」「Search Consoleに登録できる」状態を優先する。

Cloudflare Account ID:

- `3fd8c3817a6383daf0ac5377de152d68`

GitHub Actionsでdeployする場合に必要なSecret:

- `CLOUDFLARE_ACCOUNT_ID`: `3fd8c3817a6383daf0ac5377de152d68`
- `CLOUDFLARE_API_TOKEN`: Cloudflare Dashboardで作成するPages deploy用API token。チャットには貼らず、GitHub Secretsに入れる。

### MVPのシステムリソース

| 用途 | MVPで使うもの | 理由 | 後で置き換える候補 |
|---|---|---|---|
| ソースコード | GitHub repo: `0xAoyama/ao-matome` | 既存リポジトリをそのまま使える | サイト別repo分割 |
| 公開ホスティング | Cloudflare Pages | 無料、静的サイト、URLにGitHubユーザー名が出ない、後でWorkers/D1/R2へ拡張しやすい | Vercel / Netlify / GitHub Pages |
| ビルド実行 | GitHub Actions | cron実行とPages deployを同居できる | Cloudflare Workers Cron / VPS cron |
| サイト生成 | Astro または素のPython静的HTML生成 | まずはDBページ中心なので静的で十分 | Next.js / WordPress |
| データ保存 | `data/items.sqlite` と `data/public/*.json` | MVPは小規模。DBと公開JSONで足りる | Supabase Postgres / Cloudflare D1 |
| 下書き出力 | `content/drafts/*.md` | 人間レビューしやすい | CMS下書きAPI |
| 公開記事 | `content/sites/{anime,ai,life}/posts/*.md` | Git差分でレビュー可能 | WordPress / Headless CMS |
| 監視ソース | `config/sources.yaml` | サイト別にRSS/公式URLを管理 | 管理画面化 |
| 品質ゲート | `qa_gate.py` | 自動公開事故を止める | 管理画面承認フロー |
| 計測 | GSC/GA4はMVP後 | まずURL完成を優先 | Search Console API / GA4 API |

### MVPのディレクトリ構成

```text
/Users/tao/repos/ao-matome/
  config/
    sources.yaml
  data/
    items.sqlite
    public/
      anime.json
      ai.json
      life.json
  content/
    drafts/
    sites/
      anime/posts/
      ai/posts/
      life/posts/
  matome_pipeline/
    __init__.py
    db.py
    fetcher.py
    classifier.py
    dedupe.py
    generator.py
    qa_gate.py
    publisher.py
    cli.py
  site/
    package.json
    astro.config.mjs
    src/pages/index.astro
    src/pages/anime/index.astro
    src/pages/ai/index.astro
    src/pages/life/index.astro
    src/pages/[site]/[slug].astro
  .github/workflows/
    pages.yml
    collect.yml
```

### MVPの公開フロー

```text
config/sources.yaml
  -> fetcher.py がRSS/公式ページを取得
  -> items.sqlite に保存
  -> classifier.py がカテゴリ/YMYL/著作権/人物リスクを判定
  -> dedupe.py が重複排除
  -> generator.py がMarkdown下書き生成
  -> qa_gate.py が公開可否を判定
  -> publisher.py が low-risk のみ content/sites/ に移動
  -> Astro が静的HTMLを生成
  -> GitHub Actions が Cloudflare Pages にdeploy
  -> https://matrix-ao.pages.dev/ で読める
```

重要: 初期MVPでは `risk_level=low` の記事だけ自動公開する。`medium/high` は `content/drafts/` に残して、人間確認後に公開する。

### 最初に作るページ

MVPでは3サイトそれぞれに最低限以下を作る。

| URL | 内容 | 完成条件 |
|---|---|---|
| `/` | 3サイトへのポータル | 3カテゴリへのリンク、最新記事一覧が見える |
| `/anime/` | アニメ・ゲーム・推し活一覧 | 予約/配信/イベント候補がカード表示される |
| `/ai/` | 生成AIツール一覧 | 公式更新/料金差分/使い方案件がカード表示される |
| `/life/` | 生活防衛一覧 | 値上げ/セール/ポイント/税制候補がカード表示される |
| `/{site}/{slug}/` | 個別記事 | タイトル、要約、一次ソース、更新日、免責、関連リンクが表示される |

### 最初の実装タスク

1. Cloudflare Pages向けの静的サイト方式を確定する
   - MVPは `site/` 配下のAstroを推奨
   - 完成条件: ローカルで `npm run build` が通る

2. `config/sources.yaml` を作る
   - 3サイトの監視元をまず各10件登録する
   - 30件ずつは後で増やす
   - 完成条件: `python -m matome_pipeline sources validate` が通る

3. `matome_pipeline/db.py` を作る
   - SQLiteスキーマを作成する
   - `source_url`, `source_name`, `fetched_at`, `published_at`, `topic`, `entities`, `risk_level`, `ymyl`, `copyright_risk`, `generated_status`, `canonical_key` を持つ
   - 完成条件: `python -m matome_pipeline db init` で `data/items.sqlite` ができる

4. `matome_pipeline/fetcher.py` を作る
   - RSS/Atomを取得してSQLiteに保存する
   - HTMLスクレイピングはMVP後でよい
   - 完成条件: `python -m matome_pipeline fetch --site ai` で新規itemが保存される

5. `matome_pipeline/classifier.py` を作る
   - カテゴリ、YMYL、著作権リスク、人物/炎上リスクを判定する
   - 完成条件: `python -m matome_pipeline classify --site ai` で `risk_level` が入る

6. `matome_pipeline/dedupe.py` を作る
   - URL、タイトル正規化、canonical_keyで重複排除する
   - 完成条件: 同じRSSを2回取得しても公開候補が増えない

7. `matome_pipeline/generator.py` を作る
   - 記事下書きMarkdownを生成する
   - 公式本文の転載ではなく、短い要約、一次ソース、確認日、FAQ、関連リンクを出す
   - 完成条件: `content/drafts/` にMarkdownが生成される

8. `matome_pipeline/qa_gate.py` を作る
   - 一次ソースURL、更新日、広告表記、免責、引用量、YMYL、人物/炎上を検査する
   - 完成条件: high-risk記事は自動公開されずdraftに残る

9. `matome_pipeline/publisher.py` を作る
   - `risk_level=low` だけ `content/sites/{site}/posts/` に移動する
   - 完成条件: `python -m matome_pipeline publish --site ai` で公開用Markdownができる

10. Astroの一覧/個別ページを作る
    - `content/sites/*/posts/*.md` からページ生成する
    - 完成条件: `cd site && npm run build` で `dist/` ができる

11. GitHub Actions Cloudflare Pages deployを作る
    - `.github/workflows/pages.yml` を作る
    - push時に `site/` をbuildし、Cloudflare Pagesへdeployする
    - `cloudflare/wrangler-action` を使う
    - 必要Secret: `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`
    - 完成条件: GitHub Actionsのdeployが成功する

12. Cloudflare Pagesプロジェクトを作成する
    - Project name: `matrix-ao`
    - Production branch: `main`
    - GitHub連携またはWrangler deployを使う
    - 完成条件: `https://matrix-ao.pages.dev/` がHTTP 200を返す

13. 最初の3サイトに各3本のサンプル記事を出す
    - 合計9記事
    - すべて一次ソースURL、更新日、免責つき
    - 完成条件: `/anime/`, `/ai/`, `/life/` の各URLで記事が読める

14. 日次収集workflowを作る
    - `.github/workflows/collect.yml`
    - 毎日JST朝に収集、下書き生成、low-riskのみ公開、Pages deploy
    - 完成条件: workflow_dispatchで手動実行できる

15. 完成確認をする
    - `curl -I https://matrix-ao.pages.dev/` が `200` を返す
    - トップ、3カテゴリ、個別記事のURLをブラウザで確認する
    - そのURLを作業報告に必ず載せる

### MVP完了条件

以下を満たすまでMVPは完了扱いにしない。

- `https://matrix-ao.pages.dev/` が実際に開ける
- `/anime/`, `/ai/`, `/life/` が実際に開ける
- 各カテゴリに最低3本、合計9本の記事がある
- 各記事に一次ソースURL、更新日、確認日、免責がある
- high-risk/YMYL/人物炎上系が自動公開されない
- GitHub Actionsでbuild/deployが再現できる
- 作業報告に確認用URLを載せられる

### MVPと本番運用のシステム構成比較

MVPでは「URLで読める」「安全に下書き/公開を分けられる」「GitHub Actionsで再現deployできる」ことを優先する。本番運用では「3サイトを継続更新できる」「計測と収益化を回せる」「障害・スパム・法務リスクを抑えられる」ことを優先する。

| 項目 | MVP構成 | 本番運用構成 | 移行判断 |
|---|---|---|---|
| 公開URL | `https://matrix-ao.pages.dev/` 配下に3カテゴリを置く | 独自ドメイン、または3サイト別ドメイン/サブドメイン | GSCで流入兆候が出たら独自ドメイン化 |
| サイト分割 | 1 repo / 1 Pages / `/anime`, `/ai`, `/life` | 1 repo multi-site継続、またはサイト別repo/サイト別ドメイン | 収益・運用方針が分かれたら分割 |
| ホスティング | Cloudflare Pages | Cloudflare Pages / Vercel / Netlify / VPS / WordPress | build時間、予約投稿、リダイレクト、独自機能が足りなくなったら移行 |
| ビルド | GitHub Actionsで静的build | GitHub Actions + queue + preview環境 + rollback | 自動更新頻度が日次以上になったら強化 |
| サイト生成 | Astro静的サイト | Astro/Next.js/Headless CMS/WordPress | 編集者・承認者が増えたらCMS検討 |
| データ保存 | SQLite: `data/items.sqlite` | Postgres/Supabase/Cloudflare D1/R2 | 件数が数万、複数worker、検索/管理画面が必要になったら移行 |
| 公開データ | Markdown + JSON | DB/API + Markdown生成、またはCMS記事 | 手動レビュー・再生成がつらくなったら移行 |
| 収集 | RSS/Atom中心、必要最小限の公式ページ | RSS、サイトマップ、API、差分監視、Playwright、価格/在庫監視 | 収集元が各サイト30件超になったらジョブ管理を強化 |
| 実行スケジュール | GitHub Actions cron + workflow_dispatch | cron worker、queue、retry、失敗通知、レート制限管理 | 失敗やタイムアウトが増えたら移行 |
| 生成 | テンプレ + LLM要約でMarkdown下書き | テンプレ、LLM、embeddings、RAG、記事タイプ別プロンプト | 記事タイプが増えたらプロンプト/テンプレを分離 |
| 重複排除 | URL、タイトル正規化、canonical_key | embedding類似度、クラスタリング、イベントID/商品ID管理 | 同一ネタ重複が目立ったら強化 |
| QAゲート | low-riskのみ自動公開、medium/highはdraft | policy engine、承認UI、監査ログ、専門家レビュー導線 | YMYL/人物/炎上記事を扱うなら必須 |
| 承認フロー | Git差分/Markdown確認 | 管理画面、レビュー状態、担当者、公開予約 | 人間レビューが週数十本を超えたら導入 |
| 配信 | Cloudflare Pagesへdeploy | CDN、キャッシュ制御、OGP画像生成、RSS、メール、SNS | SNS/Discover狙いを始めたらOGP生成を追加 |
| 計測 | MVP後。手動でURL確認 | GSC API、GA4 API、順位、CTR、CV、収益CSV | 30記事以上公開したら導入 |
| 収益化 | まず広告表記・免責のみ準備 | Adsense、ASP、商品リンク管理、クリック計測、ABテスト | 月間PV/クリックが出始めたら導入 |
| SEO | sitemap、title、description、内部リンク最低限 | 構造化データ、canonical、schema、内部リンク最適化、古い記事更新 | インデックス後にGSCを見て改善 |
| 法務/著作権 | 本文転載禁止、一次ソースURL、引用最小限 | 引用監査、画像権利管理、robots確認、削除依頼対応 | 外部画像/SNS/人物系を扱うなら強化 |
| 監視/障害対応 | GitHub Actions失敗を見る | Slack/メール通知、Sentry、ログ集約、失敗リトライ | 自動更新が収益に影響し始めたら導入 |
| バックアップ | Git管理 + SQLite artifact | DB backup、記事backup、設定backup、復元手順 | 本番DB移行時に必須 |
| セキュリティ | GitHub Secrets最小限 | secret管理、権限分離、依存関係監査、CMS認証 | APIキー/外部投稿が増えたら強化 |
| 運用コスト | ほぼ無料 | 月数千円〜数万円。DB、LLM、監視、CMS、CDN、API費用 | 月間収益が固定費を上回る見込みで拡張 |

### フェーズごとの構成比較

Coding Agent AIがある前提では、「雑なMVP」は不要。最初から本番品質の薄い縦スライスを作る。ただし、未検証テーマに最初からフル本番インフラを張るのは避ける。

| フェーズ | 目的 | 公開URL/サイト構成 | インフラ | データ/生成 | QA/公開 | 計測 | 判断 |
|---|---|---|---|---|---|---|---|
| Phase 0: Production-Ready Thin Slice | URLで読める最小本番品質を作る | Cloudflare Pagesの1 URL配下に `/anime`, `/ai`, `/life` を置く | Cloudflare Pages + GitHub Actions + Astro | SQLite + Markdown + RSS収集 + テンプレ生成 | low-riskのみ公開、medium/highはdraft | 手動URL確認、最低限sitemap/rss | 「公開までの機械」が動くか |
| Phase 1: 探索運用 | 当たるテーマ/記事型を探る | 1 URL配下のまま、3カテゴリ + 小テーマタグを増やす | GitHub Actions cron、失敗時通知 | 収集元を増やす。各カテゴリ内に複数サブテーマを持つ | low-risk自動公開、人間レビューを継続 | GSC/GA4導入、CTR/表示回数を見る | どの小テーマが伸びるか |
| Phase 2: 勝ち筋集中 | 伸びたテーマに投入量を寄せる | 勝ちカテゴリを強化。必要ならサブディレクトリを深掘り | Cloudflare Pages/Vercel検討、build最適化 | DBページ、比較表、カレンダー、内部リンク自動化 | 記事タイプ別QA、古い記事の自動更新 | GSC API/GA4/クリック/収益CSV | 継続するテーマ、撤退するテーマを決める |
| Phase 3: 分離/本番化 | 収益化できるテーマを独立資産にする | 独自ドメイン、またはサイト別ドメイン/サブドメイン | CDN、DB、queue、preview、rollback | Postgres/Supabase/D1、管理画面、記事API | 承認UI、監査ログ、権利管理 | 順位、CV、ASP、Adsense、ABテスト | 本格投資するサイトを決める |
| Phase 4: スケール運用 | 複数サイトを継続更新する | サイト別ブランド、メディアポートフォリオ | 監視、バックアップ、障害通知、権限分離 | embeddings重複排除、RAG、価格/在庫/API差分監視 | policy engine、専門家レビュー導線 | LTV、収益性、更新ROI | 横展開/売却/撤退を判断 |

### フェーズごとの優先順位

| フェーズ | 優先するもの | 捨てるもの |
|---|---|---|
| Phase 0 | URL公開、再現deploy、安全な下書き/公開分離、低コスト | 完璧なCMS、複雑なDB、SNS完全自動化、GSC自動分析 |
| Phase 1 | どのテーマが伸びるかの検証、記事型の勝ち負け、収集元の品質 | 3サイトすべての過剰作り込み |
| Phase 2 | 伸びたテーマへの集中、内部リンク、DBページ、更新性 | 伸びないテーマの惰性運用 |
| Phase 3 | 独自ドメイン、収益導線、承認フロー、計測自動化 | 1 repo/1 Pagesにこだわること |
| Phase 4 | 複数サイト運用の標準化、監視、利益率、撤退基準 | 無審査の大量自動公開、属人的手作業 |

### 当たるテーマを掘るには3サイトで足りるか

結論: 「3サイト」だけで当たりテーマを探す、というより、最初は「1つの公開基盤 + 3カテゴリ + 各カテゴリ内の複数サブテーマ」で探索するのがよい。3サイトは運営単位としては十分だが、探索単位としては少ない。

| 見方 | 3サイトで足りるか | 理由 | 推奨 |
|---|---|---|---|
| 運営リソース | 足りる | 最初から5〜10サイトを持つと品質/監視/レビューが散る | 3カテゴリで開始 |
| テーマ探索 | 足りない | 3本だけだと、外した時に学習量が少ない | 各カテゴリ内に5〜10個のサブテーマを持つ |
| SEO検証 | やや足りない | インデックス/CTRはクエリ単位で差が出る | 記事型を複数試す |
| 収益検証 | やや足りない | PVがあってもCVしないテーマがある | EC/SaaS/広告/ASPで分けて測る |
| 運用検証 | 足りる | 収集、生成、QA、deployの負荷を見るには3カテゴリで十分 | まず1基盤で運用 |

### 推奨する探索設計

3サイトをいきなり完全分離せず、最初は以下のように「3カテゴリ × サブテーマ」で掘る。

| 親カテゴリ | サブテーマ例 | 狙い |
|---|---|---|
| アニメ・ゲーム・推し活 | グッズ予約、店舗別特典、配信開始、イベント/ライブ、コラボカフェ、ゲーム更新、ガチャ、声優イベント | 短期トレンド、EC/VOD/チケット収益 |
| 生成AI | 公式更新、料金差分、モデル比較、業務テンプレ、API変更、障害情報、AIエージェント、画像/動画生成 | 中期の高単価SaaS/教材/法人リード |
| 生活防衛 | 値上げ一覧、セール日程、ポイント還元、ふるさと納税、税制変更、公共料金、通信費、家計アプリ | 行動意図が強い検索とASP/EC収益 |

初期の記事本数は「3サイト × 3本 = 9本」では少なすぎる。URL公開MVPの最低条件としては9本でよいが、当たりテーマ探索には以下を目標にする。

| 期間 | 目標本数 | 目的 |
|---|---:|---|
| URL公開MVP | 9本 | サイト/生成/QA/deployが動くことを確認 |
| 探索30日 | 60〜120本 | GSCで表示回数/CTR/クエリを比較できる量にする |
| 探索90日 | 200〜400本 | 勝ちサブテーマ、収益導線、撤退テーマを判断 |

### 探索時の判断基準

| 指標 | 見るもの | 判断 |
|---|---|---|
| GSC表示回数 | どのサブテーマが表示されるか | 表示が出るテーマは継続候補 |
| CTR | タイトル/検索意図が合っているか | 表示はあるがCTRが低いならタイトル改善 |
| 掲載順位 | ロングテールで10位以内に入るか | 入る型を量産候補にする |
| 更新頻度 | ネタが継続的に出るか | ネタ切れテーマはDBページ化か撤退 |
| 自動化率 | 下書きから公開まで何分か | 人間確認が重いテーマは後回し |
| リスク率 | medium/high判定が多いか | 高リスクテーマは自動公開対象から外す |
| 収益クリック | EC/SaaS/ASPにクリックが出るか | PVだけのテーマと収益テーマを分ける |


### MVP後にやること

- Search Console登録
- GA4導入
- 独自ドメイン設定
- Cloudflare Pagesへの移行検討
- WordPress/Headless CMS化の検討
- SNS投稿自動化
- アフィリエイトリンク管理
- 監視ソースを各サイト30件以上に増やす

## 成功条件

単なるまとめではなく、「更新されるDB」を作ること。

- アニメ/ゲーム: 発売日、予約、特典、配信、イベントのDB
- AI: 料金、機能、API、使い方、比較のDB
- 生活防衛: 値上げ、セール、ポイント、期限、公式リンクのDB

この形にすれば、自動化しやすく、Googleスパムポリシー上も「独自価値のない転載」から距離を取れる。
