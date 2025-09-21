
# IMPORT
import time as t

# MODUL
from database.database import connection

conn = connection()
cursor = conn.cursor()


def tambah():
    while True:
        print("\n+" + "="*50 + "+")   
        print("|" +f"{"TAMBAH BARANG".center(50)}"+"|")
        print("+" + "="*50 + "+")  
        print("\nKetik 'stop' untuk keluar dari program")
        print("") 
 
        nama_B = input("Masukan nama barang : ").strip()
        if nama_B.lower() == "stop":
            print("\nKeluar...\n", end="\r")
            t.sleep(3)
            return
        cursor.execute("SELECT nama FROM barang WHERE LOWER(nama) = LOWER(?)",(nama_B,))
        cek_nama = cursor.fetchone()
        print("Mengecek...\n")
        t.sleep(3)
        if cek_nama is not None and cek_nama != ():
            print(f"{nama_B} sudah ada")
        elif not nama_B.strip():
             print("Nama barang tidak boleh kosong")    
        else:
            print("Menambahkan...\n", end="\r")
            t.sleep(3)
            while True:
                id_b = input("Masukan ID barang : ").strip()
                if id_b.lower() == "stop":
                    print("\nKeluar...\n", end="\r")
                    t.sleep(3)
                    return
                cursor.execute("SELECT id FROM barang WHERE LOWER(id) = LOWER(?)",(id_b,))
                cek_id = cursor.fetchone()
                print("Mengecek...\n", end="\r")
                t.sleep(3)
                if cek_id is not None and cek_id != ():
                    print(f"{id_b} sudah ada")
                elif not id_b.strip():
                    print("ID barang tidak boleh kosong")       
                else:
                    print("Menambahkan...\n", end="\r")
                    t.sleep(3)
                    break          
            while True:
                try:
                    harga_b = input("Masukan harga barang  : ")
                    if harga_b.lower() == "stop":
                        print("\nKeluar...\n", end="\r")
                        t.sleep(3)
                        return
                    print("Mengecek...\n", end="\r")
                    t.sleep(3)
                    hrga = int(harga_b)
                    if hrga < 0:
                        print("Harga tidak boleh negatif")
                    elif harga_b is not None and harga_b !=():
                        print("Menambahkan...\n", end="\r")
                        t.sleep(3)
                        break
                except ValueError:
                    print("Masukan harga yang benar") 
            while True:
                try:
                    stck = input("Masukan jumlah stock : ")   
                    if stck.lower() == "stop":
                        print("\nKeluar...\n", end="\r")
                        t.sleep(3)
                        return
                    print("Menambahkan...\n", end="\r")
                    t.sleep(3)
                    stock = int(stck)
                    if stock < 0:
                        print("stock tidak boleh kurang dari 0")
                    elif stck is not None and stck !=():
                        cursor.execute("INSERT INTO barang (id,nama,harga,stock) VALUES (?,?,?,?)",(id_b,nama_B,hrga,stock))
                        conn.commit()
                        print("\nMemasukan data...\n", end="\r")
                        t.sleep(3)
                        print(f"Data baru dengan ID {id_b} | Nama : {nama_B} | Harga : {hrga} | dan Stock sebanyak : {stck}. Berhasil dimasukkan\n")
                        t.sleep(2)
                        return
                    
                        
                except ValueError:
                    print("Stock harus berupa angka")     


           