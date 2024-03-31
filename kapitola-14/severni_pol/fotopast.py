import random
from textwrap import dedent

from IPython.display import display_markdown

CHOICES = "MMMMMMTTTTTTTTTTTTL"
random.seed(1)


def radek(delka=60):
    return "".join([random.choice(CHOICES) for _ in range(delka)])


def pozorovani(pocet_radek=20) -> str:
    return "\n".join([radek() for _ in range(pocet_radek)])


def _spocitej_zvirata(pozorovani: str):
    """Funkce spočítá medvědy a tuleně pro všechna pozorování.

    Pravidla:
    - Každý řádek je jeden den; tohle bude důležité za chvíli.
    - Lišky (`L`) počítat nechceme, chceme je přeskočit - počítat budeme jen medvědy (`M`) a tuleně (`T`)
    - Medvědi jsou hladoví, a také trpěliví; takže:
    - když **ve stejný den** přijde k fotopasti medvěd
    - a hned po něm přijde k fotopasti tuleň
    - tak ten medvěd toho tuleně sežere (započítáme tedy medvěda, ale nemůžeme započítat tuleně)

    Args:
        pozorovani (str): hodnoty pozorování, každý řádek je jeden den

    Returns:
        dict: klíčem je písmeno které představuje druh, a hodnotou je počet
    """
    zvirata = {
        "M": 0,
        "T": 0,
    }
    for day in pozorovani.splitlines():
        predchozi_zvire = None
        for zvire in day:
            if zvire not in "MT" or (predchozi_zvire == "M" and zvire == "T"):
                continue
            zvirata[zvire] = zvirata[zvire] + 1
    return zvirata


def vyhodnot(pozorovani: str, zvirata: dict[str, int]):
    spravne = _spocitej_zvirata(pozorovani)
    if spravne == zvirata:
        _vyhral()
    else:
        _prohral(spravne)


def _vyhral():
    message = dedent(
        """
        # Výborně!
                     
        To je správný výsledek.
        
        ![medved](./imgs/medved2.jpg)
        """
    )
    display_markdown(message, raw=True)


def _prohral(zvirata: dict):
    message = dedent(
        f"""
        # To se mi nějak nezdá ...
                     
        Čekla bych tohle: {zvirata=}
        
        ![tuleň](./imgs/tulen.jpg)
        """
    )
    display_markdown(message, raw=True)
