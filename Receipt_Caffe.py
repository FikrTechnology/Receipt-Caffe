import os


menu = ['1,Paket Hemat,25000', '2,Paket Nasi,35000', '3,Spesial Harga,50000']
idx = []
subTotal = 0
nama_kasir = ''
kode_kasir = ''

def receipt():
    match sistem_operasi:
        case 'posix' : os.system('clear')
        case 'nt' : os.system('cls')

    global subTotal

    print('='*100)
    print(' '*40+'Selamat Datang di Caffe')
    print('='*100)
    print(f'Kasir        : {nama_kasir}')
    print(f'NIM          : {kode_kasir}')
    print('-'*100)

    print(f"{'No':10} | {'Nama Paket':30} | {'Qty':30} | {'Harga Satuan':30}")
    print('-'*100)

    for index, data in enumerate(idx):
        data_break = data.split(",")
        quantity = data_break[0]
        paket = data_break[1]
        harga = data_break[2]
        subTotal += int(data_break[3])

        print(f"{index:10} | {paket:30} | {quantity:30} | {harga:30}")  

    pajak = int(subTotal * 0.1)

    print('-'*100)
    print('\n')
    print(' '*50 + 'Subtotal    : Rp'+ str(subTotal))
    print(' '*50 + 'Pajak       : Rp'+ str(pajak))
    print(' '*50 + 'Total       : Rp'+ str(int(subTotal + pajak)))
    print('\n')
    print('='*100)
    print('\n')

    while True:
        inp = input('Ingin Melanjutkan Orderan? [Y/N] ').upper()
        if inp == 'Y':
            idx.clear()
            subTotal = 0
            show_menu()
        elif inp == 'N':
            idx.clear()
            subTotal = 0
            kasir()
        else:
            print('Maaf Inputan anda salah')
    

def show_menu():
    match sistem_operasi:
        case 'posix' : os.system('clear')
        case 'nt' : os.system('cls')

    print('='*100)
    print(' '*40+'Selamat Datang di Caffe')
    print('='*100)
    print('\n')

    print(f"{'no':30} | {'Paket':40} | {'Harga':30}")
    print('-'*100)

    for data in menu:
        data_break = data.split(",")
        index = data_break[0]
        paket = data_break[1]
        harga = data_break[2]

        print(f"{index:30} | {paket:40} | {harga:30}")        

    print('\n')

    input_menu = int(input('Silahkan Masukkan Menu anda : '))
    sum_menu = int(input('Silahkan Masukkan banyak menu yang di pesan : '))



    if input_menu == 1:
        banyak_menu = sum_menu
        paket = 'Paket Hemat'
        harga = 25000
        if banyak_menu >= 2:
            discount = int((banyak_menu * harga) * 0.25)
            total_harga = int((banyak_menu * harga) - discount)
        else:
            total_harga = harga
        
        idx.append(f"{banyak_menu},{paket},{harga},{total_harga}")
    elif input_menu == 2:
        banyak_menu = sum_menu
        paket = 'Paket Nasi'
        harga = 35000
        if banyak_menu >= 2:
            discount = int((banyak_menu * harga) * 0.25)
            total_harga = int((banyak_menu * harga) - discount)
        else:
            total_harga = harga
        
        idx.append(f"{banyak_menu},{paket},{harga},{total_harga}")
    elif input_menu == 3:
        banyak_menu = sum_menu
        paket = 'Special Harga'
        harga = 50000
        if banyak_menu >= 2:
            discount = int((banyak_menu * harga) * 0.25)
            total_harga = int((banyak_menu * harga) - discount)
        else:
            total_harga = harga
        
        idx.append(f"{banyak_menu},{paket},{harga},{total_harga}")
    else:
        print('Maaf inputan anda salah')

    while True:
        inp = input('Ingin memesan lagi? [Y/N] ').upper()
        if inp == 'Y':
            show_menu()
        elif inp == 'N':
            receipt()
        else:
            print('Maaf Inputan anda salah')


def kasir():
    match sistem_operasi:
        case 'posix' : os.system('clear')
        case 'nt' : os.system('cls')

    global nama_kasir
    global kode_kasir

    print('='*100)
    print(' '*40+'Selamat Datang di Caffe')
    print('='*100)
    print('\n')

    nama_kasir = input(' '*20+'Silahkan Masukkan Nama   : ')
    kode_kasir = input(' '*20+'Silahkan Masukkan Kode   : ')

    print('\n')    
    print('='*100)

    show_menu()


if __name__ == '__main__':

    sistem_operasi = os.name

    match sistem_operasi:
        case 'posix' : os.system('clear')
        case 'nt' : os.system('cls')
    
    kasir()