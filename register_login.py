import csv
import os
import string    
import random 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== JUAL BELI HASIL PANEN ===")
    print("[1] LOGIN")
    print("[2] REGISTER")
    print("[3] UBAH PASSWORD")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        login()
    elif(selected_menu == "2"):
       register()
    elif(selected_menu == "3"):
       ubahPassword()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_opsi():
    clear_screen()
    total = 0
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                total += int(1)
    print("Total pesanan anda saat ini: ",total)
    print("===========================")
    print("[1] TAMPIL SELURUH MENU")
    print("[2] DATA BELANJA SAYA")
    print("[3] STRUK BELANJA SAYA")
    print("[4] HISTORY BELANJA SAYA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        showalldata()
    elif(selected_menu == "2"):
       belanjasaya()
    elif(selected_menu == "3"):
       strukbelanja()
    elif(selected_menu == "4"):
       datahistory()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        
        
def datahistory():
    clear_screen()
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===========================")
    print("Pilih Kode Struk Anda!")
    print("==============================")
    print("Kode")
    print("==============================")
    contacts = []
    with open("dataStruk.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if datalogin == row1[0]:
                print(f'{row1[1]}')
    print("==============================")
    struk = input("Input kode struk anda: ")
    clear_screen()
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===========================")
    print("Data Pesanan Anda!")
    print("==============================")
    print("Barang          Harga")
    print("==============================")
    with open("dataBelanjaPelanggan.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (struk == row1[5]):
                print(f'{row1[1]} \t {row1[2]}')
    print("==============================")
    print("Silahkan pilih opsi dibawah ini")
    print("[1] KEMBALI")
    print("[2] MENU UTAMA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        datahistory()
    elif(selected_menu == "2"):
       show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
    


def showalldata():
    clear_screen()
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===========================")
    print("No        Barang        Harga")
    print("==============================")
    contacts = []
    with open("barang.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            contacts.append(row)
            print(f'{row[0]} \t {row[1]} \t {row[2]}')

    print("==============================")
    print("Silahkan pilih opsi dibawah ini")
    print("[1] PESAN")
    print("[2] HAPUS PESAN")
    print("[3] KEMBALI")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        pesan()
    elif(selected_menu == "2"):
       editpesan()
    elif(selected_menu == "3"):
       show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")


def pesan():
    clear_screen()
    total1 = 0
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===========================")
    print("No        Barang        Harga")
    print("==============================")
    contacts = []
    with open("barang.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            contacts.append(row)
            print(f'{row[0]} \t {row[1]} \t {row[2]}')
    print("==============================")
    csv_file = csv.reader(open('barang.csv', "r"), delimiter=",")
    number = input('Masukkan No/Nama Barang: ')
    jumlah = int(input('Masukkan jumlah: '))
   
    
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if number == row[0] or number == row[1]:
            print("Data barang berhasil di tambah ke pesanan!")
            with open("history.csv",mode="a",newline="") as f:
                writerr = csv.writer(f,delimiter=",")
                email = row[1]
                password = row[2]
                total1 = int(row[2])*jumlah
                writerr.writerow([datalogin,email,password,jumlah,total1])
    print("==============================")
    print("Silahkan pilih opsi dibawah ini")
    print("[1] KEMBALI")
    print("[2] MENU UTAMA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        pesan()
    elif(selected_menu == "2"):
       show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")



def belanjasaya():
    clear_screen()
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===============================================================")
    print("Data Pesanan Anda!")
    print("===============================================================")
    print("Barang          Harga Satuan     Stok          Total")
    print("===============================================================")
    contacts = []
    lines = list()
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                print(f'{row1[1]} \t {row1[2]} \t\t   {row1[3]} \t\t{row1[4]}')
    print("==============================")
    print("Silahkan pilih opsi dibawah ini")
    print("[1] KEMBALI")
    print("[2] MENU UTAMA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        show_opsi()
    elif(selected_menu == "2"):
        show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
    



def editpesan():
    clear_screen()
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===============================================================")
    print("Pilih Barang Yang Akan Dihapus!")
    print("===============================================================")
    print("Barang          Harga Satuan     Stok          Total")
    print("===============================================================")
    contacts = []
    lines = list()
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                print(f'{row1[1]} \t {row1[2]} \t\t   {row1[3]} \t\t{row1[4]}')
    print("==============================")
    barang = input("Masukkan Nama Barang: ")
    
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            lines.append(row1)
            if datalogin == row1[0]:
                for field in row1:
                    if field == barang:
                        lines.remove(row1)
                        print("Data barang berhasil dihapus!")
                
    with open('history.csv', 'w',newline="") as writeFile:
       
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    print("==============================")
    print("Silahkan pilih opsi dibawah ini")
    print("[1] KEMBALI")
    print("[2] MENU UTAMA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        show_opsi()
    elif(selected_menu == "2"):
       show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        
        
def tambahdataStruk(data):
    lines = list()
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            lines.append(row1)
            if datalogin == row1[0]:
                for field in row1:
                    if field == datalogin:
                        print("")
        with open("dataStruk.csv",mode="a",newline="") as f:
            writerr = csv.writer(f,delimiter=",")
            writerr.writerow([row1[0],data])
            tambahdatabelanja(data)

def tambahdatabelanja(data):
    lines = list()
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            lines.append(row1)
            if datalogin == row1[0]:
                for field in row1:
                    if field == datalogin:
                        with open("dataBelanjaPelanggan.csv",mode="a",newline="") as f:
                            writerr = csv.writer(f,delimiter=",")
                            writerr.writerow([row1[0],row1[1],row1[2],row1[3],row1[4],data])
                            hapusall()



def hapusall():
    lines = list()
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            lines.append(row1)
            if datalogin == row1[0]:
                for field in row1:
                    if field == datalogin:
                        lines.remove(row1)

    with open('history.csv', 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)



def strukbelanja():
    clear_screen()
    global total,bayar
    print("=== JUAL BELI HASIL PANEN ===")
    print("Kamu Login Sebagai: ",datalogin)
    print("===============================================================")
    print("Total Keseluruhan Belanja Kamu!")
    print("===============================================================")
    print("Barang          Harga Satuan     Stok          Total")
    print("===============================================================")
    contacts = []
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                print(f'{row1[1]} \t {row1[2]} \t\t   {row1[3]} \t\t{row1[4]}')

    with open("history.csv","r") as f:
        total = 0
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                total += int(row1[4])
              
               
        print("==============================")
        print("subtotal:       ",total)
        print("==============================")
        bayar = int(input("Inputkan pembayaran anda:     "))
        totalakhir = bayar - total
        if bayar > total:
            print("Kembalian:       ",totalakhir)
        elif bayar == total:
             print("Tidak ada kembalian karena uang pas!!")
        else:
            print("Uang yang diiputkan kurang!!:       ",totalakhir)

    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
    print("==============================")
    clear_screen()
    print("Struk Akhir Anda")
    print("==============================")
    print("Kode Struk: ",str(ran))
    print("==============================")
    print("Barang          Harga")
    print("==============================")
    contacts = []
    with open("history.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                print(f'{row1[1]} \t {row1[2]}')
    
    #persiapan sum
    with open("history.csv","r") as f:
        total = 0
        reader = csv.reader(f,delimiter=",")
        for row1 in reader:
            if (datalogin == row1[0]):
                total += int(row1[4])
        print("==============================")
        print("subtotal:       ",total)
        print("==============================")
        print("uang anda:      ",bayar)
        if bayar > total:
            print("Kembalian:      ",totalakhir)
            tambahdataStruk(str(ran))
            
        elif bayar == total:
             print("Uang yang anda berikan pas!!")
             tambahdataStruk(str(ran))
        else:
            print("Pembayaran anda kurang sebanyak!!:      ",totalakhir)
            tambahdataStruk(str(ran))
    print("==============================")
    print("Terimakasih telah berbelanja di toko kami :)")
    print("==============================")
    print("Silahkan pilih opsi dibawah ini")
    print("[1] KEMBALI")
    print("[2] MENU UTAMA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        pesan()
    elif(selected_menu == "2"):
       show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")            
    print("Silahkan pilih opsi dibawah ini")
    print("[1] KEMBALI")
    print("[2] MENU UTAMA")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        pesan()
    elif(selected_menu == "2"):
       show_opsi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")              
    


def register():
    statusregis = 0
    with open("users.csv",mode="a",newline="") as f:
        writerr = csv.writer(f,delimiter=",")
        email = input("Please enter username: ")
        password = input("password: ")
        password2 = input("konfirmasi password: ")
        if password == password2:
            writerr.writerow([email,password])
            statusregis = 1
            
        else:
            print("password dan konfirmasi pasword berbeda!")
    if statusregis == 1:
        show_menu()

def login():
    clear_screen()
    email = input("username: ")
    password = input("password: ")
    global datalogin,status
    with open("users.csv","r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [email,password]:
                datalogin = email
                status = True
                show_opsi()
                return True
        status = False
        print("try again")
        return False    
    
def ubahPassword():
    clear_screen()
    contacts = []
    line_count = 0
    statusubah = 0
    email = input("Inputkan username anda: ")
    global datalogin,status
    
    with open("users.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        lines = []
        for line in reader:
            if line[0] == email:
                password = input("Inputkan password baru anda: ")
                statusubah = 1
                line_count += 1
                line[1] = password
            lines.append(line)

    if statusubah == 1:
        with open("users.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)
            print("Password berhasil di ubah!")
        print("Silahkan pilih opsi dibawah ini")
        print("[1] KEMBALI")
        print("[0] Exit")
        print("------------------------")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            show_menu()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!") 
    else:
        print("Data tidak di temukan")
        print("Silahkan pilih opsi dibawah ini")
        print("[1] KEMBALI")
        print("[0] Exit")
        print("------------------------")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            show_menu()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!") 
    
    

show_menu()





