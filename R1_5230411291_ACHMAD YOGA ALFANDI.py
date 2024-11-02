class Pegawai:
    def __init__(self, id_pegawai, nama, alamat):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.alamat = alamat
    
    def tampilkan_info(self):
        return f"Pegawai: {self.nama} (ID: {self.id_pegawai})"

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        
    def hitung_harga(self):
        pass
    
    def tampilkan_info(self):
        return f"Produk: {self.nama_produk} (Kode: {self.kode_produk})"

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Snack")
        self.harga = harga
    
    def hitung_harga(self):
        # Override dengan logika harga khusus snack
        return self.harga * 1.1  # Markup 10% untuk snack
    
    def tampilkan_info(self):
        # Override method tampilkan
        return f"Snack: {self.nama_produk} - Rp{self.harga:,.2f}"

class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, "Makanan")
        self.harga = harga
    
    def hitung_harga(self):
        # Override dengan logika harga khusus makanan
        return self.harga * 1.15  # Markup 15% untuk makanan
    
    def tampilkan_info(self):
        # Override method tampilkan
        return f"Makanan: {self.nama_produk} - Rp{self.harga:,.2f}"

class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, "Minuman")
        self.harga = harga
    
    def hitung_harga(self):
        # Override dengan logika harga khusus minuman
        return self.harga * 1.2  # Markup 20% untuk minuman
    
    def tampilkan_info(self):
        # Override method tampilkan
        return f"Minuman: {self.nama_produk} - Rp{self.harga:,.2f}"

class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi

class Struk:
    def __init__(self, no_transaksi, nama_pegawai, no_struk, nama_produk, jumlah_produk):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.no_struk = no_struk
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = 0
    
    def hitung_total(self, harga_produk):
        self.total_harga = self.jumlah_produk * harga_produk
        return self.total_harga

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat beberapa produk
    snack1 = Snack("S001", "Keripik Kentang", 10000)
    makanan1 = Makanan("M001", "Nasi Goreng", 25000)
    minuman1 = Minuman("D001", "Es Teh", 5000)
    
    # Menampilkan informasi produk dengan method yang sudah di-override
    print("\nInformasi Produk:")
    print(snack1.tampilkan_info())
    print(f"Harga jual: Rp{snack1.hitung_harga():,.2f}")
    
    print("\n" + makanan1.tampilkan_info())
    print(f"Harga jual: Rp{makanan1.hitung_harga():,.2f}")
    
    print("\n" + minuman1.tampilkan_info())
    print(f"Harga jual: Rp{minuman1.hitung_harga():,.2f}")
    
    # Membuat transaksi
    pegawai1 = Pegawai("P001", "Budi Santoso", "Jl. Merdeka No. 123")
    struk1 = Struk("T001", pegawai1.nama, "STR001", makanan1.nama_produk, 2)
    total = struk1.hitung_total(makanan1.hitung_harga())
    
    print("\nInformasi Transaksi:")
    print(f"No. Struk: {struk1.no_struk}")
    print(f"Pegawai: {struk1.nama_pegawai}")
    print(f"Produk: {struk1.nama_produk}")
    print(f"Jumlah: {struk1.jumlah_produk}")
    print(f"Total Harga: Rp{total:,.2f}")