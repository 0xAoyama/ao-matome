// アフィリエイトリンク管理
//
// ASP（A8.net / もしも / バリューコマース等）の承認が下りたら、該当IDの
// アフィリエイトURLをここに設定するだけで全ページのCTA・店舗リンクが差し替わる。
// null の間は公式サイトへフォールバックし、PR表記も自動で消える。

export const VOD_AFFILIATE_URLS: Record<string, string | null> = {
  danime: null, // 例: A8.net / afb の案件URL
  unext: null,
  dmmtv: null,
  primevideo: null,
  abema: null,
  netflix: null, // Netflixはアフィリエイトプログラムなし（常に公式リンク）
};

export const STORE_AFFILIATE_URLS: Record<string, string | null> = {
  rakuten: null, // 楽天アフィリエイト（審査なし・最初に設定する）
  amazon: null, // もしも経由Amazon（本家アソシエイトは実績が必要）
  animate: null,
  amiami: null,
  goodsmile: null,
  gamers: null,
  hobbystock: null,
};

export const SERVICE_OFFICIAL_URLS: Record<string, string> = {
  danime: 'https://animestore.docomo.ne.jp/',
  unext: 'https://video.unext.jp/',
  dmmtv: 'https://tv.dmm.com/vod/',
  primevideo: 'https://www.amazon.co.jp/gp/video/storefront',
  abema: 'https://abema.tv/',
  netflix: 'https://www.netflix.com/jp/',
};

export interface ResolvedLink {
  url: string;
  isAffiliate: boolean;
}

export function vodLink(serviceId: string): ResolvedLink {
  const aff = VOD_AFFILIATE_URLS[serviceId];
  if (aff) return { url: aff, isAffiliate: true };
  return { url: SERVICE_OFFICIAL_URLS[serviceId] ?? '#', isAffiliate: false };
}

export function storeLink(storeId: string, fallbackUrl: string): ResolvedLink {
  const aff = STORE_AFFILIATE_URLS[storeId];
  if (aff) return { url: aff, isAffiliate: true };
  return { url: fallbackUrl, isAffiliate: false };
}

/** サイト内にアフィリエイトリンクが1つでも有効か（フッターのPR文言切り替え用） */
export function hasAnyAffiliate(): boolean {
  return [...Object.values(VOD_AFFILIATE_URLS), ...Object.values(STORE_AFFILIATE_URLS)].some(Boolean);
}
