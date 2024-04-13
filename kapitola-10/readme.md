- [Seznamy - list](#seznamy---list)
  - [Co je to list](#co-je-to-list)
  - [Délka a index](#délka-a-index)
  - [Slicing](#slicing)
  - [Poslední slovo na seznamu](#poslední-slovo-na-seznamu)
  - [Poslední slovo na seznamu: indexace od konce](#poslední-slovo-na-seznamu-indexace-od-konce)
  - [Procházíme listem: cyklus for](#procházíme-listem-cyklus-for)
  - [Datový typ list je MUTABLE - jeho obsah lze měnit](#datový-typ-list-je-mutable---jeho-obsah-lze-měnit)
    - [rozšíření list: metoda append (NA KONEC)](#rozšíření-list-metoda-append-na-konec)
    - [rozšíření list: metoda insert (NA VYBRANOU POZICI)](#rozšíření-list-metoda-insert-na-vybranou-pozici)
    - [Výmaz položky ze seznamu, podle indexu: metoda pop](#výmaz-položky-ze-seznamu-podle-indexu-metoda-pop)
    - [Výmaz položky na indexu, funkce del](#výmaz-položky-na-indexu-funkce-del)
  - [Cvičení](#cvičení)


# Seznamy - list

## Co je to list

Dejme tomu, že chceš k snídani mít palačinky. K tomu, aby sis je mohl udělat, potřebuješ
několik základní ingrediencí - a když je nemáš doma, napíšeš si je na seznam. Trochu jiné
slovo pro seznam může být - například - `list`.

Jak by vypadal takový seznam - list - surovin, které potřebuješ mít, aby sis mohl udělat
palačinky?

```python
suroviny = [ "mléko", "vejce", "hladká mouka" ]
```

**Všimni si**:

- odkaz na list uložíš do proměnné `suroviny`
- za rovnítkem je **hranatá závorka**; když Python narazí na hranatou závorku, ví, že
  to co následuje za ní, je seznam hodnot, ze kterých se list skládá. 
- na konci je zase hranatá závorka; díky ní Python ví, že "tady list končí"

**Zkus si to.** 

- Spusť si Jupyter notebook v adresáři `kapitola-10`,
- ulož ho pod názvem `list.ipynb` 
- do první buňky zkus zadat ten příkaz pro založení seznamu surovin  
- na další buňce se zkus na ten list podívat

```python
print(suroviny)
```

## Délka a index

Pamatuješ se, jak sis  četl o to, co to je string? Konkrétně, psal jsem, že 
[text se chová jako seznam jednotlivých znaků](../kapitola-06/#text-se-chová-jako-seznam-jednotlivých-znaků-iterable).
Asi bys udělal dobře, kdyby ses na tuhle jednu podkapitolu teď podíval znovu.

List je vlastně seznam hodnot. Jako takový má délku, a ty se na ní můžeš kdykoliv zeptat.
Vyzkoušej si to:

```python
print("Délka seznamu surovin je", len(suroviny))
```

Kromě toho je dobré vědět, že seznam je - stejně jako text - indexován, a to od nuly.
To znamená, že když se chceš podívat na první hodnotu seznamu surovin, můžeš to udělat
takhle:

```python
print("První surovina na seznamu je", suroviny[0])
print("Druhá surovina na seznamu je", suroviny[1])
```

**Vyzkoušej si to.**

Pokud se pokusíš získat něco, co na seznamu není, program skončí s chybou. 

Co to znamená?

- máš list o třech položkách, s následujícími indexy:
  - index 0: mléko - `suroviny[0]`
  - index 1: vejce - `suroviny[1]`
  - index 2: hladká mouka - `suroviny[2]`
- list má délku tři, ale poslední položka je na indexu 2, ne na indexu 3 
  (stejně jako u datového typu `str`)

Když se pokusíš přistoupit na index, který v seznamu není, stane se tohle (zkus to).

```python
chybejici_surovina = suroviny[3]
```

Pokud sis to vyzkoušel, dostal jsi na výstupu chybu, které vypadá nějak takhle:

> IndexError: list index out of range

Co ti Python říká?

- _IndexError_ - nejspíš je něco špatně s indexací něčeho, co lze indexovat
- _list_ _index_ _out_ _of_ _range_ - index listu je mimo rozsah (_range_ je anglicky rozsah, nebo také vzdálenost)

**Kvízová otázka:** Co, a proč, ti vypíše tenhle příkaz? Zkus si nejdřív na tu otázku
odpovědět, a potom to zkus v nové buňce spustit. Až to spustíš, zkus v _následující_ 
buňce vysvětlit, co se vlastně stalo. Pokud to není jasné, co se vlastně stalo,
podívej se [sem](../kapitola-06/readme.md#slicing)

```python
print(suroviny[0][0:3])
```

## Slicing

Možná si vzpomínáš, že jsi u datového typu `str` četl něco o "slicingu".
Co je to slicing? Pro připomenutí a osvěžení paměti - podívej se 
[na šestou kapitolu, podkapitola Slicing](../kapitola-06/readme.md#slicing) a zase 
se vrať.

Máš to? Fajn. Slicing se dá použít nejen na string, ale také na list. Ale abychom si to 
mohli demonstrovat, potřebujeme trochu delší list.

- Pokud ještě nemáš spuštěný Jupyter, tak ho spusť
- Pokud ještě nemáš založený notebook, tak ho založ, a to v adresáři `kapitola-10`
- Notebook ulož - nazvi ho `list.ipynb`
- A potom, na jeho konci, spusť v nové buňce tohle (netrap se tím, že nevíš, co to dělá)

```python
import re
import pathlib
for f in pathlib.Path(".").rglob("*.md"):
    slova = [ s.lower() for s in re.split(r"\s",f.read_text(encoding="utf-8")) ]
    slova = [ s for s in slova if re.match("^[a-z]+$", s)]
    break
```

Tak, a teď si (v nové buňce pod tím) pocvičíme pár operací. Vyzkoušej si to.
Pěkně každou operaci zvlášť.

```python
# dej mi prvních deset slov na seznamu
print(slova[:10])
```

```python
# dej mi třetí a čtvrté slovo
#
# všimni si, vzpomeň si: 
#  - indexujeme od nuly, takže třetí slovo je na indexu 2 (ano, je to matoucí)
#  - číslo za dvojtečkou je první slovo, které se NEVRACÍ
#  - takže slovo na indexu 4 - což je PÁTÉ slovo (indexujeme od nuly!) se NEVRACÍ
print(slova[2:4])

# Vrátilo to to, co bys čekal? Podívej se na výstup z předchozí buňky.
# Je to správně?
```

**Cvičení**

- do proměnné `slovo_11` ulož **jedenácté** slovo - a pozor, lidé na rozdíl od Pythonu 
  počítají od jedničky, ne od nuly
- do proměnné `slova_2_az_6` ulož druhé, až šesté slovo seznamu (včetně)
- ověř, že proměnná `slova_2_az_6` má délku 5 (funkce `len`)
- ověř, že v proměnné `slova_2_az_6` skutečně jsou správná slova 
  (srovnej na `print(slova[:10])`, zobrazí se ti tam prvních 10 slov)
- vypiš třetí slovo
- vypiš padesáté slovo
- vypiš první slovo, za ním znak `+`, a za ním desáté slovo - (tj bude to vypadat zhruba takhle: `tomto+je`)

## Poslední slovo na seznamu

**Co když** potřebuješ získat **poslední** slovo z toho seznamu? Jak na to?

Zkus to poslední slovo (z proměnné `slova`) získat. **Nápověda**: potřebuješ vědět, 
jak je ten seznam dlouhý,a vzpomeň si, že je list indexován od nuly (takže list 
o délce deset má první položku na indexu nula, a poslední na indexu 9). 

**Zkus to, a potom teprve čti dál.**

## Poslední slovo na seznamu: indexace od konce

Máš to? Co když ti teď řeknu, že to jde udělat mnohem jednodušším způsobem?

Připraven?

```python
# dej mi poslední slovo ze seznamu
print(slova[-1])
```

Ono totiž je možné indexovat list (nebo string) od začátku, ale klidně také od konce.

Jak to funguje? Zhruba nějak takhle. Dejme tomu, že máš následující (kratší) list:

```python
pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
```

Když v indexu použiješ záporné číslo, má se za to, že **počítáš pozice od konce**.
Poslední prvek je na pozici `-1`, druhý prvek od konce na pozici `-2`, a tak dále.

```
| pozice   :   0   1   2   3   4   5   6   7   8 
| od konce :  -9  -8  -7  -6  -5  -4  -3  -2  -1 
| --------   +---+---+---+---+---+---+---+---+---+
| pismena  : | a | b | c | d | e | f | g | h | i |
| --------   +---+---+---+---+---+---+---+---+---+
```

A ve skutečnosti se to docela často používá, zejména v kombinaci se "slicingem" listu.

Jak? Vyzkoušej si následující "recepty".

```python
# dej mi poslední čtyři slova
print(slova[-4:])
```
```python
# vynech poslední slovo, a dej mi tři slova která jsou před ním
print(slova[-4:-1])
```

Dává to smysl? Jestli ne, přijď se zeptat.


## Procházíme listem: cyklus for

Dejme tomu, že chceš s každou jednotlivou surovinou provést nějakou akci. Třeba jí 
přidat do mísy, a tam všechny suroviny smíchat. K tomu, abys to mohl udělat, potřebuješ
ze seznamu surovin získat postupně všechny ingredience, a s každou z nich něco provést.

Přesně k tomu slouží cyklus `for`. 

```python
for surovina in suroviny:
    print(surovina)
```

Slovo _for_ se z angličtiny dá přeložit jako _pro_, a ten výše uvedený kratičký program
se dá tedy přečíst nějak takhle:

> pro (každou) surovinu v (seznamu) suroviny:
> vypiš (print) surovinu

Zkus si to. Zadej výše uvedený kód do nové buňky, a spusť ho.

**Cyklus `for` je jeden ze základních konstruktů jazyka Python**. Když budeš psát nějaký
program, budeš ho používat dost často.

## Datový typ list je MUTABLE - jeho obsah lze měnit

Teď se bavíme primárně o datovém typu `list`, ale pro připomenutí: říkali jsme si, že 
datový typ `str` je **imutable**, že jeho obsah nelze změnit. 

To znamená, že následující program zhavaruje (zkus si to).

```python
slovo = slova[3] # dej mi čtvrté slovo na seznamu
slovo[0] = "A" # jeho první písmeno změň na "A"
```

Na výstupu bys měl dostat něco jako: `TypeError: 'str' object does not support item assignment`.

**List ale je mutable**. Jeho obsah lze změnit. Co to znamená?

```python
# první tři slova před změnou
print("před změnou", slova[:3])

# ZMĚNA LISTU
slova[0] = "JEDNOROŽEC"

# první tři slova poz měně
print("po změně", slova[:3])
```

Kteroukoliv existující položku listu můžeš takhle změnit.

Kromě toho se alel `list` dá libovolně rozšiřovat, a zkracovat.
To znamená, že do něj můžeš postupně skládat jednotlivé položky - a často se to také dělá.

### rozšíření list: metoda append (NA KONEC)

Nejčastěji se setkáš s tím, že budeš potřebovat přidat novou položku na konec 
existujícího listu. K tomu slouží metoda `append`, která bere jeden parametr, a to je
prvek, který chceš do listu přidat.

```python
suroviny = [ "mouka", "vejce" ]
suroviny.append("mléko") # přidej k surovinám mléko
```

Tak například: dejme tomu, že chceme najít všechna slova, která začínají písmenkem "n".

Jak na to? **Přečti si následující příklad, a zkus ho potom přepsat do nové buňky.**

Nekopíruj ho. opravdu ho přepiš. Nemusíš přepisovat komentáře (`#`), přepiš a spusť kód.
Proč? Protože **nejlépe** se učíme, když věci **děláme**. `Ctrl+C` a `Ctrl+V` ti sice 
usnadní život, ale nic se tak nenaučíš.

```python
# založíme nový, prázdný list
slova_na_n = []

# potom budeme procházet seznamem slov
for slovo in slova:
    # když slovo (po konverzi na malá písmena) začíná na "m" ...
    if slovo.lower().startswith("n"):
        # ... tak ho přidej na konec seznamu (append)
        # VŠIMNI SI: výsledek NIKAM NEPŘIŘAZUJEME.
        # metoda append NIC ROZUMNÉHO nevrací
        slova_na_n.append(slovo)
        # ... to znamená, že následující je CHYBA a dělá to "něco jiného"
        # slova_na_n = slova_na_n.append(slovo)

# jak ten seznam vypadá?
print("Máme celkem", len(slova_na_n), "slov začínajících na písmeno N.")
print("První tři slova:", slova_na_n[:3])
```

### rozšíření list: metoda insert (NA VYBRANOU POZICI)

Co když potřebuješ vložit něco ne na konec, ale na vybranou pozici v listu 
(mezi dva prvky, nebo na začátek)?

Dejme tomu, že do seznamu `slova_na_n` chceme vložit nové slovo, "nádherný", a 
chceme ho mít na začátku. Jak na to?

**Vyzkoušej si to**

```python
print("před změnou:", slova_na_n[:3])

# vlož slovo nádherný na pozici 0 - první parametr je pozice, druhý parametr je
# vkládaný obsah
slova_na_n.insert(0, "nádherný")
print("po změně:", slova_na_n[:3])
```

### Výmaz položky ze seznamu, podle indexu: metoda pop

Co když potřebuješ něco z listu smazat? K tomu slouží metoda `pop`.

Tahle metoda vrací prvek, který jsme odstranili. Bere jeden parametr, a to je index, 
pozice, ze které chceme výmaz provést. Tento parametr je **nepovinný**, a pokud ho 
vynecháš, odstraní **poslední** prvek na seznamu.

```python
cisla = [1,2,3,4,5]
print("před změnou:", cisla)
print("odstraněný prvek je: ", cisla.pop())  # poslední
print("po změně:", cisla)
print("odstraněný prvek je: ", cisla.pop(0))  # první
print("po změně:", cisla)
```

### Výmaz položky na indexu, funkce del

Další způsob jak něco z listu smazat, je použít klíčové slovo `del` (jako _delete_, vymazat).
Tímhle způsobem z listu položku smažeš, ale "nedostaneš jí zpátky", narozdíl od metody 
`pop` zmíněné výše.

Vyzkoušej si to:

```python
cisla = [1,2,3,4,5]
print("před změnou:", cisla)
print("mažeme prvek na indexu 1")
del cisla[1]
print("po výmazu:", cisla)
```

## Cvičení

**Vytvoř na konci novou buňku, a spusť jí.** Vznikne nový list, nazvaný `cisla`.

``` python
import random
def generuj_nahodna_cisla():
    nahodna_cisla = []
    # tento cyklus do i postupně přiřadí čísla od 0 do 99 (včetně)
    for i in range(100):
        nahodna_cisla.append(random.randint(0, 100))
    return nahodna_cisla

cisla = generuj_nahodna_cisla()
```

Potom zkus vytvořit následující úlohy:

- vytvoř nový list, nazvaný `suda_cisla`, a vlož do něj pouze sudá čísla (taková, která beze zbytku jsou dělitelná dvojkou); zjisti, kolik jich je
- vytvoř nový list, nazvaný `vetsi_nez_deset`, a korektně ho naplň
- vytvoř nový list, nazvaný `druha_mocnina`, a ulož do něj druhou mocninu (číslo se vynásobí samo sebou) všech čísel, která jsou menší než 50
- zjisti součet všech čísel v seznamu `druha_mocnina`
