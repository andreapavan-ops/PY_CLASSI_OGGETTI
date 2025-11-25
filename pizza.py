
'''Compito**: Crea una classe `Pizza` con:
- Attributi: `sapore`, `dimensione`, `cotta` (True/False)
- Metodi: `inforna()` (mette `cotta` a True), `taglia()` (stampa "Pizza tagliata"), `descrivi()` (stampa una sapore + dimensione)


rea una classe `Pizza` con:

- Attributi: `sapore`, `dimensione`, `cotta` (True/False)

'''


# 1. Definisco una classe pizza
class Pizza:
    sapore= "siciliana"
    dimensione= "grande" 
    cotta= False

    def inforna (self):
        self.cotta = True
        print("La pizza è infornata")

    def cuoci(self):
        print ("La pizza è cotta")

    def taglia(self):
        print ("La pizza è tagliata")

siciliana = Pizza()

margherita = Pizza()
margherita.sapore = margherita 

def descrivi(self):
        print(f"Sapore: {self.sapore}, Dimensione: {self.dimensione}, Cotta: {self.cotta}")





