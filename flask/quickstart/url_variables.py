from flask import Flask, escape, url_for, request

app = Flask(__name__)


@app.route('/user/<username>')
def show_username(username):
    return f'User is named {escape(username)}.'

@app.route('/posts/')
@app.route('/posts/<int:id>')
def show_posts(id=None):
    if id == None:
        return 'List with all posts'
    else:
        return f'Post of id number {id}.'

with app.test_request_context():
    print(url_for('show_username', username='Leo'))
    print(url_for('show_posts'))
    print(url_for('show_posts', id=3))
