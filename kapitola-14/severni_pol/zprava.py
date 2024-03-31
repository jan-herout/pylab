import random

random.seed(1)
PISMENA = """ abcdefghijklmnopqrstu"vwxyzěščřžýáíé,.:ň?!ťď;úů"""
SYMBOLY = "@#$%^&*([])"

_MRIZKA = None
_ASDICT = None

ZPRAVA = """První den toho roku, v devět hodin ráno, 
zazvonil u dveří pošťák.
Otevřu balík a v něm: tučňák.
Kdo nám posílá tak zvláštní dárek?

Hledáme na krabici zpáteční adresu. 
Nic.

"Hele!" říká má sestra Amandina. 
"Koukněte!"

"Podivné," říká tatínek.
...
Jsem číslo jedna, 
 dejte mi najíst, 
 až budu mít hlad...
"""


def mrizka() -> str:
    global _MRIZKA
    global _ASDICT
    if _MRIZKA:
        return _MRIZKA
    lines = []
    for s in SYMBOLY:
        mrizka = [c for c in PISMENA]
        random.shuffle(mrizka)
        lines.append(s + "".join(mrizka))
    _MRIZKA = "\n".join(lines)
    _ASDICT = asdict()
    return _MRIZKA


def asdict():
    global _ASDICT

    if _ASDICT:
        return _ASDICT
    lines = mrizka().splitlines()
    slovnik = {}
    for line in lines:
        symbol = line[0]
        preklad = line[1:]
        slovnik[symbol] = preklad
    _ASDICT = slovnik
    return _ASDICT


def _sifruj_radek(radek: str) -> str:
    symbol = random.choice(SYMBOLY)
    klic: str = asdict()[symbol]
    sifra = [symbol]
    for c in radek.lower():
        idx = klic.find(c)
        assert idx > -1, f"nenašel jsem: '{c}'"
        sifra.append(f"{idx:0>2}")
    return " ".join(sifra)


def sifruj(text: str = ZPRAVA) -> str:
    lines = [_sifruj_radek(line) for line in text.splitlines()]
    return "\n".join(lines)


def _desifruj_radek(line: str):
    symbol = line[0]
    rest = [int(num) for num in line[1:].split(" ") if num]
    if not rest:
        return ""
    klic = asdict()[symbol]
    pismena = [klic[idx] for idx in rest]
    return "".join(pismena)


def desifruj(text: str):
    lines = [_desifruj_radek(line) for line in text.splitlines()]
    return "\n".join(lines)


def zprava():
    p1 = mrizka()
    p2 = "-" * (len(PISMENA) + 1)
    p3 = sifruj()

    return "\n".join([p1, p2, p3])


if __name__ == "__main__":
    print(zprava())
