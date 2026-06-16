import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://matrix-ao.pages.dev',
  integrations: [sitemap()],
  output: 'static',
  redirects: {
    '/anime': '/news',
    '/anime/[slug]': '/news/[slug]',
    '/ai': '/news',
    '/life': '/news',
  },
});
