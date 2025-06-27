from flask import Flask
import scrape

app = Flask(__name__)


@app.route('/')
def is_open():
    return scrape.scrape()


if __name__ == '__main__':
    app.run(debug=True)

