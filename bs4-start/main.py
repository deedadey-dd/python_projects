from bs4 import BeautifulSoup
import requests

#
# with open("website.html", encoding='utf-8') as file:
#     data = file.read()
#     # print(data)
#
# soup = BeautifulSoup(data, 'html.parser')
# print(soup.title)
# print(soup.title.string)
#
# # print(soup.prettify())
# # print(soup.h1)


response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

article_tag = soup.find_all(name='span', class_='titleline')
# article_title = article_tag.getText()
# article_link = article_tag.get('href')
# article_upvote = soup.find(name='span', class_='score').getText()
#
# print(article_title)
# print(article_link)
# print(article_upvote)

# THIS WILL DO THE SAME WORK AS THE LIST COMPREHENSION BELOW

# titles = []
# links = []
#
# for article in article_tag:
#     title = article.getText()
#     link = article.get('href')
#     titles.append(title)
#     links.append(link)

titles = [article.getText() for article in article_tag]
links = [article.get('href') for article in soup.find_all(rel='noreferrer')]

upvote_text = [upvote.getText() for upvote in soup.find_all(name='span', class_='score')]
upvotes = [int(vote.split()[0]) for vote in upvote_text]
# print(titles)
# print(links)
# print(upvotes)
#
# article_data = [(title, link, vote) for title in titles for link in links for vote in upvotes]
#
# print(article_data)
print(f'{titles}\n{len(titles)}')
print(f'{links}\n{len(links)}')
print(f'{upvotes}\n{len(upvotes)}')

high_voted_index = upvotes.index(max(upvotes))
print(high_voted_index)
print(f'The article with the highest upvotes is\n\nTitle: {titles[high_voted_index]}\nLink : {links[high_voted_index]}'
      f'\nVotes: {upvotes[high_voted_index]}')

