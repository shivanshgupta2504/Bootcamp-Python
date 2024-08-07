from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
# print(response.text)
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")

# Getting article headlines
articles = soup.select(selector=".titleline a")
articles_sitestr = soup.select(selector=".titleline .sitestr")
article_text = [article.getText() for article in articles]
article_text_sitestr = [article.getText() for article in articles_sitestr]
for x in article_text_sitestr:
    article_text.remove(x)


# Getting proper links
article_link = [article.get("href") for article in articles]


def proper_link(link):
    if "https://" in link:
        return True
    else:
        return False


article_link = filter(proper_link, article_link)
article_link = [link for link in article_link]

# Getting upvotes
article_upvote = [int(vote.getText().split(" ")[0]) for vote in soup.find_all(name="span", class_="score")]

max_upvote_idx = article_upvote.index(max(article_upvote))
# print(article_upvote)
# print(max_upvote_idx)
# print(article_upvote[max_upvote_idx])
#
# print(article_text)
# print(article_link)
# max_upvote_article_text = article_text[max_upvote_idx]
# print(max_upvote_article_text)
# max_upvote_article_link = article_link[max_upvote_idx]
# print(max_upvote_article_link)


