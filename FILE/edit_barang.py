
# IMPORT
import time as t

# MODUL
from database.database import connection

conn =connection()
cursor = conn.cursor()

klr = 0.5


def edit():
    cursor.execute("SELECT * FROM barang")
    isi = cursor.fetchone()
    if isi is None:
        print("\nEMPTY SET")
        t.sleep(2)
        print("\nMOHON MEMASUKAN BARANG TERLEBIH DAHULU\n")
        t.sleep(2)
        return
    else:
        while True:
            print("\n+" + "="*50 + "+")   
            print("|" +f"{"EDIT BARANG".center(50)}"+"|")
            print("+" + "="*50 + "+")   
            print("|"+" "*2+"NO"+" "*2 +"|"+"OPSI MENU EDIT".center(43)+"|")
            print("+" + "="*50 + "+")   
            print("|"+" "*2+"1 "+" "*2 +"|"+"Edit Nama".center(43)+"|")
            print("|"+" "*2+"2 "+" "*2 +"|"+"Edit Harga".center(43)+"|")
            print("|"+" "*2+"3 "+" "*2 +"|"+"Edit Stock".center(43)+"|")
            print("|"+" "*2+"4 "+" "*2 +"|"+"Edit Semua".center(43)+"|")
            print("|"+" "*2+"5 "+" "*2 +"|"+"Keluar".center(43)+"|")
            print("+" + "="*50 + "+")  
            opsi = input("Masukan Pilihan : ").strip()
            print("Loading...\n")
            t.sleep(3)
            if opsi == "1":
                editNama()
            elif opsi == "2":
                editHarga()
            elif opsi == "3":
                stock()
            elif opsi == "4":
                editSemua()
            elif opsi == "5":
                return
            else:
                print("Invalid Option")



def editNama():
    print("\n+" + "="*50 + "+")   
    print("|" +f"{"EDIT NAMA BARANG".center(50)}"+"|")
    print("+" + "="*50 + "+")  
    print("") 
    print("\nKetik 'stop' untuk keluar dari program\n")
    while True:    
        cursor.execute("SELECT * FROM BARANG")
        y = cursor.fetchall()
        for id,nama,harga,stock in y:
            print(f"id : {id:<5} | nama : {nama:<10} | harga : {harga:<10} | stock : {stock:<5}".upper())
        editid = input("\nMasukan ID barang yang ingin diubah : ").strip()
        if editid.lower() == "stop":
            print("\nKeluar...\n", end="\r")
            t.sleep(klr)
            return
        print("Mengecek...\n")
        t.sleep(3)
        cursor.execute("SELECT * FROM BARANG WHERE LOWER(ID) = LOWER(?)",(editid,))
        cek = cursor.fetchone()
        if cek is None:
            print(f"\nID : {editid} tidak ditemukan\n")
            t.sleep(1.5)
        elif not editid.strip():
            print("Tidak boleh kosong")
        else:
            while True:    
                print(f"\nData lama -> ID : {cek[0]} | NAMA : {cek[1]}")
                nama_baru = input("\nMasukan nama baru : ").strip()
                if nama_baru.lower() == "stop":
                    print("\nKeluar...\n", end="\r")
                    t.sleep(klr)
                    return
                cursor.execute("SELECT nama FROM barang WHERE nama = LOWER(?)",(nama_baru,))
                cek_nama = cursor.fetchone()
                print("Mengecek...\n")
                t.sleep(3)
                if not nama_baru.strip():
                    print("Nama tidak boleh kosong")
                elif cek_nama:
                    print("Nama sudah ada")    
                else:
                    cursor.execute("UPDATE barang SET nama = LOWER(?) WHERE id = LOWER(?)",(nama_baru,editid,))
                    conn.commit()
                    print("\nMengubah\n")
                    t.sleep(3)
                    print(f"\nBarang dengan nama {cek[1]} Berhasil diubah menjadi {nama_baru}\n")
                    t.sleep(3)
                    return

def editHarga():
    print("\n+" + "="*50 + "+")   
    print("|" +f"{"EDIT HARGA BARANG".center(50)}"+"|")
    print("+" + "="*50 + "+")  
    print("") 
    print("\nKetik 'stop' untuk keluar dari program\n")
    while True:    
        cursor.execute("SELECT * FROM BARANG")
        y = cursor.fetchall()
        for id,nama,harga,stock in y:
            print(f"id : {id:<5} | nama : {nama:<10} | harga : {harga:<10} | stock : {stock:<5}".upper())
        editid = input("\nMasukan ID barang yang ingin diubah : ").strip()
        if editid.lower() == "stop":
            print("\nKeluar...\n", end="\r")
            t.sleep(klr)
            return
        print("Mengecek...\n", end="\r")
        t.sleep(3)
        cursor.execute("SELECT * FROM BARANG WHERE LOWER(ID) = LOWER(?)",(editid,))
        cek = cursor.fetchone()
        if cek is None:
            print(f"\nID : {editid} tidak ditemukan\n")
            t.sleep(1.5)
        elif not editid.strip():
            print("Tidak boleh kosong")
        else:
            print(f"\nData lama -> ID : {cek[0]} | NAMA : {cek[1]} | HARGA : {cek[2]}")
            while True:    
                try:
                    harga_baru = input("\nMasukan harga baru : ").strip()
                    if harga_baru.lower() == "stop":
                        print("\nKeluar...\n", end="\r")
                        t.sleep(klr)
                        return
                    cursor.execute("SELECT harga FROM barang WHERE harga = LOWER(?)",(harga_baru,))
                    cek_nama = cursor.fetchone()
                    print("Mengecek...\n", end="\r")
                    t.sleep(3)
                    hrga = int(harga_baru)
                    if not harga_baru.strip():
                        print("Harga tidak boleh kosong")
                    elif hrga < 0 : 
                        print("Harga tidak boleh negatif")
                    else:
                        cursor.execute("UPDATE barang SET harga = LOWER(?) WHERE id = LOWER(?)",(harga_baru,editid,))
                        conn.commit()
                        print("\nMengubah...\n", end="\r")
                        t.sleep(3)
                        print(f"\nBarang dengan Nama {cek[1].upper()} yang sebelumnya berharga {cek[2]} Berhasil diubah menjadi {harga_baru}\n")
                        t.sleep(3)
                        return
                except ValueError:
                    print("Masukan harga yang benar")
    



def editStock():
    print("\n+" + "="*50 + "+")   
    print("|" +f"{"EDIT STOCK BARANG".center(50)}"+"|")
    print("+" + "="*50 + "+")  
    print("") 
    print("\nKetik 'stop' untuk keluar dari program\n")
    while True:    
        cursor.execute("SELECT * FROM BARANG")
        y = cursor.fetchall()
        for id,nama,harga,stock in y:
            print(f"id : {id:<5} | nama : {nama:<10} | harga : {harga:<10} | stock : {stock:<5}".upper())
        editid = input("\nMasukan ID barang yang ingin diubah : ").strip()
        if editid.lower() == "stop":
            print("\nKeluar...\n", end="\r")
            t.sleep(klr)
            return
        print("Mengecek...\n", end="\r")
        t.sleep(3)
        cursor.execute("SELECT * FROM BARANG WHERE LOWER(ID) = LOWER(?)",(editid,))
        cek = cursor.fetchone()
        if cek is None:
            print(f"\nID : {editid} tidak ditemukan\n")
            t.sleep(1.5)
        elif not editid.strip():
            print("Tidak boleh kosong")
        else:
            print(f"\nData lama -> ID : {cek[0]} | NAMA : {cek[1]} | STOCK : {cek[3]}")
            while True:    
                try:
                    stock_baru = input("\nMasukan stock baru : ").strip()
                    if stock_baru.lower() == "stop":
                        print("\nKeluar...\n", end="\r")
                        t.sleep(klr)
                        return
                    cursor.execute("SELECT stock FROM barang WHERE stock = LOWER(?)",(stock_baru,))
                    cek_nama = cursor.fetchone()
                    print("Mengecek...\n", end="\r")
                    t.sleep(3)
                    stck = int(stock_baru)
                    if not stock_baru.strip():
                        print("Stock tidak boleh kosong")
                    elif stck < 0 : 
                        print("Stock tidak boleh negatif")
                    else:
                        cursor.execute("UPDATE barang SET stock = LOWER(?) WHERE id = LOWER(?)",(stock_baru,editid,))
                        conn.commit()
                        print("\nMengubah...\n", end="\r")
                        t.sleep(3)
                        print(f"\nBarang dengan Nama {cek[1].upper()} yang sebelumnya berstock {cek[3]} Berhasil diubah menjadi {stock_baru}\n")
                        t.sleep(3)
                        return
                except ValueError:
                    print("Masukan stock yang benar")
    



def editSemua():
    while True:    
        print("\n+" + "="*50 + "+")   
        print("|" +f"{"EDIT INFO BARANG".center(50)}"+"|")
        print("+" + "="*50 + "+")  
        print("") 
        print("\nKetik 'stop' untuk keluar dari program\n")
        cursor.execute("SELECT * FROM BARANG")
        y = cursor.fetchall()
        for id,nama,harga,stock in y:
            print(f"id : {id:<5} | nama : {nama:<10} | harga : {harga:<10} | stock : {stock:<5}".upper())
        tnyaID = input("\nMasukan ID barang yang ingin dirubah : ").strip()
        if tnyaID.lower() == "stop":
            print("Keluar...", end="\r")
            t.sleep(klr)       
            return
        print("Mencari...\n", end="\r")
        t.sleep(3)
        cursor.execute("SELECT nama, harga, stock FROM BARANG WHERE id =LOWER(?)",(tnyaID,))    
        cek = cursor.fetchone()
        if not tnyaID.strip():
            print("ID tidak boleh kosong\n")
        elif cek is None:
            print(f"Barang dengan ID {tnyaID} tidak ditemukan")
        else:
            print("Menemukan...\n", end="\r")
            t.sleep(1.5)
            print("Mengganti...\n", end="\r")
            t.sleep(1.5)
            while True:
                print(f"DATA LAMA -> NAMA : {cek[0]:<10} | HARGA : {cek[1]:<10} | STOCK : {cek[2]:<5}")
                nama_baru  = input(f"Masukkan Nama baru dari barang {cek[0]}       : ").strip()
                if nama_baru.lower() == "stop":
                    print("Keluar...\n", end="\r")
                    t.sleep(klr)
                    return
                print("Memeriksa...\n", end="\r")
                t.sleep(3)
                cursor.execute("SELECT nama FROM barang WHERE LOWER(nama) = LOWER(?)",(nama_baru,))
                cek_nama = cursor.fetchone()
                if cek_nama:
                    print("Nama sudah ada\n")
                elif not nama_baru.strip():
                    print("Nama tidak boleh kosong\n")
                else:
                    print("Mengganti...\n", end="\r")
                    t.sleep(3)
                    while True:  
                        try:  
                            harga_baru = input(f"Masukkan Harga baru dari yang semula {cek[1]} : ").strip()
                            if harga_baru.lower() == "stop":
                                print("Keluar...\n", end="\r")
                                t.sleep(klr)
                                return
                            print("Memeriksa...\n", end="\r")
                            t.sleep(3)
                            k_hrga = int(harga_baru)
                            if not harga_baru.strip():
                                print("Harga tidak boleh kosong\n")
                            elif k_hrga < 0:
                                print("Harga tidak boleh kurang dari 0 \n")
                            else:
                                print("Mengganti...\n", end="\r")
                                t.sleep(3)
                                while True:     
                                    try:  
                                        stock_baru = input(f"Masukkan Stock baru dari yang semula {cek[2]} : ").strip()
                                        if stock_baru.lower() == "stop":
                                            print("Keluar...\n", end="\r")
                                            t.sleep(klr)
                                            return
                                        
                                        print("Memeriksa...\n", end="\r")
                                        t.sleep(3)
                                        k_stock = int(stock_baru)
                                        if k_stock < 0:
                                            print("Stock tidak boleh kurang dari 0\n")
                                        elif stock_baru is not None and stock_baru !="":
                                            cursor.execute("UPDATE barang set nama = ?, harga = ?, stock = ? WHERE id = lower(?)",(nama_baru,harga_baru,stock_baru,tnyaID))    
                                            conn.commit()
                                            print("Memeriksa...\n", end="\r")
                                            t.sleep(1.5)
                                            print("Mengubah...\n", end="\r")
                                            t.sleep(3)
                                            print(f"Data dengan ID : {tnyaID} berhasil dirubah\n")
                                            t.sleep(3)
                                            return
                                        
                                    except ValueError:
                                        print("Masukkan Stock yang benar\n")    

                        except ValueError:
                            print("Masukkan Harga yang benar\n")    
                                    


def stock():
    while True:
        print("\n+" + "="*50 + "+")   
        print("|" +f"{"EDIT STOCK".center(50)}"+"|")
        print("+" + "="*50 + "+")   
        print("|"+" "*2+"NO"+" "*2 +"|"+"OPSI MENU EDIT STOCK".center(43)+"|")
        print("+" + "="*50 + "+")   
        print("|"+" "*2+"1 "+" "*2 +"|"+"Ganti Stock".center(43)+"|")
        print("|"+" "*2+"2 "+" "*2 +"|"+"Tambah Stock".center(43)+"|")
        print("|"+" "*2+"3 "+" "*2 +"|"+"Kurangi Stock".center(43)+"|")
        print("|"+" "*2+"4 "+" "*2 +"|"+"Keluar".center(43)+"|")
        print("+" + "="*50 + "+")  
        stck= input("Masukan pilihan : ").strip()
        print("Loading...", end="\r")
        t.sleep(1.5)
        if stck == "1":
            editStock()
        elif stck == "2":
            tmbh_stck()    
        elif stck == "3":
            krng_stck() 
        elif stck == "4":
            print("Keluar...", end="\r")
            t.sleep(klr)
            return 
        else:
            print("Invalid")      
                    


def tmbh_stck():
    while True:    
        print("+" + "="*50 + "+")   
        print("|"+"TAMBAH STOCK".center(50)+"|")
        print("+" + "="*50 + "+") 
        print("Ketik 'stop' untuk keluar dari program") 
        cursor.execute("SELECT * FROM BARANG")
        y = cursor.fetchall()
        for id,nama,harga,stock in y:
            print(f"id : {id:<5} | nama : {nama:<10} | harga : {harga:<10} | stock : {stock:<5}".upper())
        editid = input("\nMasukan ID/Nama barang yang ingin diubah : ").strip()
        if editid.lower() == "stop":
            print("\nKeluar...\n", end="\r")
            t.sleep(klr)
            return
        print("\nMemeriksa...", end="\r")
        t.sleep(1)
        cursor.execute("SELECT id,nama FROM BARANG WHERE LOWER(ID) = LOWER(?) OR LOWER(nama) = LOWER(?)",(editid,editid))
        cek = cursor.fetchone()
        if not editid.strip():
            print("ID tidak boleh kosong\n")
        elif cek is None:
            print(f"Barang dengan ID/Nama {editid} tidak ditemukan\n")
        else:
            print("Menemukan...", end="\r")
            t.sleep(1.5)
            cursor.execute("SELECT stock,nama FROM BARANG WHERE id = ? OR nama = LOWER(?)",(editid,editid))
            r = cursor.fetchone()
            if r:
                while True:
                    try:
                        tambah= input("\nIngin menambahkan berapa stock : ").strip()
                        if tambah.lower() == "stop" :
                            print("Keluar...\n", end="\r")
                            t.sleep(klr)
                            return
                        print("Memproses..\n", end="\r")
                        t.sleep(2)
                        intm = int(tambah)
                        if intm < 0:
                            print("Tidak bisa dijumlahkan dengan negatif\n")
                            t.sleep(2)
                        elif tambah is not None and tambah != '':
                            print(f"Menambah stock dari {r[1]}", end="\r")
                            t.sleep(1.5)
                            stck_lama = r[0]
                            stck_n = stck_lama + intm
                            cursor.execute("UPDATE barang SET stock = lower(?) WHERE id = ? OR NAMA = LOWER(?)",(stck_n,editid,editid))
                            conn.commit()
                            print("Stock berhasil ditambahkan", end="\r")
                            t.sleep(2)     
                            print(f"Stock yang semula {r[0]} sekarang menjadi {stck_n}\n")
                            t.sleep(2)     
                            return
                    except ValueError:
                        print("Stock harus berupa angka\n")    


def krng_stck():
    while True:    
        print("+" + "="*50 + "+")   
        print("|"+"KURANGI STOCK".center(50)+"|")
        print("+" + "="*50 + "+") 
        print("Ketik 'stop' untuk keluar dari program") 
        cursor.execute("SELECT * FROM BARANG")
        y = cursor.fetchall()
        for id,nama,harga,stock in y:
            print(f"id : {id:<5} | nama : {nama:<10} | harga : {harga:<10} | stock : {stock:<5}".upper())
        editid = input("\nMasukan ID/Nama barang yang ingin diubah : ").strip()
        if editid.lower() == "stop":
            print("\nKeluar...\n", end="\r")
            t.sleep(klr)
            return
        print("Memeriksa...")
        t.sleep(1)
        cursor.execute("SELECT id,nama FROM BARANG WHERE LOWER(ID) = LOWER(?) OR LOWER(nama) = LOWER(?)",(editid,editid))
        cek = cursor.fetchone()
        if not editid.strip():
            print("ID tidak boleh kosong\n")
        elif cek is None:
            print(f"Barang dengan ID/Nama {editid} tidak ditemukan\n")
        else:
            print("Menemukan...")
            t.sleep(.5)
            cursor.execute("SELECT stock FROM BARANG WHERE id = ? OR nama = LOWER(?)",(editid,editid))
            r = cursor.fetchone()
            if r:
                cekr = int(r[0])
                if cekr <= 0:
                    print("\nStock barang ini sedang kosong\n")
                    t.sleep(1.5)
                else:
                    t.sleep(1.5)

                    while True:
                        try:
                            kurang= input("\nIngin mengurangi berapa stock : ").strip()
                            if kurang.lower() == "stop" :
                                print("Keluar...\n", end="\r")
                                t.sleep(klr)
                                return
                            print("Memproses..\n", end="\r")
                            t.sleep(1.5)
                            intm = int(kurang)
                            if intm < 0:
                                print("Tidak bisa dijumlahkan dengan negatif\n")
                                t.sleep(2)
                            elif kurang is not None and kurang != '':
                                hasil = int(r[0])
                                h = hasil - intm
                                if intm >= hasil :
                                    print("\nTidak bisa mengurangi stock\n")
                                    t.sleep(1.5)
                                else:
                                    cursor.execute("UPDATE barang SET stock = stock - ? WHERE id = ? OR NAMA = LOWER(?)",(kurang,editid,editid))
                                    conn.commit()
                                    print("Stock berhasil dikurangi\n")
                                    t.sleep(2)     
                                    print(f"Stock yang semula {r[0]} sekarang menjadi {h}\n")
                                    t.sleep(2)     
                                    return
                        except ValueError:
                            print("Stock harus berupa angka\n")    

