from flask import Flask

app = Flask(__name__)


@app.route('/')
def alive():
    return 'I Am Alive'


if __name__ == "__main__":
    app.run()
