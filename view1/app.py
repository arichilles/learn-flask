from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    respon = render_template('header.html')
    respon += render_template('content.html')
    respon += render_template('footer.html')
    return respon

if __name__ == "__main__":
    app.run(debug=True)