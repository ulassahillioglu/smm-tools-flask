import requests as rq
from bs4 import BeautifulSoup as bs
import re


class YoutubeCounter():
    def __init__(self):
        self.pattern = r'"views":{"simpleText":"(\d+[.]?\d+ \w+)"}'

    def count_views(self, url):
        try:
            html_content = rq.get(url).text
            soup = bs(html_content, "html.parser")
            matches = re.findall(self.pattern, soup.prettify())
            if matches:
                return matches[0]
            return "An error occurred. Please try again in a few seconds or check the URL"

        except Exception as e:
            return f"Please check the URL and try again in a few seconds"