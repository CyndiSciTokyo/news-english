#!/usr/bin/env python3
"""把 page.html 包成可以直接打开的 index.html。page.html 本身可以原样发布成 artifact。"""
import pathlib
H = pathlib.Path(__file__).resolve().parent
SKELETON = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,-apple-system,sans-serif;background:#fafafa}
img{max-width:100%}
[hidden]{display:none!important}
</style>
__HEAD__
</head>
<body>
__BODY__
</body>
</html>
"""
src = (H / 'page.html').read_text(encoding='utf-8')
cut = src.index('<div class="wrap">')
head, body = src[:cut].strip(), src[cut:].strip()
(H / 'index.html').write_text(SKELETON.replace('__HEAD__', head).replace('__BODY__', body), encoding='utf-8')
print('index.html', (H / 'index.html').stat().st_size, 'bytes')
