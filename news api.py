import requests
query=input("What type of news are you interested in today")
api = "733148c980d440ad8c44f15ef227d377"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-29&sortBy=publishedAt&apiKey={api}"


print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]

print(f"Total articles found: {len(articles)}")

for index,article in enumerate(articles):
    print(index + 1,article["title"],article["url"])
    print("\n******************\n")
    