from bs4 import BeautifulSoup


def scrape(date):
    table_date: str
    with open('opentimes/opentimes', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        try:
            table_date = soup.find(string=date)
        except IndexError:
            return SenneInfo("error", False, date)

    open_text: str
    if table_date:
        try:
            open_text = table_date.parent.parent.find_all("td")[2].text
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
