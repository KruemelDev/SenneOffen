from datetime import datetime
from flask import Flask, jsonify, request, redirect
import scrape
from scrape import SenneInfo

app = Flask(__name__)


# dateformat: dd-mmm-yy -> 01-Jun-25


@app.route('/json', methods=['GET'])
def is_open_json():
    date = request.args.get('date')
    senne_info: SenneInfo
    date: str
    if date == "" or not check_valid_date(date):
        return redirect(f"/json?date={datetime.today().strftime('%d-%b-%y')}")
    else:
        senne_info = scrape.scrape(date)

    return jsonify({"message": senne_info.message, "isOpen": senne_info.is_open, "date": senne_info.date})


@app.route('/', methods=['GET'])
def is_open():
    date = request.args.get('date')
    if date == "" or not check_valid_date(date):
        return redirect(f"/?date={datetime.today().strftime('%d-%b-%y')}")
    return scrape.scrape(date).message


def check_valid_date(date) -> bool:
    if not date:
        return False
    try:
        datetime.strptime(date, '%d-%b-%y')
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    app.run(debug=True)
