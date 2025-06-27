from flask import Flask, jsonify
import scrape

app = Flask(__name__)


@app.route('/json')
def is_open_json():
    return jsonify({"message": scrape.scrape()})
@app.route('/')
def is_open():
    return scrape.scrape()


if __name__ == '__main__':
    app.run(debug=True)

