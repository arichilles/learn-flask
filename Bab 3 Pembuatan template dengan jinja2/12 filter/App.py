from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def Index():
    # terdapat dua karakter spasi di belakang teks
    var = 'Belajar <strong>Python</strong> dan <em>Flask</em>  '
    
    return render_template('index.html', var= var)

if __name__ == "__main__":
    app.run(debug=True)