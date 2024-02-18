- [Funkce](#funkce)
  - [Co je to funkce?](#co-je-to-funkce)
  - [Definice funkce](#definice-funkce)
  - [Vstupní argumenty a návratová hodnota](#vstupní-argumenty-a-návratová-hodnota)
    - [Vstupní argumenty předávané pozicí](#vstupní-argumenty-předávané-pozicí)
    - [Nepovinné argumenty, defaultní hodnoty](#nepovinné-argumenty-defaultní-hodnoty)
    - [Defaultní hodnoty, a argumenty předávané jako klíč a hodnota](#defaultní-hodnoty-a-argumenty-předávané-jako-klíč-a-hodnota)
  - [Cvičení](#cvičení)
  - [Další témata (co se sem nevešlo, témata na jindy)](#další-témata-co-se-sem-nevešlo-témata-na-jindy)


# Funkce

## Co je to funkce?

Představ si, kolik věcí doma spotřebujeme, a potom vyhazujeme. Slupky od brambor. Košťály
z brokolice. Staré školní sešity. Sklenice od medu. Staré noviny. 
A podobně.

A teď si představ, že všechny tyhle věci dáš bez ladu a skladu na hromadu, a necháš
je jen tak ležet. Co z toho vznikne? Nejspíš docela nepěkná hromada věcí, kterou nelze
žádným způsobem využít.

Přitom: slupky od brambor můžeš smíchat se šrotem, a nakrmit tím slepice. Brokolici 
spokojeně sežerou morčata. Sklenici od medu vymyješ, a můžeš do ní něco zavařit. Noviny
se hodí na podpal.

Každá ta věc má svoje využití, a když jí dáš na správné místo, použiješ jí správným způsobem,
tak ti může ještě docela dobře posloužit.

S kódem programu je to podobné. Když bez ladu a skladu nahrneš na hromadu sadu instrukcí,
vznikne nehezká hromada kódu, ve které se nikdo nevyzná, a která nebude sloužit tak dobře,
jak by jinak mohla.

K organizaci kódu slouží - mimo jiné - právě **funkce**. Funkce je blok kódu, který:

- má jasný název
- má nějaké vstupní parametry
- dělá něco užitečného (ideálně jednu, a právě jednu věc)
- může mít nějaké výstupy (může "vrátit" nějakou hodnotu, třeba výsledek nějakého výpočtu)

Funkce použiješ tam, kde:

- **provádíš nějakou operaci opakovaně**; pokud zjistíš, že v programu píšeš "ten samý kód"
  na dvou různých místech, nejspíš je správné napsat funkci, která dělá to co ten kus kódu,
  a potom tu funkci použít.
- **provádíš nějakou věc jenom jednou, ale je sama o sobě "příliš velká", příliš složitá;**
  když si problém rozdělíš na menší celky, a řešíš ho po částech - každou část problému
  v samostatné funkci - pravděpodobně dojdeš k cíli o dost rychleji, než když budeš
  řešit problém celý najednou 

## Definice funkce

Funkce v Pythonu **definuješ** pomocí klíčového slova `def`. Funkce vypadá nějak takhle:

```python
def polovina():
    pass
```

Všimni si:

- Klíčové slovo `def` říká, že to co následuje, je funkce.
- Za slovem `def` následuje **název** té funkce. V tomto případě `polovina`.
- Za názvem funkce následují závorky. Do těch závorek se umisťuje **seznam vstupních parametrů**,
  které funkce akceptuje. V tomto případě je prázdný (žádné vstupní parametry funkce nemá)
- Za závorkami je dvojtečka. Tím říkáš Pythonu, že to, co následuje, je blok kódu, který říká,
  co ta funkce dělá.
- A na závěr si všimni slova `pass`. Tohle slovo znamená - nedělej nic. Můžeš ho použít tam,
  kde Python vyžaduje nějaký blok kódu (v těle funkce, za podmínkou `if`, a podobně), ale kde
  "zatím nevíš", co by tam mělo být.

Tuhle funkci potom můžeš v programu použít - zavolat jí - nějak takhle:

```python
polovina()
```

Taková funkce ale pochopitelně nebude moc užitečná. Konkrétně tahle funkce "nic nedělá".

## Vstupní argumenty a návratová hodnota

Dejme tomu, že ta funkce (polovina) má rozdělit nějaký text přesně na dvě půlky, a vrátit
první z nich. Pokud by počet písmenek byl lichý, **první** písmenko se zahodí, a potom se
vrátí polovina.

Jinými slovy:

- "polovina" z textu `"abcd"` je `"ab"`
- "polovina" z textu `"abcde"` je `"bc"` - první písmenko se zahodí, a pak se text rozdělí

Aby tohle ta funkce mohla udělat, Python musí vědět, že funkce akceptuje jeden vstupní parametr.
Nazveme si ho `text`.

**Definice funkce** by pak vypadala takhle. V závorkách je uvedený seznam vstupních parametrů,
oddělených čárkou - v našem případě je jenom jeden.

```python
def polovina(text):
    # pokud je délka textu liché číslo, vynech první písmenko
    if len(text) % 2 == 1:
        text = text[1:]
    # délku textu rozděl na dva (celočíselné dělení)
    do_pismena = len(text) // 2
    return text[:do_pismena]
```

Všimni si slova `return` které je na konci. To, co je za ním, funkce **vrací** tomu, 
kdo jí zavolal. V našem případě vrací první polovinu textu. Pokud za slovem return nic
není, funkce vrací nenadefinovanou hodnotu (`None`). Mohlo by to vypadat nějak takhle.

```python
def nic_nevraci():
    return
```

Pokud funkce **neobsahuje** slovo return, pak nic nevrací, a pokud se pokusíš její 
návratovou hodnotu použít, zjistíš, že je `None` - nenadefinovaná hodnota.

### Vstupní argumenty předávané pozicí

Dejme tomu, že máš funkci, která akceptuje více parametrů:

```python
def obvod_obdelniku(strana_a, strana_b):
    return ( 2 * (strana_a + strana_b) )
```

Když takovou funkci zavoláš, musíš jí předat **právě** dva parametry, a **musíš** 
je uvést právě v tom pořadí, jak jsou uvedené v definici funkce.

Co se stane, když to neuděláš? Pojďme si to zkusit. Pokud ti ještě neběží Jupyter,
půjdeme si ho spustit. Vytvoř nový notebook v adresáři `kapitola-09`, a výše uvedenou
definici funkce vlož do jedné buňky, a tu spusť.

Potom zkus funkci spustit, ale předej jí špatný počet argumentů. Udělej to z nové buňky,
takto:

```python
obvod_obdelniku(1)
```

Python ti vynadá. Přečti si chybovou hlášku, kterou ti napsal, a zkus si jí přeložit.
Co ti vlastně Python říká?

- _required_  - požadovaný, povinný
- _positional_ - předávaný pozicí
- _missing_ - chybějící

Zkus jí teď zavolat správně:

```python
strana_1 = 5
strana_2 = 10
obvod_obdelniku(strana_1, strana_2)
```

**Co se stane?**

- do proměnné `strana_1` a `strana_2` jsi nechal vložit jejich délku, dejme tomu v metrech
- teď si všimni ještě jednou signatury té funkce: `def obvod_obdelniku(strana_a, strana_b):`
- následně zavoláš funkci `obvod_obdelniku`, a předáš jí dva argumenty
  - na první pozici jsi použil `strana_1`, takže Python si zjistí hodnotu na kterou se tato
    proměnná odkazuje, a předá jí funkci na první pozici; to znamená, že "uvnitř" funkce
    bude číslo 5 dostupné pod názvem `strana_a`, protože tento název je v definici funkce
    uvedený na první pozici
  - na druhé pozici jsi použil `strana_2`, takže Python předá na druhé pozici číslo 10, a
    uvnitř funkce bude tato hodnota dostupná pod názvem `strana_b`

### Nepovinné argumenty, defaultní hodnoty

Občas potřebuješ použít funkci, která argumentů bere hodně. Opravdu hodně. Představ si 
třeba, že chceš použít tuhle funkci: [open](https://docs.python.org/3/library/functions.html#open)

Její signatura vypadá nějak takhle:

```python
def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

**Několik pozorování**:
- všimni si, že má "spoustu" parametrů - je jich 7
- dále si všimni, že u některých z nich je v signatuře funkce rovnítko, a za ním hodnota

Zejména ten druhý fakt je poměrně hodně důležitý. Pythonu tím při definici funkce říkáš:

> Pokud tuhle funkci někdo použije, a nedá ti k dispozici hodnotu daného argumentu,
> znamená to, že si do ní dosadíš hodnotu za rovnítkem.

To znamená, že když funkci zavoláš takhle...

```python
f_handle = open("soubor.txt")
```

... tak to znamená, že:

- hodnota `mode` uvnitř funkce bude `"r"` - protože jsi ji neuvedl, použije se default, uvedený za rovnítkem v signatuře funkce
- hodnota `buffering` uvnitř funkce bude `1` - ze stejného důvodu
- hodnota `encoding` bude `None` - což znamená, že není definovaná - ze stejného důvodů
- a tak dál

### Defaultní hodnoty, a argumenty předávané jako klíč a hodnota

Mějme následující funkci:

```python
def tlac_nebo_tahni(rychlost_tahu=None, sila_tlaku=None):
    """
    Funkci použiješ takhle:
    - tlac_nebo_tahni(rychlost_tahu=10)
    - tlac_nebo_tahni(sila_tlaku=500)
    """
    if rychlost_tahu is not None:
        print("Táhneme rychlostí", rychlost_tahu)
        return
    
    print("Tlačíme!", sila_tlaku)    
```

**Všimni si**:

- některé argumenty mají za sebou rovnítko, a za ním nějakou hodnotu
- co to znamená: pokud tento parametr při použití funkce neuvedeš (nepředáš jeho hodnotu),
  použije se ve funkci ta hodnota, která je uvedená za signaturou funkce

Jinými slovy: ty hodnoty za rovnítkem jsou "defaultní" hodnoty. Použijí se, 
pokud neřekneš jinak.

**Proč je to užitečné:**

- umožňuje ti to vynechat při použití funkce ty hodnoty, u kterých se obvykle používá nějaká typická hodnota (default)
- umožňuje ti to ale také definovat argumenty, které se mohou navzájem vylučovat

Když funkci voláš, tak máš možnost některé - nebo klidně i **všechny** - argumenty
předat jako dvojice klíč/hodnota. Vypadá to nějak takhle:


```python
tlac_nebo_tahni(rychlost_tahu=10)
tlac_nebo_tahni(sila_tlaku=500)
```

Co tím vlastně říkáš:

- První řádek volá `tlac_nebo_tahni(rychlost_tahu=10)`,
  - `rychlost_tahu` nastavuje na 10
  - protože není při "provolání" funkce použitá hodnota `sila_tlaku`, použije se pro ní 
    hodnota `None` uvedená v signatuře funkce
- Druhý řádek volá `tlac_nebo_tahni(sila_tlaku=500)`
  - `sila_tlaku` se nastavuje na 500
  - protože není při "provolání" funkce použitá hodnota `rychlost_tahu`, použije se 
    pro ní hodnota `None` uvedená v signatuře funkce


## Cvičení

- spusť Jupyter, pokud ještě neběží, viz [kapitola-01](../kapitola-01/readme.md#spuštění-jupyter-notebooku)
- přepni se v něm do adresáře `kapitola-09`
- otevři si v něm (v Jupyteru) soubor [funkce.ipynb](./funkce.ipynb), a vyřeš v něm uvedené úlohy
- notebook ulož, proveď [commit a push](../kapitola-git/readme.md#git-commit)

## Další témata (co se sem nevešlo, témata na jindy)

- docstring, help
- proměnné a scope: local, enclosing, global, builtin
