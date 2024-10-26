class Musik:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre
        
    def tampilkan(self):
        print(f"Judul: {self.judul} | Penyanyi: {self.penyanyi} | Genre: {self.genre}")

class KoleksiMusik:
    def __init__(self):
        self.koleksi = []
        
    def tambah_musik(self, musik):
        self.koleksi.append(musik)
        print(f"Berhasil: '{musik.judul}' telah ditambahkan ke koleksi Anda!")
        
    def hapus_musik(self, judul):
        panjang_awal = len(self.koleksi)
        self.koleksi = [m for m in self.koleksi if m.judul.lower() != judul.lower()]
        if len(self.koleksi) < panjang_awal:
            print(f"Berhasil: '{judul}' telah dihapus dari koleksi Anda!")
        else:
            print(f"Error: '{judul}' tidak ditemukan dalam koleksi Anda.")
            
    def tampilkan_semua(self):
        if not self.koleksi:
            print("Koleksi Anda kosong. Tambahkan beberapa musik untuk memulai!")
        else:
            print("\n=== Koleksi Musik Anda ===")
            for i, musik in enumerate(self.koleksi, 1):
                print(f"{i}.", end=" ")
                musik.tampilkan()
            print("==========================")
            
    def urutkan_musik(self):
        self.koleksi.sort(key=lambda musik: musik.judul)
        print("Koleksi telah diurutkan berdasarkan judul secara alfabetis!")
        
    def cari_musik_berdasarkan_penyanyi(self, penyanyi):
        hasil = [m for m in self.koleksi if m.penyanyi.lower() == penyanyi.lower()]
        if not hasil:
            print(f"Tidak ditemukan lagu dari penyanyi '{penyanyi}'")
        else:
            print(f"\n=== Lagu oleh {penyanyi} ===")
            for i, musik in enumerate(hasil, 1):
                print(f"{i}.", end=" ")
                musik.tampilkan()
            print("==========================")

def main():
    koleksi = KoleksiMusik()
    
    while True:
        print("\n=== Pengelola Koleksi Musik ===")
        print("1. Tambah Lagu Baru")
        print("2. Hapus Lagu")
        print("3. Lihat Semua Lagu")
        print("4. Urutkan Lagu (A-Z)")
        print("5. Cari berdasarkan Penyanyi")
        print("6. Keluar")
        print("==============================")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            genre = input("Masukkan genre: ")
            musik = Musik(judul, penyanyi, genre)
            koleksi.tambah_musik(musik)
            
        elif pilihan == '2':
            judul = input("Masukkan judul lagu yang akan dihapus: ")
            koleksi.hapus_musik(judul)
            
        elif pilihan == '3':
            koleksi.tampilkan_semua()
            
        elif pilihan == '4':
            koleksi.urutkan_musik()
            koleksi.tampilkan_semua()
            
        elif pilihan == '5':
            penyanyi = input("Masukkan nama penyanyi yang dicari: ")
            koleksi.cari_musik_berdasarkan_penyanyi(penyanyi)
            
        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan Pengelola Koleksi Musik!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()