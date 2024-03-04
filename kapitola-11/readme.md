- [Základní typy cyklů v programu](#základní-typy-cyklů-v-programu)
  - [Cyklus for](#cyklus-for)
  - [Operátor range](#operátor-range)
  - [Cyklus while](#cyklus-while)
  - [Klíčové slovo continue](#klíčové-slovo-continue)
  - [Klíčové slovo break](#klíčové-slovo-break)

# Základní typy cyklů v programu

V programech velmi často narazíš na situaci, kdy je potřeba nějakou akci opakovat. A to
buď pro určitý počet prvků v nějakém seznamu (cyklus `for`, _pro_ _každý_ prvek), 
nebo dokud je nějaká podmínka splněná (cyklus `while` - _dokud_ podmínka platí, 
něco _dělej_)

## Cyklus for

Na cyklus `for` jsi už narazil. Cyklus projde něco, co se dá iterovat (nějaký kontejner),
a postupně pro každý z prvků toho kontejneru něco udělá.

Například:

```python
# string je kontejner
for pismeno in "abcd":
    print(pismeno)
```

Nebo:

```python
# list je kontejner
seznam = [ "nula", 1, 2, "tři" ]
for cislo in seznam:
    print(cislo)
```

## Operátor range

Co když potřebuješ získat seznam čísel od jedné do stovky?
Možná by tě napadlo něco jako:

```python
seznam = [1, 2, 3, 4, 5, 6, ...] # a tak dál, až do stovky
```

Asi by tě to ale docela rychle přestalo bavit, brzo by ti došla trpělivost.

Přesně k tomu ale v Pythonu slouží operátor `range` (rozsah čísel).

```python
# od jedničky dál; 101 je první číslo, které nechceme
jedna_az_sto = range(1, 101) 

# když zadáš jen jedno číslo, má se a to, že počítáš od nuly dál,
# a zadané číslo je první, které nedostaneme zpátky
od_nuly_do_deviti = range(10) 
```

K čemu je to dobré? Dejme tomu, že chceš sečíst všechna čísla od 1 to 1000. Jak na to?

Například takhle (pro šťouraly: jasně, tohle není nejlepší způsob jak na to, ale 
demonstruje k čemu je dobrý operátor `range`)

**Vyzkoušej si to.**

```python
soucet = 0
for i in range(1,1000):
    soucet = soucet + i
print(soucet)
```

Ještě bych měl napsat jednu věc: operátor range ve skutečnosti **nevytváří** list.
Vytváří **iterátor**, který umožňuje projít čísla v daném rozsahu od začátku do konce.

Můžeme to demonstrovat třeba takhle (vyzkoušej si to).

```python
rozsah_hodnot = range(3)
print(rozsah_hodnot)
```

Pokud se nepletu, vidíš na výstupu něco jako:

> range(0, 3)

Pokud bys **opravdu trval na tom**, že chceš dostat seznam hodnot, a ne iterátor, můžeš 
si vynutit jeho vytvoření takhle (vyzkoušej si to).

```python
rozsah_hodnot = range(3)
seznam_hodnot = list(range(3))
print(rozsah_hodnot, seznam_hodnot)
```

**POZOR:** není dobrý nápad vytvářet list tam, kde ti stačí iterátor, tj tam, kde pouze
potřebuješ projít seznamem hodnot (čísel) od nějaké spodní meze, po horní mez. 

## Cyklus while

Cyklus `while` použiješ tam, kde chceš něco dělat, dokud je splněná určitá podmínka.
Tak například: mám senzor, který má za úkol detekovat přítomnost myši. Dokud se myš
neobjeví, čekáme. Až se objeví, máme jí chytit do pasti.

```python
import random

def detekovana_mys():
    i = random.randint(0,10)
    print(i, end=" ")
    return i == 10

# dokud NENÍ detekována myš, čekej
while not detekovana_mys():
    print("čekej...")

# ... sklapla past ....
print("Máme jí!")
```

## Klíčové slovo continue

## Klíčové slovo break

