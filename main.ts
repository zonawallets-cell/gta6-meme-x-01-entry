// gta6-meme-x-01 entry — hand the X post's address to the house.
//
// The post itself is the entry: a GTA 6 meme posted on X from a public
// account. Nothing this program writes is judged; the house reads the post
// from X (its first picture and its text) and hands that to the judge.
// All this program does is move POST.json from the repository root into
// the output directory, where the gate reads it.
//
// The POST.json shipped here still holds the starter's placeholder address,
// so the gate refuses it as it stands (valid 0). Replace the placeholder
// with the posted meme's address before submitting:
//   {"url": "https://x.com/<handle>/status/<id>"}
//
// Node 22, standard library only. Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// and out/POST.json is then byte for byte this directory's POST.json.

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const postPath = join(BOT_DIR, 'POST.json');
const postBytes = readFileSync(postPath);

// Keep the file exactly as the repository holds it: the gate parses it.
mkdirSync(OUTPUT_DIR, { recursive: true });
writeFileSync(join(OUTPUT_DIR, 'POST.json'), postBytes);
console.log(`POST.json copied to ${OUTPUT_DIR}`);
