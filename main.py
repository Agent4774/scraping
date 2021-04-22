#! /usr/bin/env python3
from bs4 import BeautifulSoup
import requests


def get_articles():
    res = requests.get('https://news.ycombinator.com/')
    html_parser = BeautifulSoup(res.text, 'html.parser')
    main_element = html_parser.select('#hnmain tr')[3:]# getting table wrapper
    items_table = main_element[0].select('tr td table')# getting all table elements
    articles = items_table[0].select('tr .title .storylink')
    points = items_table[0].select('tr .subtext .score')
    article_hrefs = []
    
    for index, value in enumerate(articles[:len(articles)-1]):
        point_int = int(points[index].getText().split(' ')[0])
        if point_int > 100:# getting all articles with points greater than 100
            article_hrefs.append(articles[index].get('href'))
    return article_hrefs

if __name__ == '__main__':
   result = get_articles()
   print(result)
