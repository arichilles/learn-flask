from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    a = -4
    return render_template('index.html', a= a)

if __name__ == '__main__':
    app.run(debug=True)