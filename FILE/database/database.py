


# IMPORT
import sqlite3
import time as t

# MODUL
def connection():
    return sqlite3.connect("FILE/database/customers.db")

conn = connection()
cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS login(id CHAR(6) NOT NULL PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            username VARCHAR(255) NOT NULL,
            pass VARCHAR(255) NOT NULL,
            UNIQUE(username)
               )""")

cursor.execute("""
            CREATE TABLE IF NOT EXISTS barang(id CHAR(4) NOT NULL PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            harga INT(60) NOT NULL,
            stock INT(60) NOT NULL DEFAULT 0
               )""")
 
conn.commit()


def tutup_database():
    print("Menutup database...")
    t.sleep(2)
    try:
        cursor.close()
    except:
        pass
    try:
        conn.close()
    except:
        pass
    try:
        cursor.execute("SELECT * FROM barang")  
        print("Database masih terbuka")
        return True
    except sqlite3.ProgrammingError:
        print("Database sudah ditutup")
        return False  




