import fs from 'node:fs';
import path from 'node:path';

const dataBase = path.resolve(import.meta.dirname, '../../../data/public');

export interface VodService {
  id: string;
  name: string;
  monthly: string;
  trial: string;
  strength: string;
}

export interface StreamingWork {
  slug: string;
  title: string;
  season: string;
  checked_at: string;
  official_url: string;
  sample?: boolean;
  summary: string;
  availability: Record<string, string>;
}

export interface StreamingData {
  updated_at: string;
  note: string;
  services: VodService[];
  works: StreamingWork[];
}

export interface GoodsStore {
  id: string;
  name: string;
  price: string;
  bonus: string;
  url: string;
}

export interface GoodsItem {
  slug: string;
  title: string;
  franchise: string;
  maker: string;
  price: string;
  release_date: string;
  deadline: string;
  status: string;
  checked_at: string;
  official_url: string;
  sample?: boolean;
  summary: string;
  stores: GoodsStore[];
}

export interface GoodsData {
  updated_at: string;
  note: string;
  items: GoodsItem[];
}

function readJson<T>(name: string): T {
  return JSON.parse(fs.readFileSync(path.join(dataBase, name), 'utf-8')) as T;
}

export function getStreaming(): StreamingData {
  return readJson<StreamingData>('streaming.json');
}

export function getGoods(): GoodsData {
  const data = readJson<GoodsData>('goods.json');
  data.items.sort((a, b) => a.deadline.localeCompare(b.deadline));
  return data;
}
