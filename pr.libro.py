# 1. Definisco una classe
class Libro:
    titolo = "Titolo sconosciuto"
    autore = "Autore sconosciuto"
    pagine = 0

    def descrivi(self):
        print(f"{self.titolo} di {self.autore} ({self.pagine} pagine)")

# 2. Creo un oggetto (istanza della classe)
libro1 = Libro()

# 3. Accedo agli attributi
print(libro1.titolo)  # Output: Titolo sconosciuto

# 4. Modifico gli attributi
libro1.titolo = "Il Signore degli Anelli"
libro1.autore = "J.R.R. Tolkien"
libro1.pagine = 1200

# 5. Uso i metodi
libro1.descrivi()  # Output: Il Signore degli Anelli di J.R.R. Tolkien (1200 pagine)

# 6. Creo un altro oggetto - non è influenzato dal primo
libro2 = Libro()
print(libro2.titolo)  # Output: Titolo sconosciuto (valori di default)