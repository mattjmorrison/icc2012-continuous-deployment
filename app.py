from flask import Flask, Response

app = Flask(__name__)


@app.route('/<int:x>/')
def root(x):
    if x > 5:
        text = "Hi!"
    else:
        text = "Low :("
    return Response(text)


if __name__ == '__main__':
    app.run()
