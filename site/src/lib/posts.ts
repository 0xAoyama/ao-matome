import fs from 'node:fs';
import path from 'node:path';

export interface PostMeta {
  title: string;
  summary: string;
  source_url: string;
  source_name: string;
  published_at: string;
  checked_at: string;
  risk_level: string;
  ymyl: boolean;
  copyright_risk: boolean;
  category: string;
  slug: string;
}

export interface Post {
  meta: PostMeta;
  content: string;
  category: string;
  slug: string;
}

function parseFrontmatter(raw: string): { meta: Record<string, any>; content: string } {
  const match = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { meta: {}, content: raw };
  const meta: Record<string, any> = {};
  for (const line of match[1].split('\n')) {
    const idx = line.indexOf(':');
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    let val: any = line.slice(idx + 1).trim().replace(/^"(.*)"$/, '$1');
    if (val === 'true') val = true;
    if (val === 'false') val = false;
    meta[key] = val;
  }
  return { meta, content: match[2] };
}

const contentBase = path.resolve(import.meta.dirname, '../../../content/sites');

export function getPosts(category = 'news'): Post[] {
  const posts: Post[] = [];
  const dir = path.join(contentBase, category, 'posts');
  if (!fs.existsSync(dir)) return posts;
  for (const file of fs.readdirSync(dir)) {
    if (!file.endsWith('.md')) continue;
    const raw = fs.readFileSync(path.join(dir, file), 'utf-8');
    const { meta, content } = parseFrontmatter(raw);
    posts.push({
      meta: meta as PostMeta,
      content,
      category,
      slug: meta.slug || file.replace(/\.md$/, ''),
    });
  }
  posts.sort((a, b) => b.meta.published_at.localeCompare(a.meta.published_at));
  return posts;
}

export function getPost(slug: string, category = 'news'): Post | undefined {
  return getPosts(category).find(p => p.slug === slug);
}
