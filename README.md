# 每日新闻英语

每天一课,用当天的财经新闻练英文,重点在「同样的意思,英文里习惯怎么说」。

公开地址:https://cyndiscitokyo.github.io/news-english/

## 一课的结构

1. **今日五条** — 五句英文摘要,重点词标红,配中文
2. **精读一篇** — 约 150 词,逐句可点播放,附中译和值得抄下来的写法
3. **今日生词** — 12 个词,音标 / 中文 / 例句 / 记忆法,可以 ★ 收藏
4. **地道说法** — 当天最该学的三组搭配和句型,每组一道练习
5. **小测** — 五道题,选择和填空自动判对错

## 内容来源

英文全部是根据当天公开披露的事实原创改写的,不转载任何报道原文。数字、日期、公司名属于事实。

## 加一天新的课

```bash
# 1. 写 lessons/YYYY-MM-DD.json（结构照着已有的那天）
# 2. 把日期加进 lessons/manifest.json（最新的放最前面）
# 3. 补录音（只会生成缺的那些）
python3 make_audio.py
# 4. 重新生成 index.html
python3 build.py
# 5. 提交
git add -A && git commit -m "lesson: YYYY-MM-DD" && git push
```

## 文件

- `page.html` — 页面本体,改样式和逻辑改这里
- `build.py` — 给 page.html 套上 html 外壳,生成 `index.html`(不要手改 index.html)
- `make_audio.py` — 用 edge-tts 的微软神经语音生成录音,文件名是文本的哈希
- `lessons/` — 每天一个 json
- `audio/` — mp3,页面按哈希去找;找不到就退回浏览器自带的语音合成

学习记录(收藏的词、答题情况、深浅色)存在浏览器本地,换设备不同步。
