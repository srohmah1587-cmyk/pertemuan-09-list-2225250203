
def rata_rata(data):
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    return [n for n in data if n >= batas]


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menggunakan fungsi
rata = rata_rata(nilai)
lulus = nilai_lulus(nilai)

# Menampilkan ringkasan
print("Daftar nilai:", nilai)
print("Rata-rata nilai:", rata)
print("Nilai yang lulus:", lulus)
print("Jumlah siswa lulus:", len(lulus))
print("Jumlah siswa tidak lulus:", len(nilai) - len(lulus))