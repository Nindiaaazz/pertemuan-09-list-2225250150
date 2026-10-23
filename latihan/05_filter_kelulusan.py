
# Membuat list nilai mahasiswa
nilai = [75, 80, 45, 90, 55, 88, 60, 50]

# Menyaring nilai yang lulus
lulus = []

for angka in nilai:
    if angka >= 60:
        lulus.append(angka)

# Menampilkan hasil
print("Semua nilai:", nilai)
print("Nilai lulus:", lulus)
print("Jumlah mahasiswa lulus:", len(lulus))
print("Jumlah mahasiswa tidak lulus:", len(nilai) - len(lulus))
