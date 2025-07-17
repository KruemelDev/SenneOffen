from datetime import datetime

from bs4 import BeautifulSoup
from SenneInfo import SenneInfo
import re


def scrape(date):
    table_date: str
    with open('/opentimes/opentimes', 'r') as f:
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

    senne_open: bool = get_senne_open(open_text)
    return SenneInfo(open_text, senne_open, date)


# !Note!: Always the current time will be used to validate senne open for the specific date
def get_senne_open(message: str) -> bool:
    senne_open: bool = True
    time = datetime.now()
    current_time: str = str(time.hour) + str(time.minute)

    from_time: str
    until_time: str
    if 'from' in message and 'until' in message:
        split_message = message.split('from')[1].split(' ')

        try:
            date = split_message[2] + " " + split_message[3] + " " + split_message[4]
        except IndexError:
            date = ""
        if is_plausible_date(date):
            # date in the message
            try:
                from_time = split_message[1][:4]
                until_time = "2400"
            except IndexError:
                return False
        else:
            try:
                from_time = split_message[1][:4]
                until_time = split_message[6][:4]
            except IndexError:
                return False

        # Check if senne is closed at the specific time
        if in_time_frame(int(current_time), int(from_time), int(until_time)) and "Closed" in message:
            senne_open = False
    elif 'until' in message:
        split_message = message.split('until')[1].split(' ')
        try:
            from_time = "0000"
            until_time = split_message[1][:4]
        except IndexError:
            return False

        if in_time_frame(int(current_time), int(from_time), int(until_time)) and "Closed" in message:
            senne_open = False
    elif 'Transit Roads Closed' in message:
        senne_open = False
    return senne_open


def is_plausible_date(date_str):
    return bool(re.match(r"^[A-Z][a-z]{2} \d{2} [A-Z][a-z]{2}$", date_str))


def in_time_frame(current_time: int, from_time: int, until_time: int) -> bool:
    return from_time <= current_time <= until_time
