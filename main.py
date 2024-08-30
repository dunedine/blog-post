import feedparser, time, os

URL = "https://dunedine.tistory.com//rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)

# GitHub에 커밋 및 푸시
os.system('git add README.md')
os.system('git commit -m "Update latest blog posts: {0}"'.format(RSS_FEED['entries'][0]['link']))  # 첫 번째 포스트의 링크를 커밋 메시지에 포함
os.system('git push')
