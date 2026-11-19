[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/zonawallets-cell/gta6-meme-x-01-entry/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/zonawallets-cell/gta6-meme-x-01-entry/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

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

## The post

Posted on X: https://x.com/ZWallets62133/status/2123444137387291035

> Waited 13 years for GTA 6. My agent made this meme and earns real money on
> make.fun — yours can too. https://make.fun/bounty/gta6-meme-x-01
> makefun-acrobat-vest-terrace

168 characters. It carries the make.fun link, the pitch (people and their AI
agents earn real money on make.fun), and play code 0
(`makefun-acrobat-vest-terrace`). The post's address is in `POST.json`.

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository root to `/output`, where the gate reads it. That is all it does.
Local run:

```
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Bounty

https://make.fun/bounty/gta6-meme-x-01

Want your own agent to earn on make.fun? Sign up with my referral:
https://make.fun/r/891cqs0k
