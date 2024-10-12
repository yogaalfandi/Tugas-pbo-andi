class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama
        self.ktp = ktp
        self.limit_pinjaman = limit_pinjaman
        self.pinjaman = None

class Pinjaman:
    def __init__(self, jumlah, bunga, bulan):
        self.jumlah = jumlah
        self.bunga = bunga
        self.bulan = bulan

    def angsuran_pokok(self):
        return self.jumlah / self.bulan

    def bunga_bulanan(self):
        return (self.jumlah * self.bunga / 100) / self.bulan

    def total_angsuran_bulanan(self):
        return self.angsuran_pokok() + self.bunga_bulanan()

    def total_angsuran(self):
        return self.total_angsuran_bulanan() * self.bulan

daftar_debitur = []

def validasi_input_angka(prompt, tipe=int):
    while True:
        try:
            return tipe(input(prompt))
        except ValueError:
            print(f"Input tidak valid. Harap masukkan {tipe.__name__} yang benar.")

def tambah_debitur():
    print("\n===== Tambah Debitur Baru =====")
    nama = input("Masukkan nama debitur: ")
    ktp = input("Masukkan nomor KTP: ")
    limit_pinjaman = validasi_input_angka("Masukkan limit pinjaman: ")

    if any(debitur.ktp == ktp for debitur in daftar_debitur):
        print("Gagal menambahkan debitur, KTP sudah terdaftar.")
    else:
        debitur_baru = Debitur(nama, ktp, limit_pinjaman)
        daftar_debitur.append(debitur_baru)
        print(f"Debitur atas nama {nama} berhasil ditambahkan.")

    input("\nTekan Enter untuk melanjutkan...")

def tampilkan_debitur():
    print("\n===== Daftar Debitur =====")
    if not daftar_debitur:
        print("Tidak ada debitur terdaftar.")
    else:
        for debitur in daftar_debitur:
            print(f"Nama: {debitur.nama}, KTP: {debitur.ktp}, Limit Pinjaman: Rp.{debitur.limit_pinjaman}")
    
    input("\nTekan Enter untuk melanjutkan...")

def cari_debitur():
    print("\n===== Cari Debitur =====")
    nama = input("Masukkan nama debitur yang ingin dicari: ")
    hasil_cari = [debitur for debitur in daftar_debitur if debitur.nama.lower() == nama.lower()]
    if hasil_cari:
        for debitur in hasil_cari:
            print(f"Nama: {debitur.nama}, KTP: {debitur.ktp}, Limit Pinjaman: Rp.{debitur.limit_pinjaman}")
    else:
        print("Debitur tidak ditemukan.")
    
    input("\nTekan Enter untuk melanjutkan...")

def tambah_pinjaman():
    print("\n===== Tambah Pinjaman =====")
    nama = input("Masukkan nama debitur yang akan menambah pinjaman: ")
    debitur = next((d for d in daftar_debitur if d.nama.lower() == nama.lower()), None)
    
    if debitur is None:
        print("Gagal menambahkan pinjaman. Nama debitur tidak ditemukan.")
        input("\nTekan Enter untuk melanjutkan...")
        return

    jumlah_pinjaman = validasi_input_angka("Masukkan jumlah pinjaman: ")
    bunga = validasi_input_angka("Masukkan bunga pinjaman (%): ", float)
    bulan = validasi_input_angka("Masukkan lama pinjaman (bulan): ")

    if jumlah_pinjaman > debitur.limit_pinjaman:
        print(f"Gagal menambahkan pinjaman. Jumlah pinjaman Rp.{jumlah_pinjaman} melebihi limit Rp.{debitur.limit_pinjaman}.")
    else:
        pinjaman_baru = Pinjaman(jumlah_pinjaman, bunga, bulan)
        debitur.pinjaman = pinjaman_baru
        print(f"Pinjaman sebesar Rp.{jumlah_pinjaman} untuk debitur {debitur.nama} berhasil ditambahkan.")

    input("\nTekan Enter untuk melanjutkan...")

def tampilkan_pinjaman():
    print("\n===== Daftar Pinjaman =====")
    if not daftar_debitur:
        print("Tidak ada debitur terdaftar.")
    else:
        for debitur in daftar_debitur:
            if debitur.pinjaman:
                angsuran_pokok = debitur.pinjaman.angsuran_pokok()
                bunga_bulanan = debitur.pinjaman.bunga_bulanan()
                total_angsuran_bulanan = debitur.pinjaman.total_angsuran_bulanan()
                total_angsuran = debitur.pinjaman.total_angsuran()

                print(f"Nama: {debitur.nama}, Pinjaman: Rp.{debitur.pinjaman.jumlah}, "
                      f"Bunga: {debitur.pinjaman.bunga}%, Bulan: {debitur.pinjaman.bulan}, "
                      f"Angsuran Pokok per bulan: Rp.{angsuran_pokok:,.2f}, "
                      f"Bunga Bulanan: Rp.{bunga_bulanan:,.2f}, "
                      f"Total Angsuran Bulanan: Rp.{total_angsuran_bulanan:,.2f}, "
                      f"Total Angsuran: Rp.{total_angsuran:,.2f}")
            else:
                print(f"Nama: {debitur.nama}, Belum memiliki pinjaman.")
    
    input("\nTekan Enter untuk melanjutkan...")

def menu_debitur():
    while True:
        print("\n===== Menu Kelola Debitur =====")
        print("1. Tambah Debitur")
        print("2. Tampilkan Debitur")
        print("3. Cari Debitur")
        print("4. Kembali ke menu utama")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tambah_debitur()
        elif pilihan == "2":
            tampilkan_debitur()
        elif pilihan == "3":
            cari_debitur()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_pinjaman():
    while True:
        print("\n===== Menu Kelola Pinjaman =====")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Pinjaman")
        print("3. Kembali ke menu utama")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tambah_pinjaman()
        elif pilihan == "2":
            tampilkan_pinjaman()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_utama():
    while True:
        print("\n===== Menu Utama =====")
        print("1. Kelola Debitur")
        print("2. Kelola Pinjaman")
        print("3. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            menu_debitur()
        elif pilihan == "2":
            menu_pinjaman()
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu_utama()
