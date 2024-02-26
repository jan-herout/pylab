- [Seznamy - list](#seznamy---list)

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
V našem případě by to mohlo vypadat třeba nějak takhle:

```python
print("Poslední surovina na seznamu je", suroviny[len(suroviny) - 1])
print("Boom!")
print("Tady nic není", suroviny[len(suroviny)])
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

## List NENÍ imutable; list je mutable

TODO

## Slicing

TODO


## Cyklus: klíčové slovo for

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

## Test na přítomnost v seznamu

TODO - patří sýr do receptu?


## Jak změnit obsah listu

## Jak sestavit list z textu


