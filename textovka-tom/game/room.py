from dataclasses import dataclass


@dataclass
class Mistnost:
    jmeno: str
    popis: str
    vychody: list[str]


M_START = Mistnost(
    jmeno="start",
    popis="Začátek tvého dobrodružství.",
    vychody=["les"],
)

M_LES = Mistnost(
    jmeno="les",
    popis="Vešel jsi do lesa.",
    vychody=["start"],
)
