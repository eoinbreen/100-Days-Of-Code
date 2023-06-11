from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.p)

all_anchor_tags = soup.findAll(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))


headings = soup.findAll(name="h3", class_="heading")
# headings = soup.select(selector='.heading')

print(headings)

