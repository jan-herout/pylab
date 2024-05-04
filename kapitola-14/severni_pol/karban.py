import random
from textwrap import dedent
from typing import Callable

from IPython.display import display_markdown

VYSKA = "12345789AKQJ"
BARVY = "červená,kárová,listy,kříže".split(",")

SHUFFLED_DECK = [
    "2:červená",
    "K:kárová",
    "5:kříže",
    "8:kříže",
    "4:červená",
    "A:listy",
    "1:listy",
    "1:kárová",
    "5:listy",
    "1:kříže",
    "9:kříže",
    "5:červená",
    "4:kříže",
    "K:listy",
    "7:kříže",
    "J:kříže",
    "Q:červená",
    "Q:kříže",
    "4:kárová",
    "9:kárová",
    "9:listy",
    "2:listy",
    "3:listy",
    "7:červená",
    "1:červená",
    "3:kříže",
    "7:kárová",
    "Q:listy",
    "7:listy",
    "J:červená",
    "3:červená",
    "K:kříže",
    "K:červená",
    "4:listy",
    "8:červená",
    "A:červená",
    "2:kříže",
    "8:kárová",
    "8:listy",
    "2:kárová",
    "3:kárová",
    "5:kárová",
    "A:kárová",
    "A:kříže",
    "J:listy",
    "9:červená",
    "J:kárová",
    "Q:kárová",
]


DECK = sorted(SHUFFLED_DECK)


def zbyvajici_karty(vytazene_karty: list[str]) -> list[str]:
    """
    Funkce vrací informaci o tom, které karty nebyly zatím z balíčku vytažené.

    Vstupy:
        karty (list[str]): seznam karet, které jsou vytažené

    Returns:
        list[str]: seznam karet, které ještě vytažené nebyly
    """
    # založímé prázdný objekt typu dict
    # klíčem bude karta, a hodnota bude buď True, nebo False
    # pokud True, znamená to, že tahle karta byla z balíčku vytažená
    # pokud False, znamená to, že jsme jí z něj ještě nevytáhli
    karty = {}

    # pro každou kartu, která je v balíčku, si do něj založíme informaci, že
    # vytažená ještě nebyla
    for karta in DECK:
        karty[karta] = False  # tahle karta ještě z balíčku vytažená nebyla

    # tohle napiš ty: pro každou kartu z vytazene_karty změň hodnoty
    # v dictionary karty na true (karty[vytazena_karta] = True)
    for karta in vytazene_karty:
        karty[karta] = True

    # tohle napiš ty: pro každý klíč a hodnotuitems()) z dictionary karty
    # pokud je hodnota False, doplň kartu na konec listu zbyva
    zbyva = []
    for karta, vytazena in karty.items():
        if vytazena:
            continue
        zbyva.append(karta)

    # vracíme seznam zbývajících karet
    return zbyva


def je_to_spravne(vytazene_karty: list[str], func: Callable):
    got = func(vytazene_karty)
    wanted = zbyvajici_karty(vytazene_karty)
    if wanted == got:
        _vyhral()
    else:
        _prohral(wanted)


def _vyhral():
    message = dedent(
        """
        # Výborně!
                     
        To je správný výsledek.
        
        ![medved](./imgs/joker-good.png)
        """
    )
    display_markdown(message, raw=True)


def _prohral(wanted):
    message = dedent(
        f"""
        # To se mi nějak nezdá ...
                     
        Čekla bych tohle: {wanted=}
        
        ![tuleň](./imgs/joker-bad.png)
        """
    )
    display_markdown(message, raw=True)
