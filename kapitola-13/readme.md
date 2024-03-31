- [Dictionary](#dictionary)
  - [Co je to dictionary](#co-je-to-dictionary)
  - [Prázdné dictionary a jeho postupná konstrukce](#prázdné-dictionary-a-jeho-postupná-konstrukce)
  - [Získání hodnoty podle klíče a KeyError](#získání-hodnoty-podle-klíče-a-keyerror)
  - [Jakého typu může být klíč a hodnota](#jakého-typu-může-být-klíč-a-hodnota)
  - [Test na přítomnost klíče](#test-na-přítomnost-klíče)
  - [Seznam klíčů - metoda keys](#seznam-klíčů---metoda-keys)
  - [Seznam hodnot  - metoda values](#seznam-hodnot----metoda-values)
  - [Seznam klíčů a hodnot - metoda items](#seznam-klíčů-a-hodnot---metoda-items)
  - [Výmaz položky ze slovníku](#výmaz-položky-ze-slovníku)


# Dictionary

## Co je to dictionary

Jak už název napovídá, dictionary - v jazyce Python jde o datový typ `dict` -
je slovník. Dictionary vždy právě jednomu klíči přiřazuje právě jednu hodnotu,
na kterou lze tento klíč přeložit.

Jak by vypadal takový slovník (`dict`)? Představ si například, že chceš zašifrovat
zprávu v Morseově abecedě. K tomu se právě hodí `dict`, každému písmenku bys mohl
přiřadit odpovídající symbol.

```python
abeceda = {
    "a", ".-",
    "b", "-...",
    "c", "-.-.", # a tak dále
}
```

**Všimni si:**

- dictionary uzavíráme do složených závorek, zleva a zprava ( `{}` )
- uvnitř složených závorek je vždy dvojice, oddělená dvojtečkou
  - vlevo je **klíč**, anglicky _key_
  - vpravo je **hodnota**, anglicky _value_
  - oddělovač mezi klíčem a hodnotou je dvojtečka
  
Takže například: klíčem je `"a"`, a hodnotou je `".-"`.

## Prázdné dictionary a jeho postupná konstrukce

Často se ti může hodit vytvořit prázdné dictionary. Asi to teď nevypadá moc užitečně,
ale do dictionary se dají postupně odkládat nové klíče, a jejich odpovídající hodnoty.

```python
# nejdřív založíme prázdné dictionary
abeceda = {}
# následně na klíč "a" přiřadíme hodnotu ".-"
# pokud by na tom klíči již dříve nějaká hodnota byla, tohle jí přepíše
abeceda["a"] = ".-"
abeceda["b"] = "-..."
abeceda["c"] = "-.-." # a tak dále ...
```

## Získání hodnoty podle klíče a KeyError

Z objektu typu dictionary se dá získat položka podobně, jako z listu.
Používáš hranaté závorky, a do nich napíšeš klíč, pro které chceš z dictionary získat
odpovídající hodnotu.

Takže pokud bych v našem případě chtěl vědět, jak se v morzeovce kóduje písmeno a, napsal by ch to nějak takhle: 

```python
akat_jako_a = abeceda["a"] 
print(f"{akat_jako_a}")
```

Pokud se pokusíš z dictionary získat něco, co v něm není, výsledkem je chyba.

```python
# tohle písmeno jsme ještě do slovníku nezařadili
# výsledkem následujícího příkazu tedy bude chyba
print(abeceda["h"]) 
```

**Všimni si** - výsledkem je chyba typu `KeyError`. Python ti tím jasně říká, že jde 
o chybu spojenou s pokusem o získání hodnoty pro nějaký neexistující klíč (_key_).

Kromě toho: v jazyce Python platí, že u řetězců (str, string) velké a malé písmeno
nejsou stejná hodnota.

To znamená, že následující příkaz také skončí chybou - v dictionary máme přiřazenou
hodnotu pro písmenko `"a"`, ale ne pro písmenko `"A"` - proto ta chyba.

```python
print(abeceda["A"])
```

## Jakého typu může být klíč a hodnota

Klíčem v dictionary může být "cokoliv". Můžeš použít písmena, čísla, string, bool (`True` / `False`).

**Pro šťouraly:** striktně vzato tohle není 100% pravda. Klíčem v dictionary může
být pouze takový datový typ, který je "hashable", implementuje metodu
[__hash__](https://docs.python.org/3/reference/datamodel.html#object.__hash__). 
Do toho teď ale zabíhat nechci.

Hodnotou v dictionary rovněž může být cokoliv. Nejčastěji narazíš na to, že hodnotou v
dictionary je `int` nebo `str`, ale často narazíš také na to, že hodnotou je `list`
nebo dokonce jiné `dict`. Tady opravdu není žádný limit, žádný explicitní požadavek
tady neexistuje.

Vyzkoušej si to:


```python
abeceda[1] = None 
abeceda[2] = [1] # hodnota je list o jedné položce
abeceda[3] = {"žlutý" : "kůň" } # hodnota je dictionary

# všimni si, jak se navenek dict "tváří", jak se prezentuje
print(abeceda)
```

## Test na přítomnost klíče

Pokud potřebuješ zjistit, zda daný klíč v dictionary existuje, můžeš použít (stejně 
jak v případě listu) operátor `in`.

```python
print("Existuje klíč a?", ("a" in abeceda))
print("Existuje klíč A?", ("A" in abeceda))
```

## Seznam klíčů - metoda keys

Každý objekt typu dictionary ti poskytuje metodu `keys()`, která ti vrátí **iterátor**,
jehož průchodem můžeš získat seznam klíčů.

Co to přesně znamená, že tahle metoda vrací iterátor?

Můžeš si to vyzkoušet.

```python
print(abeceda.keys())
```

Všimni si, co ti Python vypsal na výstupu, nejspíš něco jako:

`dict_keys(['a', 'b', 'c', 1, 2, 3])`

Ne první pohled to trochu připomíná list, ale co se stane, když chceš získat 
první klíř, který v tom dictionary je?

```python
print(abeceda.keys()[0])
```

Měl bys vidět chybu, která vypadá nějak takhle: `TypeError: 'dict_keys' object is not subscriptable`

Tím ti vlastně Python říká, že to co vrací metoda `keys()` opravdu není list.
Pokud bys chtěl, aby to list byl, musel bys ho explicitně vytvořit.

```python
keys = list(abeceda.keys()) 
print(f"{keys=}")
print(f"{keys[0]=}")
print(f"{type(keys)=}")
```

**Nejčastěji** ale nejspíš narazíš na to, že potřebuješ projít přes jednotlivé klíče 
v cyklu, a něco s nimi udělat. V takovém případě můžeš napsat něco jako:

```python
for pismeno in abeceda:
    print(pismeno)
```

Všimni si, že tady explicitně neříkáš, že chceš dostat z dictionary všechny klíče, Python to "ví".

Osobně bych asi napsal spíš tohle:

```python
for pismeno in abeceda.keys():
    print(pismeno)
```

Výsledek bude stejný, ale - aslespoň v mých očích - má tu výhodu, že jasně říká, čeho
chci dosáhnout: chci z dictionary nazvaného `abeceda` vzít všechny klíče, a jít přes
ně v cyklu, a něco s nimi udělat.

Za zmínku stojí také to, že **dictionary dodržuje pořadí klíčů**. To znamená, že
se ti v podobném cyklu jednotlivé klíče budou vracet v tom pořadí, v jakém jsi je 
do dictionary doplnil (pro šťouraly: tohle je pravda od Pythonu verze 3.7).


## Seznam hodnot  - metoda values

Pokud bys potřeboval z dictionary získat jenom seznam hodnot, můžeš použít metodu
`values`. Platí tady to, co jsem psal o metodě `keys`, opět jde o iterátor, a
opět platí že Python dodržuje pořadí, v jakém jsi do dictionary klíče a jim 
odpovídající hodnoty přidal.

```python
for hodnota in abeceda.values():
    print(hodnota)
```

## Seznam klíčů a hodnot - metoda items

Pokud bys potřeboval získat současně klíč a jeho hodnotu, můžeš použít metodu
`items`. Opět, vrací iterátor, a dodrží se pořadí vložení do slovníku.

```python
for klic_a_hodnota in abeceda.items():
    print(f"{klic_a_hodnota=}")
```

**Všimni si:**

- metoda `items()` vrací **uspořádanou dvojici** hodnot
- na první pozici je klíč, a na druhé hodnota

Proto v praxi skoro nikdy nenarazíš na kód, který vypadá takhle, a ani bys to takhle
neměl napsat. V praxi chceš tu uspořádanou dvojici hodnot rovnou v předpisu cyklu
rozložit na klíč a na jeho hodnotu, a toho dosáhneš takhle (toto je správný způsob,
jak to napsat).

```python
for klic, hodnota in abeceda.items():
    print(f"{klic=}, {hodnota=}")
```

K tématu "uspořádaných dvojic" (`tuple`) si něco povíme jindy. 

## Výmaz položky ze slovníku

Pokud se chceš zbavit některého z klíčů, a také odpovídající hodnoty, můžeš je 
ze slovníku vymazat. K tomu slouží klíčové slovo `del` (zkratka z _delete_).

Například: náš ukázkový slovník, nazvaný `abeceda`, obsahuje také položky kde
klíčem je číslo.


```python
print(f"{abeceda=}")
del abeceda[1]
del abeceda[2]
del abeceda[3]
print(f"{abeceda=}")
```

Pokus o smazání něčeho, co v dictionary už není, skončí chybou:

```python
del abeceda["tohle tam není"]
```

