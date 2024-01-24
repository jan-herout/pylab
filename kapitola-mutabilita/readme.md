- [Imutabilita](#imutabilita)


# Mutabilita a imutabilita

Jak už víš, jazyk Python ti umožňuje uložit do paměti počítače hodnoty mnoha 
různých datových typů.

- [číselné datové typy](../kapitola-05/readme.md)
- [text, datový typ string](../kapitola-06/readme.md)
- TODO - list, dict, tuple, ....

Dále víš, že:

- Proměnná je něco jako "štítek", "ukazatel" na hodnotu, která je uložená v paměti.
- S hodnotami v paměti můžeš provádět různé operace (sčítání, odčítání, multiplikace, ...),
  a že výsledek těchto operací můžeš přiřadit do nějaké proměnné (že nějaká proměnná 
  může odkazovat na výsledek této operace)

Co ale zatím nevíš, je fakt, že některé z těchto hodnot v paměti měnit (mutovat) můžeš,
a jiné ne.

Podívejme se na jednoduchý příklad:

Mějme následující program - zkus si ho zadat do notebooku na novou buňku.

```python
_text = "a"
_text = _text + _text
```

Co tento program dělá?

- zakládá v paměti novou hodnotu `a`, a odkazuje se na ní proměnná `_text`
- potom provede složení těchto dvou hodnot, výsledkem je hodnota `aa`
- do proměnné `_text` uloží odkaz na tuto novou hodnotu

Python rozlišuje dva typy hodnot:

- hodnoty, které jsou **mutable**, tj jejich obsah se může měnit
- hodnoty, které jsou **imutable**, tedy neměnné, jejich obsah se **nemůže** změnit

Co to přesně znamená? čti dál.

## Datové typy, které jsou imutable

Následující datové typy jsou imutable. Pokud některé z nich zatím nepoznáváš, 
netrap se tím.

- číselné datové typy: `int`, `float`
- "textové" datové typy: `str`, `bytes` (byte string)
- uspořádaná n-tice, neboli `tuple`

**Co to znamená?** Znamená to, že když do nějaké proměnné přiřadíš hodnotu tohoto 
datového typu, tak se v paměti počítače tahle hodnota už **nikdy nezmění**. 
Můžeš k této hodnotě přidat hodnotu jinou, můžeš s ní provést jakoukoliv operaci, ale
**vždy to vede k vzniku nějaké nové hodnoty**, nikdy ke změně té už existující hodnoty.

A to je přesně důvod, proč následující operace selže - klidně si to v následující buňce
vyzkoušej.

```python
_text[0] = "b"
```

Výsledkem je chyba:

```
TypeError: 'str' object does not support item assignment
```

Datový typ `str` je **iumutable** (stejně jako `int`, `float`, `tuple`), a jakmile 
jednou v paměti vzniknul, už jeho obsah nemůžeš měnit. Pamatuješ si ještě, že string
je vlastně "kontejner", že je _iterable_, a že můžeš přistoupit na jeho libovolnou pozici?

Přistoupit na ní můžeš, můžeš jí získat, ale **nemůžeš jí změnit.**

Pokud bys opravdu chtěl, aby v proměnné `_text` byla hodnota `ba`, musel bys to napsat jinak.
Například nějak takhle:

```python
_text = "a" # první řádek jsme nezměnili
_text = _text  + _text # ani druhý řádek jsme nezměnili
# ... ale teď chceme hodnotu, na kterou se _text odkazuje, opravit na "ba"
_text = "b" + _text[1:] # všechno od pozice jedna, až do konce
print(_text)
```

Může to vypadat, jako že měníme "obsah proměnné text". Ale ve skutečnosti se děje něco jiného.

- v paměti vznikne hodnota `a`, na kterou se proměnná `_text` odkazuje (přiřazení do proměnné)
- potom se hodnota `a` a hodnota `a` k sobě přidá, vzniká hodnota `aa`, a proměnná text se na ní odkazuje (přiřazení do proměnné)
- potom 
  - vzniká hodnota `b`, která se do žádné proměnné nepřiřazuje
  - z `aa` se vezme všechno od první pozice až do konce, což je `a`
  - `b` a `a` se spojí, vzniká hodnota `ba`
  - a proměnná `_text` se na ní odkazuje (přiřazení do proměnné)


**Hodnoty datových typů, které jsou imutable, nelze přímo měnit.** Je možné nad nimi 
provádět různé operace (přidat, odečíst, multiplikovat, ....), ale výsledkem je vždy 
**nová** hodnota, která je také imutable.

Znamená to ale ještě jednu věc. Dejme tomu, že máš následující program (vyzkoušej si ho)

```python
cislo_1 = 1 # vzniká nová hodnota 1
cislo_2 = 1 # vzniká nová hodnota 1
cislo_2 = 2 # vzniká nová hodnota 2
print(cislo_1, cislo_2) # vypíše: 1,2
```

Do proměnné `cislo_2` jsi nejdřív přiřadil jedničku; pamatuješ se na to, jak jsme si říkali,
že proměnná je jenom "štítek", "ukazatel" na nějakou hodnotu? 
Kdyby hodnota `1` byla v paměti uložená jenom **jednou**, tak by řádek, který provádí
operaci `cislo_2 = 2` musel ovlivnit také hodnotu, na kterou se odkazuje proměnná
`cislo_1`. To znamená, že poslední instrukce, `print(cislo_1, cislo_2)`, by ti vypsala
dvě jedničky, ne jedničku a dvojku.

Když pro hodnoty, které jsou imutable, provedeš přiřazení, tak vždy vzniká **nová** hodnota,
která je také imutable - to znamená, že proměnné, které se odkazují na imutable hodnoty, 
spolu navzájem **nesdílí obsah**, nemůžou se **navzájem ovlivnit**. 

Pro mutabilní hodnoty toto neplatí - dvě proměnné se mohou odkazovat na stejnou mutabilní 
hodnotu, a když potom tuto hodnotu změníš, tak se změna projeví pro obě proměnné!

Tenhle poslední odstavec je extrémně důležitý. Jeho pochopení - respektive nepochopení - 
může být zdrojem nepříjemných chyb v programech, které budeš psát.



## Datové typy, které jsou mutable

TODO