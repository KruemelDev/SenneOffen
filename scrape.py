import requests
from bs4 import BeautifulSoup


def scrape() -> str:
    response = requests.get('https://bfgnet.de/sennelager-range-access')
    soup = BeautifulSoup(response.content, 'html.parser')
    newest_table_row = soup.find_all('tr')[1]
    open_text: str = ''
    if newest_table_row:
        open_text = newest_table_row.text.split('\n')[3]
    return open_text

