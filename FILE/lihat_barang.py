
# IMPORT
import time as t

# MODUL
from database.database import connection

conn = connection()
cursor = conn.cursor()


def lihat():
    cursor.execute("SELECT * FROM BARANG")
    lihat = cursor.fetchone()
    cursor.execute("SELECT * FROM BARANG")
    semua =  cursor.fetchall()
    cursor.execute("SELECT * FROM barang WHERE stock = 0")
    cek = cursor.fetchall()
    if lihat is None:
        print("\nANDA BELUM MENGISI DATA\n")
        t.sleep(3)
        return 
    elif lihat is not None:
        
        for id,nama,harga,stock in semua:
            print(f"ID : {id:<5}\tNAMA : {nama:<10}\tHARGA : {harga:<10}\t STOCK : {stock:<5}".upper())
        print("")    
        for nama in cek:    
            print(f"Peringatan Stock {nama[1]} sedang kosong")
        t.sleep(10)    