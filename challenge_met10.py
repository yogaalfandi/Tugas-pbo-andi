import mysql.connector

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            user="root",
            host="localhost",
            password="",
            database="penjualan"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

def initialize_db(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS penjualan")
    cursor.execute("USE penjualan")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pegawai (
            NIK CHAR(16) NOT NULL PRIMARY KEY,
            Nama VARCHAR(50),
            Alamat TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produk (
            Kode_Produk CHAR(10) NOT NULL PRIMARY KEY,
            Nama_Produk VARCHAR(50),
            Jenis_Produk VARCHAR(30)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transaksi (
            No_Transaksi CHAR(10) NOT NULL PRIMARY KEY,
            Detail_Transaksi VARCHAR(50)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Struk (
            No_Transaksi CHAR(10) NOT NULL,
            Nama_Pegawai VARCHAR(50),
            Nama_Produk VARCHAR(50),
            Jumlah_Produk INT,
            Total_Harga DECIMAL(15, 2),
            FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi)
        )
    """)

def show_transactions(cursor):
    cursor.execute("""
        SELECT 
            Transaksi.No_Transaksi,
            Transaksi.Detail_Transaksi
        FROM Transaksi
    """)
    result = cursor.fetchall()
    if result:
        print("\nData Transaksi:")
        for row in result:
            print(f"No Transaksi: {row[0]}, Detail: {row[1]}")
    else:
        print("\nTidak ada data transaksi.")

def insert_data(cursor, conn, table, data):
    try:
        cursor.execute(f"INSERT INTO {table} VALUES ({', '.join(['%s'] * len(data))})", data)
        conn.commit()
        print(f"Data berhasil ditambahkan ke tabel {table}.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_data(cursor, conn, table):
    try:
        column_to_update = input("Masukkan kolom yang ingin diubah: ").strip()
        new_value = input(f"Masukkan nilai baru untuk {column_to_update}: ")

        condition_column = input("Masukkan kolom untuk kondisi: ").strip()
        condition_value = input(f"Masukkan nilai untuk kondisi pada {condition_column}: ")

        query = f"UPDATE {table} SET {column_to_update} = %s WHERE {condition_column} = %s"
        cursor.execute(query, (new_value, condition_value))
        conn.commit()

        print(f"Data pada tabel {table} berhasil diubah.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_data(cursor, conn, table):
    try:
        condition_column = input("Masukkan kolom untuk kondisi: ").strip()
        condition_value = input(f"Masukkan nilai untuk kondisi pada {condition_column}: ")

        query = f"DELETE FROM {table} WHERE {condition_column} = %s"
        cursor.execute(query, (condition_value,))
        conn.commit()

        print(f"Data dari tabel {table} berhasil dihapus.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    conn = connect_to_db()
    cursor = conn.cursor()
    initialize_db(cursor)

    while True:
        print("\n=== Sistem Penjualan ===")
        print("1. Tampilkan Data Transaksi")
        print("2. Input Pegawai")
        print("3. Input Produk")
        print("4. Input Transaksi dan Struk")
        print("5. Ubah Data")
        print("6. Hapus Data")
        print("0. Keluar")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            show_transactions(cursor)

        elif pilihan == "2":
            data = (
                input("Masukkan NIK Pegawai: "),
                input("Masukkan Nama Pegawai: "),
                input("Masukkan Alamat Pegawai: ")
            )
            insert_data(cursor, conn, "Pegawai", data)

        elif pilihan == "3":
            data = (
                input("Masukkan Kode Produk: "),
                input("Masukkan Nama Produk: "),
                input("Masukkan Jenis Produk: ")
            )
            insert_data(cursor, conn, "Produk", data)

        elif pilihan == "4":
            transaksi_data = (
                input("Masukkan Nomor Transaksi: "),
                input("Masukkan Detail Transaksi: ")
            )
            insert_data(cursor, conn, "Transaksi", transaksi_data)

            struk_data = (
                transaksi_data[0],
                input("Masukkan Nama Pegawai: "),
                input("Masukkan Nama Produk: "),
                int(input("Masukkan Jumlah Produk: ")),
                float(input("Masukkan Total Harga: "))
            )
            insert_data(cursor, conn, "Struk", struk_data)

        elif pilihan == "5":
            table = input("Masukkan nama tabel yang ingin diubah: ").capitalize()
            update_data(cursor, conn, table)

        elif pilihan == "6":
            table = input("Masukkan nama tabel yang ingin dihapus: ").capitalize()
            delete_data(cursor, conn, table)

        elif pilihan == "0":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    conn.close()
    print("Koneksi ke database ditutup.")

if __name__ == "__main__":
    main()
