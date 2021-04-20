from flask import Flask, render_template, request, redirect
from models import Produk

app = Flask(__name__)

@app.route('/')
def index():
    import sqlite3, os
    databaseName = os.getcwd() + '\\model4\\database.db'
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    container = []
    for kode,nama,harga in cursor.execute("select * from produk"):
        model = Produk(kode,nama,harga)
        container.append(model)
    cursor.close()
    conn.close()
    return render_template('index.html', container=container)

@app.route('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        kode = int(request.form['kode'])
        nama = request.form['nama']
        harga = float(request.form['harga'])
        model = Produk(kode,nama,harga)
        model.tambah()
        return redirect('http://127.0.0.1:5000')
    else:
        return render_template('tambah_form.html')

@app.route('/ubah/<int:id>', methods=['GET','POST'])
def ubah(id):
    model = Produk()
    model.load(id)
    if request.method == 'POST':
        kode = int(request.form['kode'])
        nama = request.form['nama']
        harga = float(request.form['harga'])
        model.setKode(kode)
        model.setNama(nama)
        model.setHarga(harga)
        model.ubah()
        return redirect('http://127.0.0.1:5000')
    else:
        return render_template('ubah_form.html', model=model)
    
@app.route('/hapus/<int:id>')
def hapus(id):
    model = Produk()
    model.load(id)
    model.hapus()
    return redirect('http://127.0.0.1:5000')

if __name__ == "__main__":
    app.run(debug=True)
        