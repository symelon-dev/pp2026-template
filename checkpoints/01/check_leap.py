# leap.py の is_leap_year が正しいかを確かめる。
# 実行方法: python checkpoints/01/check_leap.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from leap import is_leap_year

cases = [
    (2024, True),
    (2025, False),
    (2000, True),
    (1900, False),
    (2100, False),
    (2400, True),
]

failed = 0
for year, expected in cases:
    actual = is_leap_year(year)
    if actual == expected:
        print(f"OK  {year}: {actual}")
    else:
        print(f"NG  {year}: 期待する値は {expected} だが、{actual} が返された")
        failed += 1

if failed:
    print(f"\n{len(cases)} 件中 {failed} 件が NG です。")
    sys.exit(1)
print(f"\n{len(cases)} 件すべて OK です。")
