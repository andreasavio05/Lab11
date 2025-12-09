from dataclasses import dataclass

@dataclass
class Rifugio:
    id: int
    nome: str
    localita: str
    altitudine: int
    capienza: int
    aperto: int


    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'{self.nome} {self.localita} {self.capienza} {self.aperto}'

    def __hash__(self):
        return hash(self.id)