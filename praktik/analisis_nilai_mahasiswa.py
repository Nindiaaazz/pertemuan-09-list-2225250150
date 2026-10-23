
# Program Analisis Nilai Mahasiswa

# Fungsi untuk menghitung rata-rata
def hitung_rata_rata(data):
    return sum(data) / len(data)


# Fungsi untuk menentukan kelulusan
def analisis_kelulusan(data):
    lulus = []

    for nilai in data:
        if nilai >= 60:
            lulus.append(nilai)

    return lulus


# Data nilai mahasiswa (minimal 10 data)
nilai_mahasiswa = [75, 80, 45, 90, 55, 88, 60, 70, 50, 95]

# Menghitung statistik nilai
total = sum(nilai_mahasiswa)
rata_rata = hitung_rata_rata(nilai_mahasiswa)
tertinggi = max(nilai_mahasiswa)
terendah = min(nilai_mahasiswa)

# Menganalisis kelulusan
nilai_lulus = analisis_kelulusan(nilai_mahasiswa)
jumlah_lulus = len(nilai_lulus)
jumlah_tidak_lulus = len(nilai_mahasiswa) - jumlah_lulus

# Menampilkan laporan
print("=== ANALISIS NILAI MAHASISWA ===")
print("Daftar nilai:", nilai_mahasiswa)
print("Jumlah data:", len(nilai_mahasiswa))
print("Total nilai:", total)
print("Rata-rata nilai:", rata_rata)
print("Nilai tertinggi:", tertinggi)
print("Nilai terendah:", terendah)
print("Jumlah mahasiswa lulus:", jumlah_lulus)
print("Jumlah mahasiswa tidak lulus:", jumlah_tidak_lulus)
print("Daftar nilai yang lulus:", nilai_lulus)
