from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def Index():
    a = 1
    b = 2
    
    return render_template('index.html', a=a, b=b)

if __name__ == '__main__':
    app.run(debug=True)