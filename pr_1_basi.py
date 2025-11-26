class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def cambia_nome(self, nome):
        self.nome = nome
        return f"{self.nome} {self.cognome}"


p1 = Persona("Mario", "Rossi")
print(p1.nome, '', p1.cognome)

p2 = Persona("Luigi", "Verdi")
print(p2.nome)

p2.cambia_nome("Gianni")
print(p2.nome)

