#プロンプト組み立て用

from pathlib import Path
from datetime import datetime

PROMPT_PATH = Path("prompts/x_post_prompt.txt")


def build_prompt() -> str:
    # プロンプトを読む
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = f.read()

    # 今日の日付・曜日
    today = datetime.now()

    date_str = today.strftime("%Y-%m-%d")

    weekdays = [
        "月曜日",
        "火曜日",
        "水曜日",
        "木曜日",
        "金曜日",
        "土曜日",
        "日曜日",
    ]

    weekday = weekdays[today.weekday()]

    # Claudeへ送る完成版プロンプト
    return f"""
今日は{date_str}（{weekday}）です。

{prompt}
"""