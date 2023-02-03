
class Gomba:

    def __init__(self, lista) -> None:
        if len(lista) == 3:
            self.nev, self.nemzettseg, self.evszak = lista
        else:
            raise Exception("Hibás értékek!")

        def __str__(self):
            return f"{self.nev} {self.nemzettseg} {self.evszak}"


class Gombak:
    def __init__(self, fajlnev) -> None:
        self.lista = []

        fh = open(fajlnev, "r", encoding="utf-8")
        sorok = fh.read().split("\n")
        fh.close()
        i = 1
        while i < len(sorok):
            adat = sorok[i].split("@")
            self.lista.append(Gomba(adat))
            i += 1

    def gombak_szama(self):
        return len(self.lista)

    def papsapka(self):
        i = 0
        while i < len(self.lista):
            if (self.lista[i].nemzettseg.rstrip() == "papsapkagombák"):
                return self.lista[i]
            i += 1

    def tinoru(self):
        i = 0
        db = 0
        while i < len(self.lista):
            if (self.lista[i].nemzettseg.rstrip() == "tinóru"):
                db += 1
            i += 1
        return db