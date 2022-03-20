from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd

def get_news(query, page_num):

    news_df = pd.DataFrame(columns=("Title", "Link", "Press", "Datetime", "Article"))
    idx = 0

    url_query = quote(query) ## utf-8 인코딩 쿼티를 통해서
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + url_query

    for _ in range(0, page_num):
        search_url = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(search_url, 'html.parser')
        links = soup.find_all('div', {'class': 'info_group'})

        for link in links:
            press = link.find('a', {'class':'info press'}).get_text()
            news_url = link.find('a').get('href')

            if (news_url == '#'):

                continue
            else:
                news_link = urllib.request.urlopen(news_url).read()
                news_html = BeautifulSoup(news_link, 'html.parser')

                title = news_html.find('h3', {"class": "tts_head"}).get_text()
                datetime = news_html.find('span', {'class': 't11'}).get_text()
                article = news_html.find('div', {'id': 'articleBody'}).get_text()


                news_df.loc[idx] = [title, news_url, press, datetime, article]
                idx += 1
                print("#", end="")
        try:
            next = soup.find('a', {'class':'btn_next'}).get('href')
            url = "https://search.naver.com/search.naver" + next
        except:
            break

    return news_df


query = input("질문검색: ")
news_df = get_news(query, 5)
print('Done')
print(news_df)
