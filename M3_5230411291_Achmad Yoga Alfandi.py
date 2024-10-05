class Menu:
    def __init__(self):
        self.menu_makanan = []
        self.menu_minuman = []

    def tampilkan_menu(self):
        print(" Pilihan Menu:")
        print("1. Tampilkan Daftar Menu Makanan")
        print("2. Tampilkan Daftar Menu Minuman")
        print("3. Tambahkan Menu (Makanan atau Minuman)")
        print("4. Keluar Program")

    def tampilkan_menu_makanan(self):
        print("Daftar Menu Makanan:")
        if not self.menu_makanan:
            print("Belum ada menu makanan.")
        else:
            for i, item in enumerate(self.menu_makanan):
                print(f"{i+1}. {item['nama']} -> - Rp {item['harga']}")

    def tampilkan_menu_minuman(self):
        print("Daftar Menu Minuman:")
        if not self.menu_minuman:
            print("Belum ada menu minuman.")
        else:
            for i, item in enumerate(self.menu_minuman):
                print(f"{i+1}. {item['nama']} -> - Rp {item['harga']}")

    def tambahkan_item_menu(self):
        print("\nTambahkan Menu:")
        print("1. Tambahkan Makanan")
        print("2. Tambahkan Minuman")
        pilihan = input("Pilih jenis menu yang ingin ditambahkan: ").strip()

        if pilihan == "1":
            self.tambahkan_makanan()
        elif pilihan == "2":
            self.tambahkan_minuman()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    def tambahkan_makanan(self):
        nama_item = input("Masukkan nama makanan: ").strip()
        harga_item = input("Masukkan harga makanan: ").strip()

        item = {"nama": nama_item, "harga": harga_item}
        self.menu_makanan.append(item)
        print(f"Menu makanan '{nama_item}' berhasil ditambahkan.")

    def tambahkan_minuman(self):
        nama_item = input("Masukkan nama minuman: ").strip()
        harga_item = input("Masukkan harga minuman: ").strip()

        item = {"nama": nama_item, "harga": harga_item}
        self.menu_minuman.append(item)
        print(f"Menu minuman '{nama_item}' berhasil ditambahkan.")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                self.tampilkan_menu_makanan()
            elif pilihan == "2":
                self.tampilkan_menu_minuman()
            elif pilihan == "3":
                self.tambahkan_item_menu() 
            elif pilihan == "4":
                print("Keluar dari program. Terima Kasih")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu = Menu()
    menu.jalankan()
