import requests as rq
from bs4 import BeautifulSoup as bs
import re 


class TwitchExtractor():
    def __init__(self): 
        self.pattern = r'"alternateName":"([a-zA-Z0-9]+)"'

    def create_url(self, url):
        try:
            res = rq.get(url)
            soup = bs(res.content, "html.parser")
            match = re.search(self.pattern, soup.prettify())
            if match:
                username = match.group(1)
                url_part = url.split("/")[-1]
                new_url = "https://www.twitch.tv/{0}/clip/{1}".format(username, url_part)
                return new_url
            return "An error occurred. Please try again in a few seconds or check the URL"
        except Exception as e:
            return "Please check the URL and try again in a few seconds"


