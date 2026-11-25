# Menulis file
with open("hello.py", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("hello.py", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("hello.py", "r") as file:
    for baris in file:
        print(baris.strip())
