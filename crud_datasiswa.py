import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="belajarpy"
)

def insertData(db):
    nama = input("Masukkan Nama Siswa : ")
    alamat = input("Masukkan Alamat Siswa : ")
    val = (nama, alamat)
    mycursor = db.cursor()
    sql = "Insert Into siswa (nama, alamat) values (%s, %s)"
    mycursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil Disimpan".format(mycursor.rowcount))
    validasiexit(db)

def showData(db):
    mycursor = db.cursor()
    sql="SELECT * FROM siswa"
    mycursor.execute(sql)
    hasil = mycursor.fetchall()
    if mycursor.rowcount < 0:
        print("Tidak Ada Data")
        validasiexit(db)
    else:
        for data in hasil:
            print(data)
        validasiexit(db)

def showDataforupdate(db):
    mycursor = db.cursor()
    sql="SELECT * FROM siswa"
    mycursor.execute(sql)
    hasil = mycursor.fetchall()
    if mycursor.rowcount < 0:
        print("Tidak Ada Data")
    else:
        for data in hasil:
            print(data)


def updateData(db):
    mycursor = db.cursor()
    showDataforupdate(db)
    nis = input("Pilih Nomor Induk Siswa : ")
    nama = input("Masukkan Nama Siswa Baru : ")
    alamat = input("Masukkan Alamat Siswa Baru : ")
    sql = "UPDATE siswa set nama = %s, alamat = %s where nis = %s"
    val = (nama, alamat, nis)
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil diubah".format(mycursor.rowcount))
    validasiexit(db)


def deleteData(db):
    mycursor = db.cursor()
    showDataforupdate(db)
    nis = input("Pilih NIS Siswa Yang Ingin Dihapus : ")
    sql = "Delete from siswa where nis=%s"
    val = (nis,)
    mycursor.execute(sql, val)
    db.commit()
    print("{} data berhasil di Hapus".format(mycursor.rowcount))
    validasiexit(db)

#Ryfan Maulana

def searchData(db):
    mycursor = db.cursor()
    key = input("Masukkan Keyword Pencarian : ")
    sql = "SELECT * FROM siswa WHERE nama LIKE %s OR alamat LIKE %s"
    val = ("%{}%".format(key), "%{}%".format(key))
    mycursor.execute(sql, val)
    hasil = mycursor.fetchall()
    if mycursor.rowcount < 0:
        print("Tidak Ada Data Seperti itu")
    else:
        for data in hasil:
            print(data)
    validasiexit(db)


def main_menu(db):
    print("")
    print("=== DATABASE SISWA CLI ===")
    print("1. TAMBAH DATA SISWA")
    print("2. TAMPILKAN DATA SISWA")
    print("3. UPDATE DATA SISWA")
    print("4. HAPUS DATA SISWA")
    print("5. CARI SISWA")
    print("0. KELUAR")
    print("==========================")
    menu = input("Pilih Menu > ")
    
    #Ryfan Maulana

    # clear screen Bisa menggunakan cls(windows) / clear(linux)
    os.system("cls") #windows
    # os.system("clear") #linux

    if menu == "1":
        insertData(db)
    elif menu == "2":
        showData(db)
    elif menu == "3":
        updateData(db)
    elif menu == "4":
        deleteData(db)
    elif menu == "5":
        searchData(db)
    elif menu == "0":
        exit()
    else:
        print("Tidak Ada Pilihan Seperti Itu")


def validasiexit(db):
    men = input("Kembali Ke Menu? Y/N : ")
    if men == "Y".upper().lower():
        main_menu(db)
    elif men == "N".upper().lower():
        exit()
    else:
        print("Tidak Ada Pilihan Seperti Itu, Harap Pilih Kembali")
        validasiexit(db)

if __name__ == "__main__":
  while(True):
    main_menu(db)
