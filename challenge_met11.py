import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import sys

# Fungsi untuk melakukan preprocessing data
def preprocess_data(file_name):
    try:
        # Membaca dataset
        data = pd.read_csv(file_name)
        print("\nData berhasil dimuat!\n")
        print(data.head())
        
        # Menghapus baris dengan nilai null
        data.dropna(inplace=True)
        print("\nData setelah menghapus baris dengan nilai null:\n")
        print(data.head())
        
        # Encode jika ada kolom kategorikal
        for col in data.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
        
        return data
    except Exception as e:
        print(f"Terjadi kesalahan saat memproses data: {e}")
        sys.exit()

# Fungsi untuk melatih model
def train_model(X, y, algorithm):
    try:
        # Membagi data menjadi data latih dan data uji
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Standarisasi data
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Memilih algoritma
        if algorithm == 'LinearRegression':
            model = LinearRegression()
        elif algorithm == 'RandomForest':
            model = RandomForestRegressor(random_state=42)
        else:
            print("Algoritma tidak dikenali. Pilih antara 'LinearRegression' atau 'RandomForest'.")
            return

        # Melatih model
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        # Evaluasi model
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean Squared Error untuk {algorithm}: {mse}\n")
        return model, mse
    except Exception as e:
        print(f"Terjadi kesalahan saat melatih model: {e}")

# Fungsi utama untuk menjalankan terminal berbasis loop
if __name__ == "__main__":
    while True:
        print("\n=== ANALISIS DATA AIR QUALITY ===")
        print("1. Muat Data dan Lakukan Preprocessing")
        print("2. Latih Model dan Bandingkan Algoritma")
        print("3. Keluar")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            file_name = input("Masukkan nama file (dengan ekstensi .csv): ")
            data = preprocess_data(file_name)

        elif choice == '2':
            if 'data' not in locals():
                print("Harap lakukan preprocessing data terlebih dahulu.")
                continue

            # Pilih kolom target
            target_col = input("Masukkan nama kolom target: ")
            if target_col not in data.columns:
                print("Kolom target tidak ditemukan dalam data.")
                continue

            # Pilih parameter (fitur) untuk pelatihan
            print("Kolom yang tersedia:", list(data.columns))
            features = input("Masukkan kolom fitur yang ingin digunakan (pisahkan dengan koma): ").split(',')
            if not all([f in data.columns for f in features]):
                print("Beberapa kolom fitur tidak valid.")
                continue

            X = data[features]
            y = data[target_col]

            # Melatih model dengan algoritma yang dipilih
            algorithm = input("Masukkan algoritma utama ('LinearRegression' atau 'RandomForest'): ")
            print(f"Melatih model menggunakan {algorithm}...")
            main_model, main_mse = train_model(X, y, algorithm)

            # Analisis menggunakan algoritma lain
            alternate_algo = 'LinearRegression' if algorithm == 'RandomForest' else 'RandomForest'
            print(f"Melakukan analisis dengan algoritma alternatif: {alternate_algo}...")
            _, alt_mse = train_model(X, y, alternate_algo)

            # Membandingkan hasil
            print(f"\nHasil Perbandingan:\n- {algorithm}: MSE = {main_mse}\n- {alternate_algo}: MSE = {alt_mse}\n")

        elif choice == '3':
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")
