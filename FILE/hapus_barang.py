
# IMPORT
import time as t

# MODUL
from database.database import connection



conn = connection()
cursor = conn.cursor()


def hapus():
    while True:   
        cursor.execute("SELECT * FROM BARANG")
        isi = cursor.fetchone()
        if isi is None:
            print("\nEMPTY SET\n")
            t.sleep(3)
            return
        else:
            t.sleep(2)
            print("\n+" + "="*50 + "+")   
            print("|" +f"{"HAPUS BARANG".center(50)}"+"|")
            print("+" + "="*50 + "+")   
            print("|"+" "*2+"NO"+" "*2 +"|"+"OPSI MENU HAPUS".center(43)+"|")
            print("+" + "="*50 + "+")   
            print("|"+" "*2+"1 "+" "*2 +"|"+"BERDASARKAN ID".center(43)+"|")
            print("|"+" "*2+"2 "+" "*2 +"|"+"BERDASARKAN NAMA".center(43)+"|")
            print("|"+" "*2+"3 "+" "*2 +"|"+"KELUAR".center(43)+"|")
            print("+" + "="*50 + "+")   
            pilih = input("Masukan pilihan : ")
            print("Loading...\n", end="\r")
            t.sleep(3)
            if pilih == "1":
                hapus_berdasarkan_id()
                cursor.execute("SELECT * FROM BARANG")
                isi = cursor.fetchone()
                if isi is None:
                    return
                
            elif pilih == "2":
                hapus_berdasarkan_nama()
                cursor.execute("SELECT * FROM BARANG")
                isi = cursor.fetchone()
                if isi is None:
                    return
                
            elif pilih == "3":
                return
            else :
                print("Invalid Choice")            


def hapus_berdasarkan_id():
    while True:    
        print("\n+" + "="*50 + "+")   
        print("|" +f"{"HAPUS BARANG DENGAN ID".center(50)}"+"|")
        print("+" + "="*50 + "+")  
        print("") 
        print("\nKetik 'stop' untuk keluar dari program")
        cursor.execute("SELECT * FROM BARANG")
        semua =  cursor.fetchall()
        for id,nama,harga,stock in semua:
            print(f"ID : {id:<5} | NAMA : {nama:<10} | HARGA : {harga:<10} | STOCK : {stock:<5}")  
        h_id = input("\nMasukan ID barang yang ingin dihapus : ")
        if h_id.lower() == 'stop':
            print("Keluar...\n", end="\r")
            t.sleep(3)
            return 
        print("Mencari...\n", end="\r")
        t.sleep(3)
        cursor.execute("SELECT nama,id FROM barang WHERE LOWER(id) = LOWER(?)",(h_id,))
        cek =  cursor.fetchone()
        if not h_id.strip():
            print("\nNama tidak boleh kosong\n")
            t.sleep(3)
        elif cek is None:
            print(f"\nBarang dengan ID : {h_id} tidak ada\n")
            t.sleep(3)
        else:
            while True:
                tanya = input(f"\nApakah anda ingin menghapus barang {cek[0]} : ")
                t.sleep(1.5)
                if tanya.lower() == "ya" or tanya.lower() == "yes":
                    print("\nMenghapus...\n", end="\r")
                    t.sleep(3)
                    cursor.execute("DELETE FROM barang WHERE LOWER(id) = LOWER(?)",(h_id,))  
                    conn.commit()
                    print(f"barang dengan ID {h_id} berhasil dihapus") 
                    t.sleep(3)
                    return False
                elif tanya.lower() == "tidak" or tanya.lower() == "no":
                    break
                else:
                    print("\nPilihannya hanya Ya/Tidak\n", end="\r")
                    t.sleep(3)
        
def hapus_berdasarkan_nama():
    while True:    
        print("\n+" + "="*50 + "+")   
        print("|" +f"{"HAPUS BARANG DENGAN NAMA".center(50)}"+"|")
        print("+" + "="*50 + "+")  
        print("") 
        print("\nKetik 'stop' untuk keluar dari program")
        cursor.execute("SELECT * FROM BARANG")
        semua =  cursor.fetchall()
        for id,nama,harga,stock in semua:
            print(f"ID : {id:<5} | NAMA : {nama:<10} | HARGA : {harga:<10} | STOCK : {stock:<5}")
        name = input("\nMasukan barang yang ingin dihapus : ")
        if name.lower() == 'stop':
            print("Keluar...\n", end="\r")
            t.sleep(3)
            return
        print("Mencari...", end="\r")
        t.sleep(3)
        cursor.execute("SELECT nama FROM barang WHERE LOWER(nama) = LOWER(?)",(name,))
        cek =  cursor.fetchone()
        if not name.strip():
            print("\nNama tidak boleh kosong\n")
            t.sleep(3)
        elif cek is None:
            print(f"\nBarang {name} tidak ada\n")
            t.sleep(3)

        else:
            while True:
                tanya = input(f"\nApakah anda ingin menghapus barang {cek[0]} : ")
                t.sleep(1.5)
                if tanya.lower() == "ya" or tanya.lower() == "yes":
                    print("\nMenghapus...\n", end="\r")
                    t.sleep(3)
                    cursor.execute("DELETE FROM barang WHERE LOWER(nama) = LOWER(?)",(name,))  
                    conn.commit()
                    print(f"{name} berhasil dihapus\n", end="\r") 
                    t.sleep(3)
                    return False
                elif tanya.lower() == "tidak" or tanya.lower() == "no":
                    break
                else:
                    print("\nPilihannya hanya Ya/Tidak\n", end="\r")
                    t.sleep(3)
                  
            
            

                  


