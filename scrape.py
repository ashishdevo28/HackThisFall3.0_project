from bs4 import BeautifulSoup
import requests

news_items = []

for i in range(1, 11):
    data = requests.get(f"https://cryptonews.net/?page={i}").text
    soup = BeautifulSoup(data, "html.parser")
    news_items.extend(map(lambda a: a[1], filter(lambda classes: "news-item" in classes[0], map(lambda tag: [tag.get('class', ""), tag.get('data-title')], soup.body.main.find_all("div")))))

print("\n".join(news_items))

while True:
    pass
