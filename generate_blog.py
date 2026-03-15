from openai import OpenAI
import datetime
import random

client = OpenAI()

date = datetime.date.today()

topics = [
"ネット文化",
"SNSの心理",
"アニメ文化",
"ネットミーム",
"炎上の仕組み",
"ゲーム文化",
"オタク文化",
"ネット議論"
]

topic = random.choice(topics)

response = client.responses.create(
    model="gpt-5",
    input=f"{topic}について800文字くらいのブログ記事を書いて"
)

article = response.output_text

image = f"https://picsum.photos/800/400?random={date}"

filename = f"post-{date}.md"

content = f"""
# {topic}

投稿日: {date}

![image]({image})

{article}
"""

with open(filename,"w") as f:
    f.write(content)

with open("index.md","a") as f:
    f.write(f"\n- [{topic}]({filename})")
