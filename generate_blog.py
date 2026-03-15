import datetime
import random

topics = [
"最近のネット文化について",
"SNSで起こる炎上の理由",
"アニメの評価が分かれる理由",
"逆張り意見が生まれる心理",
"ネットミームが広がる仕組み",
"ゲームコミュニティの文化",
"オタク文化の変化",
"ネット議論が荒れやすい理由",
"流行が急に終わる理由",
"ネットでバズるコンテンツの特徴"
]

topic = random.choice(topics)

content = f"""
# 今日の研究テーマ

投稿日: {datetime.date.today()}

テーマ：{topic}

今日はこのテーマについてゆるく考察してみる。

インターネットでは様々な文化や現象が生まれている。
なぜそのような現象が起きるのか、
背景や理由を自分なりに考えてまとめていく。

このブログでは、主が気になったことを
自由に研究していく。
"""

filename = f"post-{datetime.date.today()}.md"

with open(filename,"w") as f:
    f.write(content)
