mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika",
}

mahasiswa.pop("jurusan", None)  # Menghapus dengan key secara aman (tidak error jika key tidak ada)
del mahasiswa["nama"]           # Menghapus dengan del

print(mahasiswa)