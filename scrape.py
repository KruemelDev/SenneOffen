import requests
from bs4 import BeautifulSoup


def scrape(date):
    response = requests.get('https://bfgnet.de/sennelager-range-access')
    if response.status_code != 200:
        return SenneInfo("Could not load information", False, date)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        newest_table_row = soup.find(string=date)
    except IndexError:
        return SenneInfo("error", False, date)

    open_text: str
    if newest_table_row:
        try:
            open_text = newest_table_row.parent.parent.find_all("td")[2].text
        except IndexError:
            return SenneInfo("error", False, date)
    else:
        return SenneInfo("error", False, date)

    senne_open: bool = True
    if 'Transit Roads Closed' in open_text:
        senne_open = False

    return SenneInfo(open_text, senne_open, date)


class SenneInfo:
    def __init__(self, message: str, is_open: bool, date: str):
        self.message = message
        self.is_open = is_open
        self.date = date
