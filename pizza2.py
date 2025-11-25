class Pizza:
    sapore = "siciliana"
    dimensione = "grande" 
    cotta = False

    def inforna(self):
        self.cotta = True
        print("La pizza è infornata")

    def cuoci(self):
        print("La pizza è cotta")

    def taglia(self):
        print("La pizza è tagliata")

    def descrivi(self):
        print(f"Sapore: {self.sapore}, Dimensione: {self.dimensione}, Cotta: {self.cotta}")


siciliana = Pizza()

margherita = Pizza()
margherita.sapore = "margherita"

margherita.descrivi()