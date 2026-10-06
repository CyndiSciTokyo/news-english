#!/usr/bin/env python3
"""给 lessons/*.json 里所有要朗读的英文生成录音，存到 audio/ 下。

用法:  python3 make_audio.py          只补缺的
       python3 make_audio.py --force  全部重录
文件名是文本的 FNV-1a 哈希，和 page.html 里的 akey() 一致。
需要 edge-tts：pip install edge-tts
"""
import asyncio, json, pathlib, sys
import edge_tts

H = pathlib.Path(__file__).resolve().parent
OUT = H / 'audio'
VOICE = 'en-US-AriaNeural'
RATE = {'s': '-5%', 'w': '-15%'}   # s = 句子, w = 单词


def akey(t):
    x = 2166136261
    b = t.encode('utf-16-le')
    for i in range(0, len(b), 2):
        x = ((x ^ (b[i] | b[i + 1] << 8)) * 16777619) & 0xffffffff
    return '%08x' % x


def collect():
    items, seen = [], set()

    def add(t, kind='s'):
        t = (t or '').strip()
        if t and t not in seen:
            seen.add(t)
            items.append((t, kind))

    for f in sorted(OUT.parent.glob('lessons/*.json')):
        if f.name == 'manifest.json':
            continue
        d = json.loads(f.read_text(encoding='utf-8'))
        for b in d.get('briefs', []):
            add(b['en'])
        for s in d.get('deep', {}).get('sentences', []):
            add(s['en'])
        for v in d.get('vocab', []):
            add(v['w'], 'w')
            add(v['ex'])
        for p in d.get('patterns', []):
            for r in p.get('rows', []):
                add(r[2])
            add(p.get('drill', {}).get('a'))
        for q in d.get('quiz', []):
            if q.get('t') == 'tr' and isinstance(q.get('a'), str):
                add(q['a'])
    return items


async def main():
    force = '--force' in sys.argv
    OUT.mkdir(exist_ok=True)
    items = collect()
    keep, made = set(), 0
    for text, kind in items:
        path = OUT / (akey(text) + '.mp3')
        keep.add(path.name)
        if path.exists() and not force:
            continue
        await edge_tts.Communicate(text, VOICE, rate=RATE[kind]).save(str(path))
        made += 1
        print('+', path.name, text[:58])
    for old in OUT.glob('*.mp3'):
        if old.name not in keep:
            old.unlink()
            print('-', old.name)
    print(len(items), '条文本，新录', made, '条，audio/ 下共', len(list(OUT.glob('*.mp3'))), '个文件')


asyncio.run(main())
