# Formátovací řetězce: f-string

Občas potřebuješ na obrazovku napsat nějakou hodnotu, a potřebuješ jí přesně naformátovat.
K tomu se dá použít takzvaný "f-string", neboli "formátovací string".

Vypadá to nějak takhle:

```
cislo = 1.23456789
print(f"hodnota v proměnné cislo je {cislo}")
```

**Všimni si:**

- před uvozovkami je uvedené písmenko `f`. Tím programu říkám, že následuje f-string
- uvnitř uvozovek je něco, co je uvedené ve "složených závorkách" (havranech): `{cislo}`;
  tím programu říkám, že na toto místo má vložit tu hodnotu, na kterou se odkazuje proměnná `cislo`

Ve skutečnosti v těch složených závorkách může být uvedený **libovolný literál**. To znamená, 
že tam může být uvedená jakákoliv proměnná, výsledek nějakého výpočtu, a podobně.

Například:

```python
print(f"tři krát čtyři je {3 * 4}")
```

Asi to teď nevypadá moc užitečně, ale s pomocí f-stringů se dají dělat různé "triky".
Nejčastěji asi narazíš na:

**Rychlý debugging**

```python
cislo_1 = 1.23456
print(f"{cislo_1 = }")
```

**Formátování desetinných čísel** - dejme tomu, že chci float zobrazit na dvě číslice za desetinnou čárkou.

```python
cislo_1 = 1/3
print(cislo_1)
print(f"{cislo_1:.2f}")
```

Ale je možné také například doplnit nuly (mezery) zleva, zprava, převést číslo do šestnáctkové soustavy,
a určitě toho jde provést mnohem víc.