import feedparser

jma_news = feedparser.parse("http://www.jma-net.go.jp/rss/jma.rss")

print(jma_news['feed']['title'])

for article in jma_news['entries']:
    print(f'タイトル: {article.get("title")}')
    print(f'リンク: {article.get("link")}')
    print(f'日付: {article.get("published")}')
    print(f'概要: {article.get("summary")}')
    print()