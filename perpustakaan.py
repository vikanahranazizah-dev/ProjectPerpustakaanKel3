from buku import Buku

class Perpustakaan:
    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.data_buku = {}
        self.muat_data()

    def muat_data(self):
        self.data_buku = {}
        try:
            file = open(self.nama_file, "r")
            for baris in file:
                baris = baris.strip()
                if baris == "":
                    continue
                bagian = baris.split("|")
                if len(bagian) == 5:
                    buku = Buku(bagian[0], bagian[1], bagian[2],
                                bagian[3], bagian[4])
                    self.data_buku[buku.kode] = buku
            file.close()
        except FileNotFoundError:
            pass

    def simpan_data(self):
        file = open(self.nama_file, "w")
        for kode in self.data_buku:
            file.write(self.data_buku[kode].ke_baris() + "\n")
        file.close()

    def tambah_buku(self, buku):
            if buku.kode in self.data_buku:
                print("Gagal, kode buku sudah ada!")
                return
            self.data_buku[buku.kode] = buku
            self.simpan_data()
            print("Buku berhasil ditambahkan.")
    
    def cari_buku(self, kode):
            if kode in self.data_buku:
                print("Buku ditemukan:")
                self.data_buku[kode].tampilkan_info()
            else:
                print("Buku dengan kode", kode, "tidak ditemukan.")

    def hapus_buku(self, kode):
            if kode not in self.data_buku:
                print("Buku dengan kode", kode, "tidak ditemukan.")
                return
            self.data_buku[kode].tampilkan_info()
            jawab = input("Yakin ingin menghapus? (y/n): ")
            if jawab.lower() == "y":
                del self.data_buku[kode]
                self.simpan_data()
                print("Buku berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

    def ubah_buku(self, kode):
            if kode not in self.data_buku:
                print("Buku dengan kode", kode, "tidak ditemukan.")
                return
            buku = self.data_buku[kode]
            print("Data saat ini:")
            buku.tampilkan_info()
            print("Isi data baru (kosongkan jika tidak diubah)")
    
            judul = input("Judul baru    : ")
            penulis = input("Penulis baru  : ")
            penerbit = input("Penerbit baru : ")
            tahun = input("Tahun baru    : ")
    
            if judul != "":
                buku.judul = judul
            if penulis != "":
                buku.penulis = penulis
            if penerbit != "":
                buku.penerbit = penerbit
            if tahun != "":
                buku.tahun = tahun
    
            self.simpan_data()
            print("Buku berhasil diperbarui.")

    
    
