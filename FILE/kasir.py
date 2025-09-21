
# IMPORT 
import time as t 
import datetime 
import random
import string



# MODUL
from database.database import connection


conn = connection()
cursor=conn.cursor()

sekarang = datetime.datetime.now()
tanggal = sekarang.strftime("%d-%m-%y %H:%M:%S")
  

klr = 1.5
tgu = 2.5

def random_():
    karakter = string.ascii_letters + string.digits
    angka_acak = "".join(random.choices(karakter, k=6))
    return angka_acak

barangsss ={}
struk = []

def kasir_interfaces():
    cursor.execute("SELECT * FROM BARANG")
    cek = cursor.fetchone()
    if cek is None:
        print("\nBELUM ADA ISI\n", end="\r")
        t.sleep(tgu)
        return
    else:  
        totalsemua = 0
        totalitem = 0
        while True:    
            print("+"+"="*80+"+")
            print("|"+"Selamat datang di Xioo菊地 Shop".center(78)+"|")
            cursor.execute("SELECT * FROM BARANG")
            lihat = cursor.fetchall()
            print("+"+"="*80+"+")
            print("|" + "ID".center(15) + "NAMA".center(22) + "   " +"HARGA".center(20) + "   " + "STOCK".center(17) + "|")
            print("+"+"="*80+"+")
            for id,nama,harga,stock in lihat:
                print("|" + f"     {id:<10}         {nama:<13}          {harga:<13}          {stock:<10}".upper() + "|")
            print("+"+"="*80+"+")
            print("Ketik 'stop' untuk keluar dari program")
            print("Ketik 'tambah' atau 'add' untuk nmenghitung total")
            print("")
            pilihan = input("Masukan nama/ID barang : ").strip()
            if pilihan.lower()== "stop":
                print("Keluar...", end="\r")
                t.sleep(klr)
                return
            if pilihan.lower()== "tambah" or pilihan.lower() == "add":
                if totalitem == 0 :
                    print("Anda belum memasukan item", end="\r")
                    t.sleep(2) 
                    print(" "*30, end="\r")
                else:
                    print("Menghitung total...", end="\r")
                    t.sleep(5)
                    print(" "*20, end="\r")
                    break                      

                
            elif pilihan.lower() not in ("tambah","add"):
                print("Mencari...", end="\r")
                t.sleep(2)
                cursor.execute("SELECT * FROM BARANG WHERE ID = ? OR NAMA = LOWER(?)",(pilihan,pilihan))
                hasil = cursor.fetchone()
                if not pilihan.strip():
                    print("Pilihan tidak boleh kosong", end="\r")
                    t.sleep(tgu)
                elif hasil is None:
                    print("Barang tidak ditemukan", end="\r")
                    t.sleep(tgu)
                elif hasil[3] is None or hasil[3] <= 0 :
                    print(f"Barang {hasil[1]} sedang kosong", end="\r")
                    t.sleep(tgu)   
                elif hasil is not None and hasil != ():
                    cursor.execute("SELECT NAMA,HARGA,STOCK FROM BARANG WHERE ID = ? OR NAMA = LOWER(?)", (pilihan,pilihan))
                    data = cursor.fetchone()
                    stck = int(stock)
                    if data:
                        nama, harga, stock = data
                        while True:
                            try:
                                jumlah = input(f"Masukan jumlah pembelian dari {hasil[1]} : ")
                                if jumlah.lower() == "stop":
                                    t.sleep(2)
                                    print("")
                                    break
                                jmlh = int(jumlah)
                                if jmlh < 0 :
                                    print("Jumlah tidak bisa kurang dari 0", end="\r")    
                                    t.sleep(tgu)
                                elif stck >= jmlh:
                                    totalsemua += harga * jmlh
                                    totalitem+=jmlh
                                    ht = harga * jmlh
                                    barangsss[pilihan]={"hrg":harga,"jml":jumlah,"ht" : ht}
                                    cursor.execute("UPDATE BARANG SET STOCK = STOCK -  ? WHERE ID = ? OR NAMA = LOWER(?)",(jumlah,pilihan,pilihan))
                                    conn.commit()
                                    print("Memasukan ke keranjang...", end="\r")
                                    t.sleep(tgu)
                                    break
                                elif stck < jmlh:
                                    print(f"Stock tersisa {hasil[3]}", end="\r")    
                                    t.sleep(tgu)
                                    


                            except ValueError:
                                print("Masukan jumlah yang benar")  
        print("+"+"="*80+"+")
        print("|"+" Total Semua Item ".center(80)+"|")
        print("+"+"="*80+"+") 
        print("|"+"JUMLAH".center(25)+"NAMA BARANG".center(25)+"HARGA".center(30)+"|")
        print("+"+"="*80+"+") 
        for nm,info in barangsss.items():
            print("|"+"     "+f"{info["jml"]:<10}".center(24)+f"{nm:<10}".upper().center(20)+"     "+f"{info["hrg"]:<10}".center(26) + "|")
        print("|"+"-"*80+"|") 
        print("|"+"Subtotal : ".center(40)+f"{totalsemua}".center(40)+"|")
        print("|"+"Total : ".center(40)+f"{totalsemua}".center(40)+"|")
        print("+"+"="*80+"+") 
        while True:
            try:
                bayar = int(input("Masukkan jumlah pembayaran : "))
                if bayar < 0:
                    print("Pembayaran kurang dari 0", end="\r")
                    t.sleep(3)
                elif totalsemua > bayar:
                    kureng = totalsemua - bayar
                    print(f"pembayaran kurang {kureng}", end="\r")
                    t.sleep(4)
                else:
                    kembalian = bayar - totalsemua
                    break
            except ValueError:
                print("\r"+"Masukan harga yang benar", end="\r")
                t.sleep(3)
# kembalian,bayar,totalsemua,sintaks for
        print("Mencetak struk...", end="\r") 
        t.sleep(3)      
        print("\r" + " " * 50 + "\r", end=" ")
        print("="*52)
        print("Xioo菊地 Shop".center(52))
        print("NIM: 241240001497".center(52))
        print("="*52)
        print("{:<10}{:>42}".format("Tanggal",tanggal))
        print("{:<10}{:>42}".format("Resi",random_()))
        print("="*52)
        print("{:<25} {:>5} {:>8} {:>10}".format("Nama Barang","Qty","Harga","Total"))
        print("-"*52)
        for nm,info in barangsss.items():
            print("{:<25} {:>5} {:>8} {:>10}".capitalize().format(nm,info["jml"],info["hrg"],info["ht"]))
        print("-"*52)
        print("{:<25} {:>5} {:>8} {:>10}".format("SUBTOTAL","","",totalsemua))
        print("{:<25} {:>5} {:>8} {:>10}".format("BAYAR","","",bayar))
        print("{:<25} {:>5} {:>8} {:>10}".format("KEMBALIAN","","",kembalian))
        print("="*52)
        print("TERIMAKASIH TELAH BERBELANJA".center(52))
        print("barang yang dibeli tidak dapat".center(52).capitalize())
        print("dikembalikan".center(52).capitalize())
        print("="*52)
      
        # struk.append("="*52)
        # struk.append("Xioo菊地 Shop".center(52))
        # struk.append("NIM: 241240001497".center(52))
        # struk.append("="*52)
        # struk.append("{:<10}{:>42}".format("Tanggal",tanggal))
        # struk.append("{:<10}{:>42}".format("Resi",random_()))
        # struk.append("="*52)
        # struk.append("{:<25} {:>5} {:>8} {:>10}".format("Nama Barang","Qty","Harga","Total"))
        # struk.append("-"*52)
        # for nm,info in barangsss.items():
        #     struk.append("{:<25} {:>5} {:>8} {:>10}".capitalize().format(nm,info["jml"],info["hrg"],info["ht"]))
        # struk.append("-"*52)
        # struk.append("{:<25} {:>5} {:>8} {:>10}".format("SUBTOTAL","","",totalsemua))
        # struk.append("{:<25} {:>5} {:>8} {:>10}".format("BAYAR","","",bayar))
        # struk.append("{:<25} {:>5} {:>8} {:>10}".format("KEMBALIAN","","",kembalian))
        # struk.append("="*52)
        # struk.append("TERIMAKASIH TELAH BERBELANJA".center(52))
        # struk.append("barang yang dibeli tidak dapat".center(52).capitalize())
        # struk.append("dikembalikan".center(52).capitalize())
        # struk.append("="*52)
        t.sleep(5)


