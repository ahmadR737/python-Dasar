class AkunBank:
    def __init__(self, nama, alamat, saldo_awal):
        self.nama = nama          # 1. Public: bisa diakses dari mana saja
        self._alamat = alamat     # 2. Protected (_): konvensi untuk internal/subclass
        self.__saldo = saldo_awal # 3. Private (__): name mangling (_AkunBank__saldo)

    # Getter untuk membaca data private secara aman
    def lihat_saldo(self):
        return self.__saldo

    # Setter untuk mengubah data private dengan validasi
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor Rp{jumlah} berhasil.")
        else:
            print("Jumlah setor harus lebih dari 0.")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik Rp{jumlah} berhasil.")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid.")


class TabunganMahasiswa(AkunBank):
    def info_singkat(self):
        # Subclass masih bisa mengakses public dan protected
        return f"{self.nama} - Alamat: {self._alamat}"


# --- Penggunaan ---
akun = TabunganMahasiswa("Budi", "Jl. Merdeka No. 10", 500000)

# 1. Public
print("Nama:", akun.nama)
akun.nama = "Budi Santoso"
print("Nama baru:", akun.nama)

# 2. Protected (bisa diakses, tapi sebaiknya lewat subclass / dihindari dari luar)
print("Info:", akun.info_singkat())
print("Alamat (protected):", akun._alamat)

# 3. Private (tidak bisa langsung diakses dengan akun.__saldo)
print("Saldo awal:", akun.lihat_saldo())
akun.setor(250000)
akun.tarik(100000)
print("Saldo akhir:", akun.lihat_saldo())

# Mencoba akses langsung __saldo akan menimbulkan AttributeError:
# print(akun.__saldo)