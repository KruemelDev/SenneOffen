from flask import Flask, jsonify
import scrape

app = Flask(__name__)


@app.route('/json')
def is_open_json():
    message: str = scrape.scrape()
    senne_open: bool = True
    if 'Transit Roads Closed' in message:
        senne_open = False

    return jsonify({"message": message, "isOpen": senne_open})


@app.route('/')
def is_open():
    return scrape.scrape()


if __name__ == '__main__':
    app.run(debug=True)

