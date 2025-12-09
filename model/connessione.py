from dataclasses import dataclass
from datetime import timedelta


@dataclass
class Connessione:
    id: int
    id_rifugio1: int
    id_rifugio2: int
    distanza: int
    difficolta: str
    durata: timedelta
    anno: int


    def __str__(self):
        return self.id, self.id_rifugio1, self.id_rifugio2, self.distanza, self.durata, self.anno

    def __repr__(self):
        return self.id, self.id_rifugio1, self.id_rifugio2, self.distanza, self.durata, self.anno

    def __hash__(self):
        return hash(self.id)
