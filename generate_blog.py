import datetime

title = "今日の気になったこと"

content = f"""
# {title}

投稿日: {datetime.date.today()}

今日はネットで気になったことをゆるく考察します。

このブログでは、主が日常やネットで気になったことを
自由に調べたり考えたりしてまとめていきます。
"""

with open("index.md","w") as f:
    f.write(content)
