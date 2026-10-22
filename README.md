# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A

## Tujuan

Mengolah kumpulan data numerik menggunakan list Python, memahami penggunaan indeks, serta menerapkan fungsi untuk menghitung rata-rata, menentukan nilai minimum dan maksimum, dan menghitung jumlah mahasiswa yang lulus berdasarkan batas kelulusan.

## Struktur Program

Program pada pertemuan ini terdiri dari file latihan dan file praktik.

### 1. File Latihan

File latihan digunakan untuk mempelajari konsep dasar list Python, meliputi:
- Membuat dan menyimpan kumpulan data numerik dalam list.
- Mengakses elemen list menggunakan indeks.
- Menghitung jumlah dan banyaknya data.
- Menentukan nilai minimum dan maksimum.
- Menggunakan perulangan dan fungsi untuk mengolah data.

### 2. File Praktik

File `praktik/analisis_nilai_mahasiswa.py` digunakan untuk menganalisis data nilai mahasiswa.

Program menggunakan beberapa fungsi, yaitu:
- `rata_rata(data)` untuk menghitung nilai rata-rata dan menangani list kosong agar tidak terjadi kesalahan pembagian dengan nol.
- `nilai_lulus(data, batas=60)` untuk menentukan mahasiswa yang memperoleh nilai lebih besar atau sama dengan batas kelulusan.
- Fungsi bawaan `min()` dan `max()` untuk menentukan nilai minimum dan maksimum.

Hasil pengolahan data ditampilkan dalam bentuk ringkasan yang mudah dipahami.

## Cara Menjalankan

Jalankan program melalui terminal menggunakan perintah berikut:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Pastikan terminal berada di direktori utama repository sebelum menjalankan perintah tersebut.

## Test Case Wajib

Pengujian dilakukan untuk memastikan fungsi dapat mengolah data numerik dengan benar, menentukan kelulusan, serta menangani list kosong.

| No. | Data yang Diperiksa | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `[60, 70, 80]` – Rata-rata | 70.00 | 70.00 | Berhasil |
| 2 | `[60, 70, 80]` – Minimum / maksimum | 60 / 80 | 60 / 80 | Berhasil |
| 3 | `[60, 70, 80]` – Jumlah lulus | 3 mahasiswa | 3 mahasiswa | Berhasil |
| 4 | `[59, 60, 61]` – Batas kelulusan 60 | 2 mahasiswa lulus | 2 mahasiswa lulus | Berhasil |
| 5 | `[]` – Penanganan list kosong pada fungsi rata-rata | Tidak error | Tidak error | Berhasil |

## Refleksi

Melalui praktikum ini, saya memahami bahwa list Python dapat digunakan untuk menyimpan dan mengolah banyak data numerik dalam satu variabel. Saya juga memahami bahwa indeks list dimulai dari 0, sehingga setiap elemen dapat diakses berdasarkan posisinya.

Selain itu, saya belajar menggunakan fungsi untuk menghitung rata-rata, menentukan nilai minimum dan maksimum, serta menghitung jumlah mahasiswa yang lulus berdasarkan batas nilai tertentu.

Salah satu kesalahan yang berhasil diperbaiki adalah penanganan list kosong ketika menghitung rata-rata. Jika list kosong langsung dibagi dengan jumlah elemennya, program dapat mengalami `ZeroDivisionError`. Kesalahan tersebut dapat diatasi dengan memeriksa apakah list kosong sebelum melakukan pembagian. Dengan demikian, program menjadi lebih aman dan dapat menangani berbagai kondisi data.