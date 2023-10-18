import requests
from bs4 import BeautifulSoup
import pprint


all_page_links = []
all_page_subtexts = []


def scrap_hacker_news(num_of_pages=1):
    news = []
    hacker_news_url = 'https://news.ycombinator.com/news'

    for page in range(num_of_pages):
        url = hacker_news_url if page > 1 else f'{hacker_news_url}?p={page + 2}'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        all_page_links.extend(soup.select('.titleline > a'))
        all_page_subtexts.extend(soup.select('.subtext'))

    news.extend(create_custom_hn(all_page_links, all_page_subtexts))

    return news


def format_link(link):
    homepage = 'https://news.ycombinator.com/'
    if not link.startswith('https://'):
        return f'{homepage}{link}'
    return link


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtexts):
    hn = []
    for i, item in enumerate(links):

        title = links[i].getText()
        href = format_link(links[i].get('href', None))
        score = subtexts[i].select('.score')
        if len(score):
            points = int(score[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


articles = scrap_hacker_news(3)
pprint.pprint(f'Article Count: {len(articles)}')
pprint.pprint(articles)
