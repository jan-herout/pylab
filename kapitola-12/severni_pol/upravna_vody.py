import random

from IPython.display import display_markdown

_vstupni_mereni = None

VYHRA = """
# Správně!

![rajcata](./imgs/dobra-rajcata.png)
"""

PROHRA = """
# Špatně!

![rajcata](./imgs/plesniva-rajcata.png)
"""


def _jedno_mereni(i):
    random.seed(i)
    prvek = random.choice("abcdefghijklmnopqrstuvwxyz")
    cislo = str(random.randint(10, 99))
    znamenko = random.choice(["", "+", "-"])
    return prvek + cislo + znamenko


def pust_vodu_a_ziskej_mereni():
    global _vstupni_mereni
    if _vstupni_mereni:
        return _vstupni_mereni
    _vstupni_mereni = "".join([_jedno_mereni(i) for i in range(500)]) + "w00"

    return _vstupni_mereni


def spust_upravnu(instrukce: list[list[str, str, str]]):
    wanted = _spravne_instrukce(_vstupni_mereni)
    if wanted == instrukce:
        display_markdown(VYHRA, raw=True)
        return

    display_markdown(PROHRA, raw=True)


def _spravne_instrukce(vstup: str | None = None):
    if vstup:
        vstupni_text = vstup
    else:
        vstupni_text = _vstupni_mereni

    seznam = []
    i = 0

    while i < len(vstupni_text):
        # získej trojici prvek, hodnota, měření
        prvek = vstupni_text[i]
        hodnota = vstupni_text[i + 1 : i + 3]

        offset_znamenko, znamenko = i + 3, None
        if i + 3 < len(vstupni_text):
            znamenko = vstupni_text[offset_znamenko]

        # pokud nemáš znaménko, pokračuj
        if not znamenko or znamenko not in "+-":
            i = i + 3
            continue

        # sestav měření
        if znamenko == "+":
            jedna_instrukce = [prvek.upper(), hodnota, znamenko]
        else:
            jedna_instrukce = [prvek, hodnota, "+"]

        seznam.append(jedna_instrukce)
        i = i + 4
    return seznam
