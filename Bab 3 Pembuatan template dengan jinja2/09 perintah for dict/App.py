from os import name
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    dict = {
        '/': 'Home',
        '/produk': 'Produk dan Layanan',
        '/testimoni': 'Testimoni',
        '/kontak': 'Kontak'        
    }
    
    return render_template('index.html', dict= dict)

if __name__ == '__main__':
    app.run(debug=True)