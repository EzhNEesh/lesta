import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import re


class TableParser:
    @staticmethod
    def get_table() -> list:
        wiki_url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
        wiki_page = requests.get(wiki_url)
        wiki_bs = BeautifulSoup(wiki_page.text, 'html.parser')
        table_html = wiki_bs.find_all('tr')

        table = []
        for row in table_html[1:]:
            row_data = row.text.split('\n\n')
            if len(row_data) != 6:
                break

            row_data[0] = row_data[0].lstrip('\n')
            row_data[-1] = row_data[-1].rstrip('\n')

            row_data[1] = int(re.search(r'\d+(?:\.\d\d\d|,\d\d\d)*', row_data[1])[0]
                              .replace('.', '')
                              .replace(',', ''))
            table.append(row_data)

        return table


@dataclass
class DataTable:
    table: list
