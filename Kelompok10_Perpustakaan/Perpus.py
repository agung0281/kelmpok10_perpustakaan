from Buku import Buku
import Kelompok10_Perpustakaan

lanjut = True
ulang = True
bukuKe = []
PercyJackson = Buku("123456789", "Percy Jackson's Greek Gods", 2014, ("Greek mythology"), "Rick Riordan", 469)
bukuKe.append(PercyJackson)

SherlockHolmes = Buku("987654321", "Young Sherlock Holmes: Death Cloud", 2010, ("Detective Fiction"), "Andy Lane", 666)
bukuKe.append(SherlockHolmes)

Uburubur = Buku("978-979-780-915-7", "Ubur-ubur Lembur", 2018, ("Comedy"), "Raditya Dika", 240)
bukuKe.append(Uburubur)

while lanjut == True:
    print('1. Tambah Buku\n2. Cari Buku\n3. Baca Buku\n4. Ganti Judul\n5. Keluar')
    pilih = int(input('Pilih operasi Anda : '))

    while(not(pilih >= 1 and pilih <= 5)): 
        print('Menu pilihan ', pilih, ' tidak ada dalam menu, silahkan pilih kembali')
        print('1. Tambah Buku\n2. Cari Buku\n3. Baca Buku\n4. Ganti Judul\n5. Keluar')
        pilih = int(input('Pilih operasi Anda : '))

    if pilih == 1:
        print('\nIni adalah menu Tambah Buku')
        kodeBukuBaru = input('ISDN\t: ')
        judulBaru    = input('Judul\t: ')
        penulisBaru  = input('Penulis\t: ')
        tahunTerbit  = input('Tahun\t: ')
        cetakan      = input('Cetakan\t: ')
        genreBaru    = input('Genre\t: ')
        halaman      = input('Jumlah halaman\t: ')
        
        bukuBaru = Buku(kodeBukuBaru, judulBaru, tahunTerbit, genreBaru, penulisBaru,halaman)
        bukuKe.append(bukuBaru)

    elif pilih == 2:
        print('\nIni adalah menu Cari Buku')
        noUrut = int(input('Pilih nomor buku : '))
        cariBuku = bukuKe[noUrut - 1]

        print('ISDN\t\t: ', cariBuku.ISDN)
        print('Judul\t\t: ', cariBuku.judul)
        print('Tahun terbit\t: ', cariBuku.tahunTerbit)
        print('Cetakan\t\t: ', cariBuku.cetakan)
        print('Genre\t\t: ', cariBuku.genre)
        print('Penulis\t\t: ', cariBuku.penulis)
        print('Jumlah halaman\t: ', cariBuku.jumlahHalaman)
        print('Jumlah peredaran: ', cariBuku.cekPeredaran())

    elif pilih == 3:
        print('\nIni adalah menu Baca Buku')
        noUrut = int(input('Pilih nomor buku : '))
        bacaBuku = bukuKe[noUrut - 1]
        bacaBuku.baca()

    elif pilih == 4:
        print('\nIni adalah menu Ganti Judul')
        noUrut   = int(input('Pilih nomor buku\t: '))
        bukuJudulBaru = bukuKe[noUrut - 1]
        
        judulBaru = input('Judul baru : ')
        bukuJudulBaru.gantiJudul(judulBaru)

    elif pilih == 5:
        print('\nIni adalah Menu Daftar Judul Buku')
        for n in range(0,len(bukuKe)):
            print(n+1,". " ,bukuKe[n].judul)

    elif pilih == 6:
        lanjut = False

    pilihLanjut = input('\nAnda ingin mencari buku lagi? : ')
    while (not(pilihLanjut=='y'or pilihLanjut=='n')):
        pilihLanjut = input('\nAnda ingin mencari buku lagi?: ')    
    if pilihLanjut == 'y':
        lanjut = True
    else :
        lanjut = False

