
# IMPORT
import time as t 


# MODUL
from auth import login_admin, nama_admin
from tambah_barang import tambah
from hapus_barang import hapus
from lihat_barang import lihat
from edit_barang import edit
from kasir import kasir_interfaces
from database.database import connection,tutup_database

conn = connection()
cursor = conn.cursor()

jawaban = [True]

def awal():
    while True:    
        jawaban.clear()
        jawaban.append(True)
        print("+" + "="*50 + "+")   
        print("|" +f"{"SELAMAT DATANG".center(50)}"+"|")
        print("+" + "="*50 + "+")   
        print("|"+" "*2+"NO"+" "*2 +"|"+"OPSI MENU".center(43)+"|")
        print("+" + "="*50 + "+")   
        print("|"+" "*2+"1 "+" "*2 +"|"+"ADMIN".center(43)+"|")
        print("|"+" "*2+"2 "+" "*2 +"|"+"KASIR".center(43)+"|")
        print("|"+" "*2+"3 "+" "*2 +"|"+"KELUAR".center(43)+"|")
        print("+" + "="*50 + "+")   
        pilih = input("Masukan opsi (1/2/3) : ") 
        if pilih == "1":
            print("Loading..\n")
            t.sleep(1.5) 
            login = login_admin()
            if login:
                admin()
        elif pilih == "2":
            print("Loading..")
            t.sleep(3)
            while jawaban[0] == True:
                kasir_interfaces()
               
                while True:
                    ulang = input("Apakah Anda ingin transaksi lagi? (ya/tidak): ").strip().lower()
                    match ulang.lower():
                        case "ya":
                            break
                        case 'tidak':
                            jawaban.clear()
                            jawaban.append(False)
                            break
                        case _:
                            print('Wrong answer')
            

        
        elif pilih == "3":
            print("Keluar dari program...\n", end="\r")
            t.sleep(3)
            break
        else:
            print("Invalid Choice")

def admin():
    while True:
        print("+" + "="*50 + "+")   
        print("|" +f"{nama_admin().center(50)}"+"|")
        print("+" + "="*50 + "+")   
        print("|"+" "*2+"NO"+" "*2 +"|"+"OPSI MENU".center(43)+"|")
        print("+" + "="*50 + "+")   
        print("|"+" "*2+"1 "+" "*2 +"|"+"Lihat Barang".center(43)+"|")
        print("|"+" "*2+"2 "+" "*2 +"|"+"Tambah Barang".center(43)+"|")
        print("|"+" "*2+"3 "+" "*2 +"|"+"Hapus Barang".center(43)+"|")
        print("|"+" "*2+"4 "+" "*2 +"|"+"Edit Barang".center(43)+"|")
        print("|"+" "*2+"5 "+" "*2 +"|"+"Keluar".center(43)+"|")
        print("+" + "="*50 + "+")      
        pilihan = input("Masukan pilihan : ")
        if pilihan == "5":
            print("Keluar...", end="\r")
            t.sleep(3)
            break
        print("Loading...", end="\r")
        t.sleep(3)
        if pilihan == "1":
            print(" ")
            lihat_barang()
            print("\n"*2)
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            edit_barang()
        else:
            print("\nNot Found\n")
            t.sleep(3)
def tambah_barang():
    tambah()
def lihat_barang():
   lihat()
def hapus_barang():
    hapus()
def edit_barang():
    edit()
def kasir():
    kasir_interfaces()



awal()
tutup_database()
print("\nTHANKYOU\nHAVE A NICE DAY")




