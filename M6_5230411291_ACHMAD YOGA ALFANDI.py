from typing import Optional
from datetime import datetime
import os
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

class Order:
    def __init__(self, nama: str, detail: str):
        self._id: int = 0
        self.nama: str = nama
        self.detail: str = detail
        self.pengiriman: list['Pengiriman'] = []
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, nilai: int):
        self._id = nilai
        
    def proses_order(self):
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.GREEN}✓ Memproses pesanan untuk: {Fore.YELLOW}{self.nama}")
        print(f"{Fore.GREEN}✓ Detail pesanan: {Fore.YELLOW}{self.detail}")
        print(f"{Fore.GREEN}✓ Status: {Fore.YELLOW}Pesanan telah berhasil diproses!")
        print(f"{Fore.CYAN}{'='*50}")
        
    def tambah_pengiriman(self, pengiriman: 'Pengiriman'):
        self.pengiriman.append(pengiriman)
        
    def __str__(self) -> str:
        return f"Pesanan(id={self._id}, nama={self.nama}, detail={self.detail})"


class Pengiriman:
    def __init__(self, id: int, nama: str, keterangan: str, tanggal: str, alamat: str):
        self.id: int = id
        self.nama: str = nama
        self.keterangan: str = keterangan
        self.tanggal: str = tanggal
        self.alamat: str = alamat
        self.status: str = "Menunggu"
        
    def proses_pengiriman(self):
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.GREEN}➤ Memproses pengiriman untuk: {Fore.YELLOW}{self.nama}")
        print(f"{Fore.GREEN}➤ Alamat pengiriman: {Fore.YELLOW}{self.alamat}")
        print(f"{Fore.GREEN}➤ Keterangan: {Fore.YELLOW}{self.keterangan}")
        print(f"{Fore.GREEN}➤ Tanggal: {Fore.YELLOW}{self.tanggal}")
        self.status = "Sedang Diproses"
        print(f"{Fore.GREEN}➤ Status: {Fore.YELLOW}{self.status}")
        print(f"{Fore.CYAN}{'='*50}")
        
    def __str__(self) -> str:
        return f"Pengiriman(id={self.id}, nama={self.nama}, alamat={self.alamat}, status={self.status})"


def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_menu():
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.WHITE}{Back.BLUE} SISTEM PEMESANAN DAN PENGIRIMAN ".center(50))
    print(f"{Fore.CYAN}{'═'*50}")
    print(f"{Fore.YELLOW}1. {Fore.WHITE}Buat Pesanan Baru")
    print(f"{Fore.YELLOW}2. {Fore.WHITE}Tambah Pengiriman ke Pesanan")
    print(f"{Fore.YELLOW}3. {Fore.WHITE}Lihat Semua Pesanan")
    print(f"{Fore.YELLOW}4. {Fore.WHITE}Lihat Detail Pesanan")
    print(f"{Fore.YELLOW}5. {Fore.WHITE}Proses Pengiriman")
    print(f"{Fore.YELLOW}6. {Fore.WHITE}Keluar")
    print(f"{Fore.CYAN}{'═'*50}")


def buat_pesanan() -> Order:
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.WHITE}{Back.BLUE} BUAT PESANAN BARU ".center(50))
    print(f"{Fore.CYAN}{'═'*50}")
    nama = input(f"{Fore.GREEN}Masukkan nama pelanggan: {Fore.WHITE}")
    detail = input(f"{Fore.GREEN}Masukkan detail pesanan: {Fore.WHITE}")
    pesanan = Order(nama=nama, detail=detail)
    pesanan.id = len(daftar_pesanan) + 1
    pesanan.proses_order()
    return pesanan


def tambah_pengiriman(pesanan: Order) -> Pengiriman:
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.WHITE}{Back.BLUE} TAMBAH PENGIRIMAN BARU ".center(50))
    print(f"{Fore.CYAN}{'═'*50}")
    id_pengiriman = len(pesanan.pengiriman) + 1
    nama = pesanan.nama
    keterangan = input(f"{Fore.GREEN}Masukkan keterangan pengiriman: {Fore.WHITE}")
    
    while True:
        tanggal = input(f"{Fore.GREEN}Masukkan tanggal pengiriman (YYYY-MM-DD): {Fore.WHITE}")
        try:
            datetime.strptime(tanggal, '%Y-%m-%d')
            break
        except ValueError:
            print(f"{Fore.RED}Format tanggal salah! Gunakan format YYYY-MM-DD")
    
    alamat = input(f"{Fore.GREEN}Masukkan alamat pengiriman: {Fore.WHITE}")
    
    pengiriman = Pengiriman(
        id=id_pengiriman,
        nama=nama,
        keterangan=keterangan,
        tanggal=tanggal,
        alamat=alamat
    )
    return pengiriman


def lihat_pesanan(daftar_pesanan: list[Order]):
    if not daftar_pesanan:
        print(f"\n{Fore.RED}Belum ada pesanan!")
        return
    
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.WHITE}{Back.BLUE} DAFTAR SEMUA PESANAN ".center(50))
    print(f"{Fore.CYAN}{'═'*50}")
    
    for pesanan in daftar_pesanan:
        print(f"\n{Fore.GREEN}ID Pesanan: {Fore.YELLOW}{pesanan.id}")
        print(f"{Fore.GREEN}Nama Pelanggan: {Fore.YELLOW}{pesanan.nama}")
        print(f"{Fore.GREEN}Detail: {Fore.YELLOW}{pesanan.detail}")
        print(f"{Fore.GREEN}Jumlah pengiriman: {Fore.YELLOW}{len(pesanan.pengiriman)}")
        print(f"{Fore.CYAN}{'-'*50}")


def lihat_detail_pesanan():
    id_pesanan = int(input(f"\n{Fore.GREEN}Masukkan ID Pesanan: {Fore.WHITE}"))
    pesanan = next((pesanan for pesanan in daftar_pesanan if pesanan.id == id_pesanan), None)
    
    if pesanan is None:
        print(f"\n{Fore.RED}Pesanan dengan ID {id_pesanan} tidak ditemukan!")
        return
    
    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"{Fore.WHITE}{Back.BLUE} DETAIL PESANAN ".center(50))
    print(f"{Fore.CYAN}{'═'*50}")
    
    print(f"{Fore.GREEN}ID Pesanan: {Fore.YELLOW}{pesanan.id}")
    print(f"{Fore.GREEN}Nama Pelanggan: {Fore.YELLOW}{pesanan.nama}")
    print(f"{Fore.GREEN}Detail: {Fore.YELLOW}{pesanan.detail}")
    
    if pesanan.pengiriman:
        print(f"\n{Fore.WHITE}{Back.BLUE} DAFTAR PENGIRIMAN ".center(50))
        for kirim in pesanan.pengiriman:
            print(f"\n{Fore.GREEN}ID Pengiriman: {Fore.YELLOW}{kirim.id}")
            print(f"{Fore.GREEN}Status: {Fore.YELLOW}{kirim.status}")
            print(f"{Fore.GREEN}Keterangan: {Fore.YELLOW}{kirim.keterangan}")
            print(f"{Fore.GREEN}Tanggal: {Fore.YELLOW}{kirim.tanggal}")
            print(f"{Fore.GREEN}Alamat: {Fore.YELLOW}{kirim.alamat}")
            print(f"{Fore.CYAN}{'-'*50}")
    else:
        print(f"\n{Fore.RED}Belum ada pengiriman untuk pesanan ini.")


def proses_pengiriman():
    try:
        id_pesanan = int(input(f"\n{Fore.GREEN}Masukkan ID Pesanan: {Fore.WHITE}"))
        pesanan = next((pesanan for pesanan in daftar_pesanan if pesanan.id == id_pesanan), None)
        
        if pesanan is None:
            print(f"\n{Fore.RED}Pesanan dengan ID {id_pesanan} tidak ditemukan!")
            return
        
        if not pesanan.pengiriman:
            print(f"\n{Fore.RED}Belum ada pengiriman untuk Pesanan ID {id_pesanan}!")
            return
        
        print(f"\n{Fore.CYAN}{'═'*50}")
        print(f"{Fore.WHITE}{Back.BLUE} PENGIRIMAN TERSEDIA ".center(50))
        print(f"{Fore.CYAN}{'═'*50}")
        
        for kirim in pesanan.pengiriman:
            print(f"{Fore.GREEN}ID Pengiriman: {Fore.YELLOW}{kirim.id}, {Fore.GREEN}Status: {Fore.YELLOW}{kirim.status}")
        
        id_pengiriman = int(input(f"\n{Fore.GREEN}Masukkan ID Pengiriman yang akan diproses: {Fore.WHITE}"))
        pengiriman = next((p for p in pesanan.pengiriman if p.id == id_pengiriman), None)
        
        if pengiriman is None:
            print(f"\n{Fore.RED}Pengiriman dengan ID {id_pengiriman} tidak ditemukan!")
            return
        
        pengiriman.proses_pengiriman()
    except ValueError:
        print(f"\n{Fore.RED}Masukkan ID dalam bentuk angka!")


# Program utama
daftar_pesanan: list[Order] = []

def main():
    while True:
        bersihkan_layar()
        tampilkan_menu()
        
        pilihan = input(f"\n{Fore.GREEN}Masukkan pilihan Anda (1-6): {Fore.WHITE}")
        
        if pilihan == '1':
            pesanan = buat_pesanan()
            daftar_pesanan.append(pesanan)
            input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '2':
            if not daftar_pesanan:
                print(f"\n{Fore.RED}Belum ada pesanan! Silakan buat pesanan terlebih dahulu.")
                input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")
                continue
                
            print(f"\n{Fore.CYAN}{'═'*50}")
            print(f"{Fore.WHITE}{Back.BLUE} DAFTAR PESANAN TERSEDIA ".center(50))
            print(f"{Fore.CYAN}{'═'*50}")
            
            for pesanan in daftar_pesanan:
                print(f"{Fore.GREEN}ID Pesanan: {Fore.YELLOW}{pesanan.id}, {Fore.GREEN}Pelanggan: {Fore.YELLOW}{pesanan.nama}")
            
            try:
                id_pesanan = int(input(f"\n{Fore.GREEN}Masukkan ID Pesanan untuk menambah pengiriman: {Fore.WHITE}"))
                pesanan = next((pesanan for pesanan in daftar_pesanan if pesanan.id == id_pesanan), None)
                
                if pesanan:
                    pengiriman = tambah_pengiriman(pesanan)
                    pesanan.tambah_pengiriman(pengiriman)
                    print(f"\n{Fore.GREEN}✓ Pengiriman berhasil ditambahkan!")
                else:
                    print(f"\n{Fore.RED}Pesanan dengan ID {id_pesanan} tidak ditemukan!")
            except ValueError:
                print(f"\n{Fore.RED}Masukkan ID dalam bentuk angka!")
            
            input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '3':
            lihat_pesanan(daftar_pesanan)
            input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '4':
            lihat_detail_pesanan()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '5':
            proses_pengiriman()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '6':
            print(f"\n{Fore.GREEN}Terima kasih telah menggunakan Sistem Pemesanan dan Pengiriman!")
            break
            
        else:
            print(f"\n{Fore.RED}Pilihan tidak valid! Silakan coba lagi.")
            input(f"\n{Fore.YELLOW}Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()