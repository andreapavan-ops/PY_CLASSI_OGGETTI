class Pizza:
    def __init__(self, sapore="siciliana", dimensione="grande"):
        self.sapore = sapore
        self.dimensione = dimensione
        self.cotta = False

    def inforna(self):
        self.cotta = True
        print("La pizza è infornata")

    def cuoci(self):
        print("La pizza è cotta")

    def taglia(self):
        print("La pizza è tagliata")

    def descrivi(self):
        print(f"Sapore: {self.sapore}, Dimensione: {self.dimensione}, Cotta: {self.cotta}")


margherita = Pizza("margherita", "media")
margherita.descrivi()
