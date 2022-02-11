# 재활용
import requests
from bs4 import BeautifulSoup
import os
import time


class Crawl:
    def __init__(self):
        pass

    def request(self, url):
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'gall.dcinside.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        try:
            url_get = requests.get(url, headers=header)
        except:
            url_get = requests.get(url, headers=header)
        return url_get

    def get_tags(self, first, last):

        posts = list()

        for page in range(first, last+1):
            req = self.request(
                "https://gall.dcinside.com/board/lists/?id=taeyeon_new1&page=%d" % page)
            soup = BeautifulSoup(req.text, "html.parser")
            posts.append(soup.find_all('tr', {'class': 'ub-content us-post'}))

            print(page, "페이지 완료")
            time.sleep(1.5)

        return posts

    def write(self, url, posts: list, tag):

        title = list()
        num = list()
        nick = list()

        for i in range(len(posts)):
            for j in range(len(posts[i])):
                title.append(posts[i][j].find('a'))
                num.append(posts[i][j].find_all('td', {'class': 'gall_num'}))
                nick.append(posts[i][j].find_all(
                    'td', {'class': 'gall_writer ub-writer'}))

        f = open("%s" % url, 'w', encoding='utf-8')
        f.write("글번호\t제목\t작성자\tURL\n")

        for k in range(len(title)):
            t = title[k].text.strip()
            n = num[k][0].text.strip()

            if (tag in t) and ("공지" not in n):
                string = "%s\t%s\t%s\t%s\n" % (n, t, nick[k][0].text.strip(
                ), "https://gall.dcinside.com"+title[k].get('href'))
                f.write(string)
        f.close()

    def run(self, fpage: int, lpage: int, url, tag):
        posts = self.get_tags(fpage, lpage)
        self.write(url, posts, tag)
