# 振り返りのファイルの各見出しに、本文が書かれているかを確かめる。
# 使い方: python .github/scripts/check_reflection.py checkpoints/01/reflection.md
import re
import sys
from pathlib import Path

PLACEHOLDER = "（ここに書く）"
MIN_CHARS = 10

path = Path(sys.argv[1])
if not path.exists():
    print(f"NG  {path} がありません。")
    sys.exit(1)

sections = re.split(r"^## ", path.read_text(encoding="utf-8"), flags=re.M)[1:]
failed = 0
for section in sections:
    title, _, body = section.partition("\n")
    body = body.strip()
    if PLACEHOLDER in body:
        print(f"NG  「{title}」に「{PLACEHOLDER}」が残っています。")
        failed += 1
    elif len(body) < MIN_CHARS:
        print(f"NG  「{title}」が短すぎます（{MIN_CHARS} 文字以上書いてください）。")
        failed += 1
    else:
        print(f"OK  「{title}」")

if failed:
    sys.exit(1)
