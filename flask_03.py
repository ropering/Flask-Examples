from flask import Flask
from flask.templating import render_template
#동적인 페이지 내용 추가하기
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index_01.html')

@app.route('/about')
def about():
    return 'This is about page'

@app.route('/contact')
def contact():
    return 'This is contact page'

@app.route('/<username>')
def hello_user(username):
    return render_template('index.html', user=username)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')