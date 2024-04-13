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

Jaký je v tom rozdíl?

Iterátor je něco, co ví, jak vytvořit další prvek, ale dokud ho nepotřebuješ, tak ten
prvek neexistuje.

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
import time

def detekovana_mys():
    i = random.randint(0,10)
    print(i, end=" ")
    return i == 10

# dokud NENÍ detekována myš, čekej
while not detekovana_mys():
    print("čekej...")
    # jak dlouho chceme čekat?
    time.sleep(0.3) 

# ... sklapla past ....
print("Máme jí!")
```

## Klíčové slovo continue

Občas se můžeš dostat do situace, kdy na základě splnění nějaké podmínky chceš
přeskočit zbytek cyklu, a pokračovat další hodnotou cyklu. K tomu slouží klíčové
slovo [continue](https://docs.python.org/3/reference/simple_stmts.html#continue).

Například:

- mám list, a v něm je seznam nějakých hodnot
- chci listem projít, a na konci chci mít k dispozici součet všech čísel v listu

V příkladu uvedeném níže je uvedené ještě jedna funkce, kterou jsi zatím neviděl.

Jde o funkci [isinstance](https://docs.python.org/3/library/functions.html#isinstance):

`isinstance(h, int)`:

- první argument je testovaná hodnota (`h`)
- druhý argument je datový typ (třída: `int`) - a pokud hodnota je tohoto typu, 
  funkce vrací `True`


```python
hodnoty = [ "a", [ None ], None, 10, 11, 12 , "d"]
soucet = 0
for h in hodnoty:
    if not isinstance(h, int):
        print("Tohle není číslo:", h, "; je to", type(h))
        # protože chceme sčítat pouze čísla, tuhle hodnotu přeskočíme
        continue
    soucet = soucet + h

print("Součet čísel je", soucet)
```

**Pro šťouraly:** ano, existuje list comprehension, a ano, v tomto případě by bylo lepší
použít list comprehension.

## Klíčové slovo break

Někdy se můžeš dostat do situace, kdy na základě splnění nějaké podmínky chceš cyklus
přerušit. K tomu slouží klíčové slovo 
[break](https://docs.python.org/3/reference/simple_stmts.html#break).

Například:

- mám list, a v něm je seznam nějakých hodnot
- jakmile narazím na první číslo, které je bezezbytku dělitelné dvěma, chci cyklus přerušit

```python
hodnoty = [ "a", [ None ], None, 11, 10, 12 , "d"]
prvni = None

for h in hodnoty:
    if not isinstance(h, int):
        continue
    if h % 2 == 0:
        prvni = h
        break
    
if prvni:
    print("První číslo dělitelné dvěma je", prvni)
```

**Pro šťouraly:** ano, i tohle se dá napsat s pomocí funkcí 
[filter](https://docs.python.org/3/library/functions.html#filter) a
[next](https://docs.python.org/3/library/functions.html#next).