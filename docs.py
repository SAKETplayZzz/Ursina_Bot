import datetime
import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
CHEAT_SHEET_URL = "https://www.ursinaengine.org/cheat_sheet_dark.html"
# Time before cached version will be updated (in seconds)
MAX_DATA_AGE = 1800
DEBUG = True if os.getenv("LOG_LEVEL") == "debug" else False


class CheatSheet():
    """ Use get_doc(keyword) for queries."""

    def __init__(self, local_html=None) -> None:
        self.last_update = datetime.datetime.now()
        self.__html = ""
        self.docs = dict()
        if local_html:
            with open(local_html) as file:
                self.__html = file.read()
        self.__fetch_from_url(CHEAT_SHEET_URL)
        self.__parse_html()

    def get_doc(self, keyword: str) -> dict:
        """ Retrieve a dictionary containing cheat sheet 
        information for a given keyword"""
        if self.check_data_expired():
            self.__fetch_from_url(CHEAT_SHEET_URL)
            self.__parse_html()

        res = self.docs.get(keyword)
        return res or {}

    def get_keys(self) -> list:
        return sorted(self.docs.keys())

    def __fetch_from_url(self, url: str) -> bool:
        debug_print(f"GET: {CHEAT_SHEET_URL}")
        response = requests.get(url)
        if response.ok:
            debug_print("response OK")
            self.last_update = datetime.datetime.now()
            self.__html = response.text
            return True
        else:
            print("Error: Invalid response from",
                  CHEAT_SHEET_URL,
                  "Using local version if available.")
            return False

    def check_data_expired(self) -> bool:
        time_delta = (datetime.datetime.now() - self.last_update).seconds
        debug_print(f"DEBUG: last data update {time_delta} seconds ago")
        if time_delta > MAX_DATA_AGE:
            return True
        else:
            return False

    def __parse_html(self) -> None:
        soup = BeautifulSoup(self.__html, "html5lib")
        content = soup.find("div", id="content").find_all(
            "div", recursive=False)

        for e in content:
            info = e.contents[1]
            search_string = e.div["id"].lower()
            example = None
            if info.find("div", class_="example"):
                example = info.find("div", class_="example").extract()

            regex = re.compile(r"(?:\n)([a-z_A-Z]+\(.*\))")
            params = info.find("params")
            methods = regex.findall(info.text)
            github_url = info.a
            res = {
                "label": e.div.text,
                "methods": methods,
            }
            if github_url:
                res["github_url"] = github_url["href"]
            if params:
                res["params"] = params.text
            if example:
                res["example"] = example.text

            self.__set_key(search_string, res)

    def __set_key(self, key: str, value: dict) -> None:
        self.docs[key] = value


def debug_print(text: str) -> None:
    if DEBUG:
        print(text)


if __name__ == "__main__":
    from pprint import PrettyPrinter
    pp = PrettyPrinter()
    cs = CheatSheet()
    # cs = CheatSheet(local_html="test_data/ursina_cheat_sheet.html")

    pp.pprint(cs.get_doc("animation"))
