import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk menghitung BMI
def hitung_bmi():
    try:
        # Mengambil input berat dan tinggi dari pengguna
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get()) / 100  # Konversi tinggi dari cm ke meter

        # Validasi nilai input
        if berat <= 0 or tinggi <= 0:
            messagebox.showerror("Kesalahan Input", "Berat dan tinggi harus lebih dari 0!")
            return

        # Menghitung BMI
        bmi = berat / (tinggi ** 2)

        # Menentukan kategori BMI dan warna hasil
        if bmi < 18.5:
            status = "Kekurangan Berat Badan"
            warna = "blue"
        elif 18.5 <= bmi < 24.9:
            status = "Berat Badan Normal"
            warna = "green"
        elif 25 <= bmi < 29.9:
            status = "Kelebihan Berat Badan"
            warna = "orange"
        else:
            status = "Obesitas"
            warna = "red"

        # Menampilkan hasil dengan warna sesuai kategori
        label_hasil.config(
            text=f"Indeks BMI Anda: {bmi:.2f}\nKategori: {status}",
            foreground=warna
        )

        # Menampilkan notifikasi sukses
        messagebox.showinfo("Sukses", "Perhitungan BMI berhasil!")


    except ValueError:
        messagebox.showerror("Kesalahan Input", "Masukkan angka yang valid untuk berat dan tinggi!")

# Fungsi untuk mereset input dan hasil
def reset():
    entry_berat.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)
    label_hasil.config(text="Indeks BMI Anda:\nKategori:", foreground="black")

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Indeks Massa Tubuh (BMI)")

# Tema untuk input lebih modern
style = ttk.Style()
style.theme_use("clam")  # Menggunakan tema modern

# Informasi awal
messagebox.showinfo(
    "Selamat Datang!",
    "Masukkan berat badan dalam kilogram (kg) dan tinggi badan dalam sentimeter (cm). Klik 'Hitung BMI' untuk mendapatkan hasil."
)

# Frame utama untuk tata letak
frame_input = ttk.Frame(root, padding="20")
frame_input.pack(pady=20)

# Label dan Entry untuk berat badan
ttk.Label(frame_input, text="Berat Badan (kg):", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_berat = ttk.Entry(frame_input, width=20, font=("Arial", 11))
entry_berat.grid(row=0, column=1, padx=10, pady=10)
entry_berat.insert(0, "70")  # Placeholder berat

# Label dan Entry untuk tinggi badan
ttk.Label(frame_input, text="Tinggi Badan (cm):", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_tinggi = ttk.Entry(frame_input, width=20, font=("Arial", 11))
entry_tinggi.grid(row=1, column=1, padx=10, pady=10)
entry_tinggi.insert(0, "170")  # Placeholder tinggi

# Tombol untuk menghitung BMI
btn_hitung = ttk.Button(root, text="Hitung BMI", command=hitung_bmi)
btn_hitung.pack(pady=10)

# Tombol untuk reset
btn_reset = ttk.Button(root, text="Reset", command=reset)
btn_reset.pack(pady=5)

# Label hasil untuk menampilkan BMI
label_hasil = ttk.Label(root, text="Indeks BMI Anda:\nKategori:", font=("Arial", 12), anchor="center", justify="center")
label_hasil.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
