import sqlite3, os

DATABASE = os.getcwd() + '\\model4\\database.db'

class Produk:
    def __init__(self, kode=0, nama='', harga=0):
        self.kode = kode
        self.nama = nama
        self.harga = harga
    
    def setKode(self, kode):
        self.kode = kode
    
    def setNama(self, nama):
        self.nama = nama
        
    def setHarga(self, harga):
        self.harga = harga
        
    def tambah(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produk VALUES(?,?,?)", (self.kode, self.nama, self.harga))
        conn.commit()
        cursor.close()
        conn.close()
        
    def ubah(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("update produk set nama=?, harga=? where kode=?", (self.nama, self.harga, self.kode))
        conn.commit()
        cursor.close()
        conn.close()
    
    def hapus(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("delete from produk where kode=?", (self.kode,))
        conn.commit()
        cursor.close()
        conn.close()
        
    def load(self, id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        for kode,nama,harga in cursor.execute("select * from produk"):
            if kode == id:
                self.kode = kode
                self.nama = nama
                self.harga = harga
        cursor.close()
        conn.close()