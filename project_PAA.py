import random
import time
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan array acak
def generate_array(n, max_value):
    random.seed(42)  # Menetapkan seed untuk data yang konsisten
    return [random.randint(1, max_value) for _ in range(n)]

# Fungsi untuk memeriksa apakah elemen dalam array unik
def check_uniqueness(arr):
    return len(arr) == len(set(arr))  # Jika panjang array sama dengan panjang set, maka unik

# Fungsi untuk menghitung waktu untuk worst case dan average case
def calculate_performance(n, max_value):
    arr = generate_array(n, max_value)

    # Worst case (menggunakan data yang sangat besar atau banyak duplikat)
    worst_case = time.time()
    check_uniqueness(arr)
    worst_case = time.time() - worst_case

    # Average case (menggunakan data acak)
    average_case = time.time()
    check_uniqueness(arr)
    average_case = time.time() - average_case

    return worst_case, average_case

# Daftar ukuran array yang akan diuji
sizes = [100, 150, 200, 250, 300, 350, 400, 500]
results = {}

# Hitung worst case dan average case untuk setiap ukuran array
for n in sizes:
    max_value = 250 - 3  # Nilai maksimum untuk array (250 - 3 digit terakhir stambuk)
    worst_case, average_case = calculate_performance(n, max_value)
    results[n] = (worst_case, average_case)

# Simpan hasil ke dalam file worst_avg.txt
with open('worst_avg.txt', 'w') as f:
    for n, (worst, avg) in results.items():
        f.write(f"{n}: Worst case: {worst:.6f} sec, Average case: {avg:.6f} sec\n")

# Menyimpan grafik dalam format jpg
n_values = list(results.keys())
worst_times = [results[n][0] for n in n_values]
average_times = [results[n][1] for n in n_values]

# Plot grafik
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_times, label='Worst Case', marker='o')
plt.plot(n_values, average_times, label='Average Case', marker='x')
plt.xlabel('Ukuran Array (n)')
plt.ylabel('Waktu (detik)')
plt.title('Worst Case vs Average Case untuk Ukuran Array yang Berbeda')
plt.legend()
plt.grid(True)
plt.savefig('performance_plot.jpg')  # Menyimpan plot dalam format JPG
