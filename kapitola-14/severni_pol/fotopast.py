import random

CHOICES = "MMMMMMTTTTTTTTTTTTL"
POZOROVANI = None
random.seed(1)


def radek(delka=60):
    return "".join([random.choice(CHOICES) for _ in range(delka)])


def pozorovani(pocet_radek=20) -> str:
    global POZOROVANI
    if POZOROVANI:
        return POZOROVANI
    POZOROVANI = "\n".join([radek() for _ in range(pocet_radek)])
    return POZOROVANI
