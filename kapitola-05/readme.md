- [Číselné proměnné, a operace s nimi; něco víc o datových typech](#číselné-proměnné-a-operace-s-nimi-něco-víc-o-datových-typech)
  - [Nejdůležitější poznatky](#nejdůležitější-poznatky)
  - [Číselné datové typy](#číselné-datové-typy)
  - [Desetinná značka](#desetinná-značka)
  - [Oddělovač tisíců](#oddělovač-tisíců)
  - [Operátor a operand](#operátor-a-operand)
  - [Základní operace s číselnými hodnotami](#základní-operace-s-číselnými-hodnotami)
  - [Experiment 1](#experiment-1)
  - [Konverze datových typů, zaokrouhlování](#konverze-datových-typů-zaokrouhlování)
    - [Zaokrouhlování](#zaokrouhlování)
    - [Převod na celé číslo](#převod-na-celé-číslo)
  - [převést (`float` je desetinné číslo).](#převést-float-je-desetinné-číslo)
  - [funkce type](#funkce-type)
  - [Kontrolní otázky](#kontrolní-otázky)
  - [Commit](#commit)
- [Zdroje](#zdroje)
  - [Česky](#česky)
  - [Anglicky](#anglicky)

# Číselné proměnné, a operace s nimi; něco víc o datových typech

## Nejdůležitější poznatky

- existují tři číselné datové typy: `int`, `float`, a `complex` (na který příliš často nenarazíš)
- desetinná tečka (nikoliv čárka), oddělovač tisíců
- co je to operátor, co je to operand
- funkce `round` slouží k zaokrouhlení (nahoru i dolů, na zadaný počet desetinných čísel)
- funkce `type` ti vrátí datový typ zadané hodnoty
- v Pythonu je možné převádět hodnoty mezi datovými typy, ale nemusí se to vždy podařit (`ValueError`)


## Číselné datové typy

V programovacím jazyku Python můžeš narazit na tři typy číselných hodnot.

| datový typ | co to je                                                                                                                                  |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `int`      | celá čísla, anglicky [integer](https://slovnik.seznam.cz/preklad/anglicky_cesky/integer), v Pythonu se název zkracuje na `int`            |
| `float`    | desetinná čísla, tj. čísla s [plovoucí](https://slovnik.seznam.cz/preklad/anglicky_cesky/float) desetinnou čárkou; například `1.54`       |
| `complex`  | [komplexní čísla](https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo) - o těch se teď bavit nebudeme, uvádím je jen pro úplnost |

Na číselné hodnoty jsme poprvé narazily ve [třetí kapitole](../kapitola-03/readme.md).

## Desetinná značka

**Zapamatuj si:** v hodinách matematiky desetinná čísla zapisuješ s desetinnou _čárkou_; nejspíš to tak je protože čárku není v sešitě tak snadné přehlédnout,
jako tečku. Ve většině programovacích jazyků se ale zapisuje **desetinná tečka** - je to tak proto, že první počítače vznikly v anglosaském světě, kde se
místo čárky používá tečka. Můžeš si o tom trochu víc přečíst [tady](https://cs.wikipedia.org/wiki/Desetinn%C3%A1_zna%C4%8Dka).

Nenech se tím zmást.

## Oddělovač tisíců

Když ve škole píšeš nějaké opravdu dlouhé číslo, možná ho píšeš s mezerami po každých třech číslicích (oddělovač tisíců).
Možná jsi někdy viděl zápis, kde místo mezer je použitá tečka. V textech, které jsou psané česky, je to úplně normální -
ostatně si o tom můžeš přečíst víc [tady](https://prirucka.ujc.cas.cz/?id=791).

V Pythonu (a ostatně - ve většině programovacích jazyků) to ale normální není.

Opravdu dlouhé číslo bys mohl zapsat v pythonu nějak takhle: `8573963.534548`.

To se ovšem docela špatně čte, že? Je to přibližně... kolik? Osmdesát pět milionů? Nebo snad osm milionů? Nebo osm set tisíc?

A přesně z toho důvodu je v pythonu možné také použít oddělovač tisíců. To číslo se dá napsat také takhle:

```python
8_573_963.534_548
```

Všimni si:

- Najednou je to mnohem jasnější. Na první pohled vidíš, v jakém řádu to číslo je, jsou to miliony.
- Oddělovač tisíců se dá použít i za desetinnou čárkou.

Po pravdě řečeno, Pythonu je jedno, jestli ten oddělovač budeš používat, nebo ne. Je mu dokonce jedno, **na jakém místě v čísle** ten oddělovač použiješ.
Python znak podtržítka v čísle prostě ignoruje.

Jinými slovy, tyhle tři zápisy stejného čísla jsou prostě **ekvivalentní**, je to **pořád to samé** číslo.

- `8573963.534548` - to se asi nečte úplně dobře, že?
- `857_39_63.5_34548` - no **fuj!** Tohle úplně ignoruje smysl použití oddělovače tisíců, jeho smyslem je **zpřehlednit** zápis toho čísla
- `8_573_963.534548` - není tohle mnohem lepší?

**Kontrolní otázka** - jaký je poměr času, který průměrný programátor stráví _čtením_ kódu a _zápisem_ kódu? Je čitelnost zápisu důležitá? Viz [kapitola 2](../kapitola-02/readme.md).

Ne, vážně. Nad tou otázkou se zamysli, a pokud si **nepamatuješ** odpověď, tak se do textu druhé kapitoly podívej, a tu informaci si najdi.

## Operátor a operand

Když zapíšeš v programu nějakou operaci se dvěma hodnotami, například: `5 + 6`, tak jsi použil:

- dva operandy, to jsou ta dvě čísla
- jeden **operátor**, v tomto případě součet

## Základní operace s číselnými hodnotami

S čísly můžeš provádět následující základní operace. Na těchto operacích tě pravděpodobně nic nepřekvapí.

| operátor | příklad | význam                                        |
| -------- | ------- | --------------------------------------------- |
| `+`      | `1 + 2` | součet                                        |
| `-`      | `2 - 1` | rozdíl                                        |
| `*`      | `2 * 2` | násobek                                       |
| `/`      | `4 / 2` | podíl - pozor, výsledek je **vždy** `float` ! |

Kromě toho ale existují ještě další typy operací:

| operátor | příklad  | význam                                                                    |
| -------- | -------- | ------------------------------------------------------------------------- |
| `//`     | `5 // 2` | **celočíselné dělení**; výsledek bude `2`                                 |
| `%`      | `5 % 2`  | **zbytek** po celočíselném dělení; výsledek bude `1`                      |
| `**`     | `2**3`   | x umocněné na `y`, například `2**3` je třetí mocnina dvojky (`2 * 2 * 2`) |

## Experiment 1

- spusť Jupyter
- přepni se do adresáře `kapitola-05`
- v předchozích kapitolách sice sis již jednoduché výpočty vyzkoušel, teď si zkus spočítat několik příkladů s operátory, které jsi zatím nepoužil.
  - Pokud má kostka cukru výšku `1.1 cm`, kolik řad nad sebou se vejde do krabičky, která je vysoká `16 cm`? Použij operátor pro celočíselné dělení.
  - Jaký je obsah čtverce o straně `4321 m`? Použij operátor pro výpočet mocniny.
  - Prkno má na délku `347 cm`. Když ho rozřežeš na kousky o délce `13 cm`:
    - jak velký kus ti nakonec zbude? Použij operátor pro zbytek po celočíselném dělení.
    - kolik kousků o délce `13 cm` máš? Použij operátor pro celočíselné dělení.
- zkus si do nějaké buňky napsat desetinné číslo:
  - `1.254` - **správně**
  - `1,254` - **ŠPATNĚ!!!** Všimni si, co ti Jupyter napsal zpátky: `(1, 254)` - to nevypadá jako číslo, že? A také to číslo není. Víc si o tom povíme někdy jindy.
- notebook (až úlohy vyřešíš) ulož pod názvem `kapitola-05.ipynb`, ale zatím ho nezavírej, budeš do něj dál psát; na konci kapitoly budu chtít, abys provedl jeho commit,
  opravdu tyhle úlohy vyřeš, i když jsou triviální.

## Konverze datových typů, zaokrouhlování

Ve druhé kapitole jsem psal, že Python je interpretovaný programovací jazyk, a že většina takových programovacích jazyků používá _duck_ _typing_.

> když to kváká jako kachna, tak to je kachna

Ještě na to časem narazíme, ale mnohem, mnohem později ... V tomhle okamžiku není úplně snadné vysvětlit do všech důsledků, co to znamená.
V tomto okamžiku to pro nás znamená, že u proměnných **nemusíme** deklarovat datový typ, a i když bychom datový typ nějak deklarovali,
Pythonu na té deklaraci vlastně vůbec nezáleží - ta samá proměnná může v jednom řádku kódu odkazovat na hodnotu, která je `int` (celé číslo),
a na dalším řádku na hodnotu, která je `float` (desetinné číslo). V Pythonu je to v pořádku, pokud bys tohle udělal v nějakém kompilovaném
programovacím jazyce, tak se na tom nejspíš kompilátor zakucká, vynadá ti, a odmítne program přeložit.

Čas od času se hodí hodnotu v jednom datovém typu převést na hodnotu v jiném datovém typu.

### Zaokrouhlování

Například: o něco výše je uvedený tenhle příklad:

> Pokud má kostka cukru výšku 1.1 cm, kolik řad nad sebou se vejde do krabičky, která je vysoká 16 cm?

Jak to vypočítat?

Jedna možnost (pravděpodobně ta správnější) je použít celočíselné dělení:

```python
kolik_kostek = 16 // 1.1
```

Schválně, zkus si tenhle výpočet (i s tím názvem proměnné) zadat do notebooku. Máš ho pořád ještě otevřený? Pokud ne, otevři ho znovu.

Možná tě napadne, že existuje ještě druhá možnost, a to vypočítat ten podíl jako desetinné číslo, a to zaokrouhlit.
V Pythonu existuje funkce [round](https://docs.python.org/3/library/functions.html#round), která slouží přesně
k tomuto účelu.

> round(number, ndigits=None)

> Funkce vrací číslo (number) zaokrouhlené na daný počet číslic (ndigits) za desetinnou čárkou.
> Pokud ndigits vynecháš, vrací celé číslo, které je nejbližší danému vstupnímu číslu.

Všimni si: vrací **nejbližší** číslo. To znamená, že zaokrouhluje dolů, nebo nahoru, podle toho, co je za desetinnou
čárkou.

Zkus si jí použít. Zadej v notebooku tuhle sekvenci příkazů.

```python
kolik_kostek_float = 16 / 1.1
kolik_kostek = round(kolik_kostek_float)
```

Povedlo se?

Zkus se potom podívat na hodnoty, na které ty proměnné odkazují.

```python
print(kolik_kostek_float)
print(kolik_kostek)
```

Do krabičky se vejde `14.54545454....` kostek nad sebe. To je - po zaokrouhlení - `15` kostek cukru.

**To není správný výsledek**. Výsledek je zaokrouhlený nahoru, ale ta patnáctá kostka cukru se do krabičky už nevejde.

### Převod na celé číslo

Správný výsledek v tomto případě můžeme zjistit tak, že **zahodíme** všechno, co je za desetinnou čárkou.

Zadej v notebooku tuhle sekvenci příkazů, v nové buňce, na konci notebooku.

```python
kolik_kostek_int = int(kolik_kostek_float)
print(kolik_kostek_int)
```

Proměnná `kolik_kostek_int` se odkazuje na výsledek výpočtu `16 / 1.1`, který jsme převedli na celé číslo.

Tomu se říká **konverze datového typu**. Když převedeš `float` na `int`, zahazuješ vlastně všechno, co je
za desetinnou čárkou. Tuhle konverzi můžeš provést mnoha různými "směry". 

Můžeš například převést `float` na `int`.

```python
cele_cislo = int(1.254)
```

Můžeš převést `int` na `float`.

```python
desetinne_cislo = float(1)
```

Převod můžeš pochopitelně provést i mezi proměnnými. 

Ovšem **pozor**. Vyzkoušej si v nové buňce následující příklad. Vzniká tam proměnná s názvem `text` ve které je uložený...
no... prostě nějaký text.

```python
text = "příšerně žluťoučký kůň úpěl ďábelské ódy"
cislo = int(text)
```

Tohle Pythonu "nechutná", že? Nejspíš vidíš něco jako:

`ValueError: invalid literal for int() with base 10: 'příšerně žluťoučký kůň úpěl ďábelské ódy'`

Z toho textu prostě číslo udělat nejde.

Pokud se pokusíš provést převod něčeho, co na ten cílový datový typ převést nejde, výsledkem je chyba, 
a program se zastaví. Jak s tím správně naložit ... o tom si povíme něco víc příště.

Zkus si ale ještě tohle (nová buňka na konci).

```python
text = "1"
cislo = int(text)
```

Všimni si: tohle projde. Textová hodnota 1 vypadá jako číslo, a proto se dá na číslo převést.


Zkus si ale ještě tohle (nová buňka na konci).

```python
text = "1.1"
cislo = int(text)
```

Zkus si ale ještě tohle (nová buňka na konci).

```python
text = "1.1"
cislo = float(text)
cele_cislo = int(cislo)
```

Všimni si: oba příkazy projdou.

- Textová hodnota `1.1` vypadá jako desetinné číslo, a Python ji na něj proto dokáže 
převést (`float` je desetinné číslo).
- 

## funkce type

V Pythonu existuje funkce [type](https://docs.python.org/3/library/functions.html#type), která to pro zadaný parametr
vrátí informaci o jeho datovém typu.

Zkus si to (nová buňka, na konci).

```python
type(123)
```

na výstupu bys měl vidět něco jako: `<class 'int'>` - Python ti sděluje, že 123 je něco co je třída (class) typu `int`.
O tom, co je to třída, si povíme víc někdy později. Zatím si z toho odnes poznatek, že 123 je `int`.

Zkus si také tohle:

```python
type(text)
```

Měl bys dostat něco jako: `<class 'str'>`. Python ti sděluje, že proměnná `text` odkazuje na hodnotu typu `str`, což je string.
O tom něco víc v další kapitole.

## Kontrolní otázky

Polož si prosím následující kontrolní otázky, a pokud neznáš odpovědi, přečti si text znovu (a vyzkoušej si příklady)

- jaké číselné datové typy znáš?
- co je to operátor, co je to operand?
- jak zapíšeš celočíselné dělení, jak zjistíš zbytek po celočíselném dělení?
- jak zjistíš datový typ, na který se odkazuje daná proměnná?
- jak můžeš převést datový typ `float` na `int`, a co se s tím číslem stane?
- co se stane, když se na `int` (nebo `float`) pokusíš převést něco, co se nechová jako číslo?

## Commit

Ulož nyní prosím svůj notebook, a proveď commit, a push.


# Zdroje

## Česky

- [Wikipedia: Desetinná značka](https://cs.wikipedia.org/wiki/Desetinn%C3%A1_zna%C4%8Dka)
- [Internetová jazyková příručka: Členění čísel, víceslovné číslovkové výrazy (typ 365, 2 582) a desetinná čísla](https://prirucka.ujc.cas.cz/?id=791)

## Anglicky

-  [Python Built In Functions: type](https://docs.python.org/3/library/functions.html#type)