class Buku(object):
    """description of class"""
    ISDN = ""
    judul = ""
    __jumlahDiPeredaran = 0
    tahunTerbit = 0 
    cetakan = 0
    genre = ["", ""]
    penulis = ""
    jumlahHalaman = 0

    def __init__ (self, ISDN, judul, tahunTerbit, genre, penulis, jumlahHalaman):
        self.judul = judul
        self.ISDN = ISDN
        self.tahunTerbit = tahunTerbit
        self.cetakan = 1
        self.genre = genre
        self.penulis = penulis
        self.jumlahHalaman = jumlahHalaman
        self.cetak(100)
        return

    def baca(self):
        print("Selamat membaca buku berjudul " + self.judul + " karya penulis " + self.penulis)
        return

    def cetak(self, jumlahCetak):
        self.cetakan += 1
        self.__jumlahDiPeredaran += jumlahCetak
        return

    def cekPeredaran (self):
        return self.__jumlahDiPeredaran

    def gantiJudul(self, gantiJudul) :
        self.judul = gantiJudul
        pass




