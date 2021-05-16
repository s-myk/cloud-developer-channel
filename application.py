from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Wordl!'


@app.route('/profile/<string:user_name>')
def profile(user_name):
    return f'{user_name}さんのプロフィール画面です'


if __name__ == '__main__':
    app.run()
