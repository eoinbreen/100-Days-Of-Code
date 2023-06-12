from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, 'html.parser')

all_stories = soup.select(selector='.titleline>a')
article_texts = []
article_links = []
for story in all_stories:
    text = story.getText()
    article_texts.append(text)
    link = story.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)


largest_upvotes = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvotes)
print(largest_index)
print("Most Upvoted : ")
print(article_texts[largest_index] + " - " + article_links[largest_index] + " at " + str(largest_upvotes) + " upvotes. ")

