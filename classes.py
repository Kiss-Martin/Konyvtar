# Név;Beiratkozás időpontja;Könyv azonosító;Visszahozás időpontja
class kolcsonzo:
    def __init__(self, row: str) -> None:
        data = row.split(';')
        self.nev = data[0]
        self.beiratkozas = data[1]
        self.azonosito = data[2]
        self.visszahozas = data[3]

# Név;Szerző;Kiadás éve;kategória;Kölcsönözve;Azonosí1tó
class konyv:
    def __init__(self, row: str) -> None:
        data = row.split(';')
        self.nev = data[0]
        self.szerzo = data[1]
        self.kiadasEve = data[2]
        self.kategoria = data[3]
        self.kolcsonozve = data[4]
        self.azonosito = data[5]

