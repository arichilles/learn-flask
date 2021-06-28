from os import name
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    list = [
        ('/', 'Home'),
        ('/produk', 'Produk dan Layanan'),
        ('/testimoni', 'Testimoni'),
        ('/kontak', 'Kontak')
    ]
    
    return render_template('index.html', list= list)

if __name__ == '__main__':
    app.run(debug=True)