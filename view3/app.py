from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python')
def python():
    return redirect('https://www.python.org/')

@app.route('/ruby')
def ruby():
    return redirect('https://www.ruby-lang.org/id/')

if __name__ == "__main__":
    app.run(debug=True)