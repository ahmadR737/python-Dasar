class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print(f"{self.nama} bersuara.")


class Burung(Hewan):
    def __init__(self, nama):
        super().__init__(nama)

    # Method baru / override di subclass
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")


burung = Burung("Rio")
burung.suara()
burung.terbang()