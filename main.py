from buku import Buku
from perpustakaan import Perpustakaan

def tampilkan_semua(self):
        if len(self.data_buku) == 0:
            print("Belum ada data buku.")
            return
        for kode in self.data_buku:
            self.data_buku[kode].tampilkan_info()
            print("-" * 30)

def input_wajib(pesan):
    while True:
        isi = input(pesan).strip()
        if isi == "":
            print("Tidak boleh kosong!")
        elif "|" in isi:
            print("Tidak boleh memakai tanda |")
        else:
            return isi


def main():
    perpus = Perpustakaan("data_buku.txt")

    while True:
        print()
        print("=== PERPUSTAKAAN ===")
        print("1. Tambah buku")
        print("2. Cari buku")
        print("3. Ubah buku")
        print("4. Hapus buku")
        print("5. Tampilkan semua buku")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kode = input_wajib("Kode buku : ")
            judul = input_wajib("Judul     : ")
            penulis = input_wajib("Penulis   : ")
            penerbit = input_wajib("Penerbit  : ")
            tahun = input_wajib("Tahun     : ")
            buku_baru = Buku(kode, judul, penulis, penerbit, tahun)
            perpus.tambah_buku(buku_baru)
        elif pilihan == "2":
            kode = input("Masukkan kode buku: ")
            perpus.cari_buku(kode)
        elif pilihan == "3":
            kode = input("Masukkan kode buku yang diubah: ")
            perpus.ubah_buku(kode)
        elif pilihan == "4":
            kode = input("Masukkan kode buku yang dihapus: ")
            perpus.hapus_buku(kode)
        elif pilihan == "5":
            perpus.tampilkan_semua()
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()