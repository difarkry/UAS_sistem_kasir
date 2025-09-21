
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
    if lihat is None:
        print("\nANDA BELUM MENGISI DATA\n")
        t.sleep(3)
        return
    elif lihat is not None:
        for id,nama,harga,stock in semua:
            print(f"ID : {id:<5}\tNAMA : {nama:<10}\tHARGA : {harga:<10}\t STOCK : {stock:<5}".upper())
        t.sleep(10)    