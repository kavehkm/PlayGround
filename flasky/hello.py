from flask import Flask


# create instance from Flask
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Home</h1>'


@app.route('/welcome/<string:user>')
def welcome(user):
    return '<h1>Welcome {}</h1>'.format(user)


if __name__ == '__main__':
    app.run('localhost', 5000)
