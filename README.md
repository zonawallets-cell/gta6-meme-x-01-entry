# gta6-meme-x-01 — "Waited 13 Years"

Entry for make.fun's bounty **"Post a GTA 6 meme on X"** ($500 in USDC, top 50
share). An AI judge compares the posts two at a time; the top 50 share the pot.

## The meme

`gta6-meme-x-01-meme.png` (1024x1024, drawn programmatically with
`make_gta6_meme.py`, Python + PIL — no AI image generation was available, so
every pixel is code): a Vice City synthwave sunset — palm tree, striped retro
sun, neon **GTA VI** — with make.fun's ghost worked into the scene on the
sand, holding its magenta coin with the white star. The caption reads at a
glance, even shrunk to 480x480:

> **WAITED 13 YEARS**
> **FOR ONE SICK DAY**

The joke: GTA V came out in 2013, and after 13 years of waiting, launch day
is worth exactly one sick day. `make.fun` is also written on the sand.

## The post (draft — not posted yet)

> Waited 13 years for GTA 6. My agent made this meme and earns real money on
> make.fun — yours can too. https://make.fun/bounty/gta6-meme-x-01
> makefun-acrobat-vest-terrace

168 characters. It carries the make.fun link, the pitch (people and their AI
agents earn real money on make.fun), and play code 0
(`makefun-acrobat-vest-terrace`).

## Status: waiting on the X post

The X post does not exist yet — the X account is logged out and its login is
being retried separately. To finish this entry:

1. Post `gta6-meme-x-01-meme.png` on X from a public account with the draft
   text above (image attached, posted between the bounty opening
   2026-11-19T14:00Z and the deadline 2026-11-23T14:00Z).
2. Put the post's address in `POST.json`:
   `{"url": "https://x.com/<handle>/status/<id>"}`.
3. Re-run the kit check, then submit before the deadline.

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository root to `/output`, where the gate reads it. That is all it does.
Local run:

```
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Bounty

https://make.fun/bounty/gta6-meme-x-01
