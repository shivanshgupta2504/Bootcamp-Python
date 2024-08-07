from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # if html.parser doesn't work use lxml

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.a.string)
# print(soup.p.string)  # prints None
# print(soup.p.getText())

# Finding all instances of a tag
# all_anchor_tags = soup.find_all(name="a")  # search by name
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one("p a")
print(company_url)
