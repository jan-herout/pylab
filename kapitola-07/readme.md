- [Kapitola 7: Hodnota None a dvoustavová (boolovská) logika](#kapitola-7-hodnota-none-a-dvoustavová-boolovská-logika)
  - [Hodnota None](#hodnota-none)
  - [Dvoustavová (booleovská) logika](#dvoustavová-booleovská-logika)
    - [Pravda a nepravda jako výsledek porovnání](#pravda-a-nepravda-jako-výsledek-porovnání)
    - [Logické spojky](#logické-spojky)
    - [Negace](#negace)
    - [Hodnoty, které se "chovají" jako pravdivé či nepravdivé](#hodnoty-které-se-chovají-jako-pravdivé-či-nepravdivé)
    - [Zkrácené vyhodnocování](#zkrácené-vyhodnocování)
  - [Test identity, operátor `is` a `is not`](#test-identity-operátor-is-a-is-not)
  - [Nejdůležitější poznatky](#nejdůležitější-poznatky)
  - [Zdroje](#zdroje)
    - [Anglicky](#anglicky)

# Kapitola 7: Hodnota None a dvoustavová (boolovská) logika

## Hodnota None

Čas od času potřebuješ v programu říci, že nějaká hodnota ještě není nadefinovaná.
V různých programovacích jazycích je tento problém řešený různě. V jazyce Python
k tomu slouží hodnota `None`.

`None` je hodnota, se kterou "nelze nic dělat" - nelze ji přičítat, odčítat, násobit ....

Vyzkoušej si to:

```python
cena_rohliku = 3.50
pocet_rohliku = None
zaplatis = cena_rohliku * pocet_rohliku
print("Zaplatíš:", zaplatis)
```

Na hodnotu `None` se můžeš zeptat (můžeš se ptát, jestli "něco je `None`, tj je to "neznámé",
nenadefinované). K tomu slouží operátor `is`, a 
[více o něm dál v textu](#test-identity-operátor-is-a-is-not).

Vyzkoušej si to:

```python
cena_rohliku = 3.50
pocet_rohliku = None
if pocet_rohliku is not None:
    zaplatis = cena_rohliku * pocet_rohliku
    print("Zaplatíš:", zaplatis)
else:
    print("Nevíme kolik rohlíků budeme kupovat.")
```


## Dvoustavová (booleovská) logika

Počítače vidí svět černobíle. Počítač má problém s chápáním toho, co znamená "možná". 
Něco pro ně buď pravda je, nebo to pravda není.

V jazyce Python se něco, co je pravda, označí jako `True`, a něco, co pravda není, se
označí jako `False`. Hodnoty `True` a `False` jsou hodnoty typu `bool` - `bool` je další 
základní datový typ v jazyce Python. 

Proč mluvíme o booleovské logice? Je to na počet slavného matematika, který se jmenoval
[George Boole](https://cs.wikipedia.org/wiki/George_Boole). 

[Tady](https://cs.wikipedia.org/wiki/George_Boole) si o něm můžeš něco přečíst.

### Pravda a nepravda jako výsledek porovnání

Vždy, když mezi sebou porovnáš dvě hodnoty (takové, které **jdou** porovnat), výsledkem 
je buď pravda (`True`) nebo nepravda (`False`).

Tak například, zkus si tohle. Založ si nový notebook v adresáři `kapitola-07`.

```python
cislo = 9
print("cislo < 10:", cislo < 10) # True
print("cislo je 10:", cislo == 10) # False
```

Všimni si: nejdřív do proměnné `cislo` přiřadíme hodnotu 10, a potom se na tuto hodnotu
ptáme. Porovnáváme ji s číslem 10, a výsledkem je buď pravda (`True`), nebo nepravda (`False`).

V jazyce Python je možné provést následující porovnání:

| operace | příklad  | význam               |
| ------- | -------- | -------------------- |
| `<`     | `3 < 5`  | menší než            |
| `<=`    | `5 <= 5` | menší **nebo rovno** |
| `==`    | `4 == 4` | přesně rovno         |
| `>=`    | `4 >= 4` | větší **nebo rovno** |
| `>`     | `5 > 4`  | větší než            |
| `!=`    | `5 != 4` | **není rovno**       |

Kromě toho existují ale ještě tyhle způsoby, jak se ptát na obsah.

| operace  | příklad         | význam                                      |
| -------- | --------------- | ------------------------------------------- |
| `in`     | `"a" in "abc"`  | `"a"` je v `"abc"`                          |
| `is`     | `cislo is None` | platí, že je hodnota `cislo` None?          |
| `is not` | `cislo is None` | platí, že je hodnota `cislo` **není** None? |

Co je to `None`, si povíme později. Prozatím stačí říct, že `None` znamená 
"nenadefinovanou hodnotu".

Výsledek porovnání můžeš přímo testovat, například podmínkou `if` (o tom později),
nebo ho můžeš přiřadit do nějaké proměnné. Například:

```python
cislo_a = 1
cislo_b = 2
a_mensi_nez_b = cislo_a < cislo_b
print(a_mensi_nez_b)
```

### Logické spojky

Existují dvě logické spojky, `and` a `or`, které spojují dvě boolovské hodnoty, a
výsledkem je nové boolovské hodnota.

Jazyk Python je v obou případech zapisuje stejně, takto:

- `podminka_1 and podminka_2` - **and** - výsledek je pravdivý tehdy, **a jen tehdy**, 
  pokud obě podmínky současně jsou pravdivé (logická spojka _a_)
- `podminka_1 or podminka_2` - **or** - výsledek je pravdivý tehdy, a jen tehdy, pokud 
  **alespoň jedna podmínka je pravdivá** (logická spojka _nebo_)

Jinými slovy, pokud spojuješ dvě hodnoty, výsledek bude....

| `podminka_1` | `podminka_2` | `podminka_1 and podminka_2` | `podminka_1 or podminka_2` |
| ------------ | ------------ | --------------------------- | -------------------------- |
| `True`       | `True`       | `True`                      | `True`                     |
| `False`      | `True`       | `False`                     | `True`                     |
| `True`       | `False`      | `False`                     | `True`                     |
| `False`      | `False`      | `False`                     | `False`                    |


Příklad:

```python
x = 2
y = 1
podminka_1 = x > y                   # True; x je dva, a to je víc než y
podminka_2 = (x % 2 == 0)            # True; zjistíme zbytek celočíselného dělení x dvojkou, a ten je shodný s nulou

vysledek_and = podminka_1 and podminka_2 # True; obě podmínky jsou současně pravdivé
print(vysledek)
```

Pro úplnost: jiné jazyky mohou používat odlišný zápis. Například jazyk `C` používá

- `&&` pro spojku _a_, 
- `||` pro spojku _nebo_

V budoucnu se ti může hodit to vědět.

### Negace

V boolovské algebře existuje ještě operátor pro negaci. 
Jazyk Python ho zapisuje slovem `not`, ale v jiných programovacích jazycích se 
může zapisovat jinak (například: `!` v jazyce `C`).

- negace pravdy je nepravda
- negace nepravdy je pravda

| výraz       | výsledek |
| ----------- | -------- |
| `not True`  | `False`  |
| `not False` | `True`   |

Operátor `not` vždy nejdříve vyhodnotí hodnotu, která za ním následuje, z pohledu boolovské
logiky (tj zjistí zda se něco "chová jako pravda" či zda se to "chová jako nepravda"), 
a potom teprve provede negaci.

### Hodnoty, které se "chovají" jako pravdivé či nepravdivé

Následující hodnoty se chovají jako `False`.

- nula, ať už jde o `int` (`0`), `float` (`0.0`), nebo - pro úplnost - komplexní číslo
- konstanty. `None`, `False`
- prázdné "kontejnery" (o tom víc někdy jindy), tj kontejnery s délkou nula
  - **prázdný string** - `""`
  - prázdný `list`, `dict`, `set`, prázdná `range` (`range(0)`)

**Jakékoliv jiné** hodnoty se chovají jako `True`, a jsou tedy "pravdivé".

Spusť si Jupyter notebook v adresáři `kapitola-07`, a vyzkoušej si to konverzí 
hodnoty na `bool`, takhle.

Nejdřív "pravda".

```python
print("neprázdný string:", bool("string"))
print("nenulové číslo:", bool(-1))
print("neprázdný list:", bool([1,2,3]))
```

Potom "nepravda".

```python
print("prázdný string:", bool(""))
print("nula:", bool(0))
print("prázdný list:", bool([]))
```

Nejspíš to teď vypadá nepochopitelně, ale v budoucnu se ti to bude hodit.
Dost to zpřehledňuje kód. Například, srovnej si dva následující "programy".
Který ti připadá čitelnější?

V obou z nich se objevuje nové klíčové slovo `if`, které můžeš přeložit jako _když_.
_Když_ je nějaká podmínka splněná, _pak_ udělej to, "co je za dvojtečkou".

**Správná varianta** - takhle by to mělo vypadat.

```python
suroviny = ["mouka", "voda", "kvásek", "sůl", "kmín"]

# když suroviny je "pravdivá" hodnota, tj není to prázdný list, pečeme chleba
if suroviny:
    print("Pečeme chleba!")
```

**Nesprávná varianta** - dělá "to samé", ale je _zbytečně_ _delší_, a _nejednoznačná_,
navíc v některých případech může takový podobný program "spadnout s chybou" 
(například: pokud by v proměnné suroviny bylo `None`, program by skončil s chybou).

```python
suroviny = ["mouka", "voda", "kvásek", "sůl", "kmín"]

# když délka seznamu surovin je nenulová, tj není to prázdný list, pečeme chleba
# NESPRÁVNÝ ZÁPIS. Dělá sice "totéž", ale takhle se to psát nemá.
if len(suroviny) > 0:
    print("Pečeme chleba!")
```

### Zkrácené vyhodnocování

Logické spojky (operátory) `and` a `or` používají tzv. _short-circuit_ vyhodnocování.
V češtině pro tenhle termín nejspíš nemáme ekvivalent, ale myslí se tím to, že když mám 
dvě hodnoty spojené logickou spojkou `and` nebo `or`, tak se druhá hodnota nevyhodnocuje
v situaci, kdy je to **zbytečné**.

Co to znamená?

- když dva výrazy spojím spojkou `and`, a první výraz je `False`, je zbytečné vyhodnocovat
  druhý výraz, a interpretr se o to ani nepokusí (protože výsledek spojení bude vždy `False`)
- když dva výrazy spojím spojkou `or`, a první výraz je `True`, je zbytečné vyhodnocovat
  druhý výraz, a interpretr se o to ani nepokusí (protože výsledek spojení bude vždy `True`)

**Proč je důležité to vědět:** protože se toho v programech občas "zneužívá", a protože 
to může v takových případech vést i k ošklivým logickým chybám v programu.

Jak se to zneužívá? Zneužívá se toho v situaci, kdy k výsledku vedou dvě složité operace.
Když provedu první z nich, proč plýtvat časem na spuštění té druhé operace, když je
výsledek dopředu známý?

Abych ti to ilustroval, představ si následující program (tenhle příklad ti **nepůjde**
spustit, není to úplný kód programu).

```python
# získáme raketoplán
mise = lunarni_mise.raketoplan(
    posadka = ["křeček Franta", "morče Pepa"],
    ukoly_mise = ["let na Lunární základna","následně průzkum Marsu"]
    )

# startujeme misi
mise_splnena = mise.let_na_mesic() and mise.z_mesice_na_mars():
print("mise splněna:", mise_splnena)
```

Asi chápeš, že cesta na měsíc je náročný podnik, který trvá docela dlouho, a cesta z 
měsíce na Mars je ještě náročnější a delší.

Jak s tím souvisí _short-circuit_ vyhodnocování?

- dejme tomu, že v důsledku poruchy raketoplán nedokončí ani první úkol mise;
  to znamená, že již `mise.let_na_mesic()` skončí jako `False`
- v takovém případě se program nebude ani pokoušet o let na Mars - proč zbytečně 
  investovat prostředky, čas, a úsilí do něčeho tak náročného, když mise jako celek
  vlastně již selhala?
- a tohle právě je _short-circuit_ vyhodnocení. Protože `mise.let_na_mesic()` je `False`,
  Python se nebude pokoušet vyhodnotit výsledek `mise.z_mesice_na_mars()` - a let na Mars
  neproběhne

**Pozor!** - dejme tomu, že opravdu **potřebujeme** provést let na Mars, protože na tom
závisí osud lidské rasy. Pokud by tomu tak bylo, je osud lidské rasy zpečetěn, a to 
všechno v důsledku jedné chyby v programu! Programátor si neuvědomil existenci 
_short-circuit_ zpracování, a v důsledku této tragické chyby mise skončila dřív, než měla.

## Test identity, operátor `is` a `is not`

Pokud potřebuješ zjistit, jestli nějaká hodnota je **právě pravda** , nebo 
**právě nepravda**, nebo - **nejčastěji** - zda je `None`, používáš operátor `is`. 

Vyzkoušej si to.

```python
jedna = 1
if jedna:
    print("Jednička se chová pravdivě")
if jedna is True:
    print("Ale protože jednička NENÍ PRÁVĚ pravda, pouze se tak chová, tohle nikdy neuvidíš.")
```

Ten druhý text ti Python na výstup nevypíše, zatímco ten první ano.

- **Operátor** `is` je testem identity. 
- Používá se v situaci, kdy chceš zjistit, jestli dvě hodnoty "sdílí stejné místo v paměti".
- Hodnota `True`, `False` (a hodnota `None`) jsou takzvané "singletony", jsou v paměti 
  uložené vždy maximálně jednou, bez ohledu na to, do kolika proměnných je přiřadíš.
- Proto se na testování toho, zda nějaká hodnota je právě `True` nebo právě `False`, ale
  nejčastěji zda je `None`, používá operátor `is` (test identity), a ne operátor `==` (test shody)

Jak se zeptat, jestli něco **je nadefinované?**

Máš dvě možnosti, obě budou fungovat, ale jenom "jedna z nich je správná", ta druhá je
"prohřešek proti programátorské etiketě" (Chestertonův plot).

**Správná varianta**

```python
# ... někde v kódu ....
something = None

# ... a někde jinde v kódu ....
# pokud "something" NENÍ None ....
if something is not None:
    print("Hodnota JE nadefinovaná")
```

**Nesprávná varianta**

```python
# ... někde v kódu ....
something = None

# ... a někde jinde v kódu ....
# pokud NENÍ PRAVDA, že "something JE None ...
if not something is None:
    print("Hodnota JE nadefinovaná")
```

Jak vidíš, oba zápisy budou "nejspíš" dělat to samé. **Ale správný zápis je ten první**,
ne ten druhý.

## Nejdůležitější poznatky

- pravda (`True`) a nepravda (`False`) jsou typu `bool`
- existují logické spojky: `and` (_a_) + `or` (_nebo_), a obě dvě používají _short-circuit_ (zkrácené) vyhodnocení
- i jiné typy hodnot než `True` a `False` mohou být pravdivé
  - jako **nepravdivé** hodnoty se chovají: `None`, nula, prázdný string, prázdný kontejner (list, dict, set)
  - všechny ostatní hodnoty se chovají jako **pravdivé**
- operátor `not` neguje to co je za ním, z pravdy udělá nepravdu, a naopak


## Zdroje

### Anglicky

- [Boolean Operations — and, or, not](https://docs.python.org/3/library/stdtypes.html#boolean)
- [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
