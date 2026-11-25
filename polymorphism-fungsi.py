class Kucing:
    def suara(self):
        return "Meong!"


class Anjing:
    def suara(self):
        return "Guk guk!"


def cetak_suara(hewan):
    print(hewan.suara())


cetak_suara(Kucing())
cetak_suara(Anjing())