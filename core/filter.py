from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Filter:
    def __init__(self, response):
        self.response = response
        self._links = []

    def __len__(self):
        return len(self._links)

    def __getitem__(self, item):
        return self._links[item]

    def _check_url(self, url):
        parser_url = urlparse(url)
        return bool(parser_url.scheme)

    def _load_blacklist(self):
        with open('blacklist/links.txt') as links:
            lines = links.read().splitlines()

        return lines

    def remove_links(self, links):
        blacklist = self._load_blacklist()

        for block in blacklist:
            for link in list(links):
                if block in link:
                    links.remove(link)

        return links

    def filter_links(self):
        bs = BeautifulSoup(self.response.text, "lxml")
        links = bs.find_all("a")

        for link in links:
            if "href" in link.attrs:
                url = link.attrs["href"].replace('/url?q=', '')

                if (self._check_url(url)):
                    self._links.append(url)

        return self._links
