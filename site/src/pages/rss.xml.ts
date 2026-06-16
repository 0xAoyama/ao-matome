import rss from '@astrojs/rss';
import { getPosts } from '../lib/posts';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const posts = getPosts();
  return rss({
    title: 'matrix-ao',
    description: 'アニメの配信・グッズ予約・特典比較を公式情報だけでまとめる推し活ナビ',
    site: context.site!.toString(),
    items: posts.map(p => ({
      title: p.meta.title,
      description: p.meta.summary,
      link: `/news/${p.slug}/`,
      pubDate: new Date(p.meta.published_at),
    })),
  });
}
