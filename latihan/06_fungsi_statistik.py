
# Membuat fungsi untuk menghitung rata-rata
def hitung_rata_rata(data):
    total = sum(data)
    banyak_data = len(data)
    return total / banyak_data


# Membuat list nilai mahasiswa
nilai = [75, 80, 65, 90, 88]

# Memanggil fungsi
rata_rata = hitung_rata_rata(nilai)

# Menampilkan hasil
print("Daftar nilai:", nilai)
print("Rata-rata nilai:", rata_rata)
