

# IMPORT
import bcrypt
import time as t

# MODUL
from database.database import connection

conn = connection()
cursor = conn.cursor()

def login_admin():
    global username
    print("\nKetik 'stop' untuk keluar dari program\n")
    username = input("Masukan username : ")
    if username.lower() == "stop":
        print("Keluar..", end="\r")
        t.sleep(3)
        return
    password = input("Masukan password : ")  
    if password.lower() == "stop":
        print("Keluar..", end="\r")
        t.sleep(3)
        return
    cursor.execute("SELECT pass FROM login WHERE username = ?",(username,))
    data = cursor.fetchone()
    try:
        if data:                       
            stored_hash = data[0]
            if bcrypt.checkpw(password.encode("utf-8"),stored_hash.encode("utf-8")):
                cursor.execute("SELECT nama FROM login WHERE username = ?",(username,))
                
                for nama in cursor.fetchone():
                    print("\nLoading...", end="\r")
                    t.sleep(3)
                    print(f"\nSelamat datang admin {nama[0]}\n")
                    t.sleep(5)
                    return True
            else:
                t.sleep(2)
                print("\nWrong password")
                t.sleep(2)
                return False
        else:
            t.sleep(2)
            print("\nWrong username")
            t.sleep(2)
            return False
        
    except Exception as e:
            print(f"[ERROR] bcrypt gagal: {e}")
            return False    

def nama_admin():
    cursor.execute("SELECT nama FROM login WHERE username = ?",(username,)) 
    for nama in cursor.fetchone():
        return f"Selamat Datang Admin {nama}"
    





