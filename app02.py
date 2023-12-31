from flask import Flask

app = Flask(__name__)

@app.route('/')
def wwwRoot():
    return '<h1>Hello, World!</h1>'

@app.route('/apple')
def pageApple():
    return """
        <h1>
            Hello, 사과!
        </h2>
    """

@app.route('/<path:page>')
def page(page):
     return f"""
        <h1>
            Hello, {page}
        </h2>
    """

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)