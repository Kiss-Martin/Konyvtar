class kolcsonzok:
    def __init__(self, row: str) -> None:
        data = row.split(';')
        self.name = data[0]
        self.module = data[1]
        self.time = data[2]
        self.percent = data[3]