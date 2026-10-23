
# Membuat list nilai mahasiswa
nilai = [75, 80, 65, 90, 88]

# Mengubah nilai pada indeks ke-1
nilai[1] = 85
print("Setelah diubah:", nilai)

# Menambahkan nilai di akhir list
nilai.append(95)
print("Setelah ditambah:", nilai)

# Menyisipkan nilai pada indeks ke-2
nilai.insert(2, 70)
print("Setelah disisipkan:", nilai)

# Menghapus nilai 65
nilai.remove(65)
print("Setelah dihapus:", nilai)
