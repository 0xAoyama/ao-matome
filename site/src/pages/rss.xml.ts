import rss from '@astrojs/rss';
import { getPosts } from '../lib/posts';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const posts = getPosts();
  return rss({
    title: 'matrix-ao',
    description: 'アニメ・AI・生活防衛のまとめサイト',
    site: context.site!.toString(),
    items: posts.map(p => ({
      title: p.meta.title,
      description: p.meta.summary,
      link: `/${p.category}/${p.slug}/`,
      pubDate: new Date(p.meta.published_at),
    })),
  });
}
