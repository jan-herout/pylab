# Kapitola 03: Proměnné a jednoduché datové typy

## Nejdůležitější poznatky

## Proměnné

V [první  kapitole](./../kapitola-01/readme.md) jsi řešil jednoduchý příklad s výpočtem velikosti flotily.
Psal jsi v něm kód, který vypadal nějak takhle:

```python
piratu_celkem = 128
piratu_na_lod = 14 + 1 + 1
lodi = piratu_celkem / piratu_na_lod
print("Ve flotile bude celkem", lodi, " lodí")
```

Podívej se na první řádek tohoto programu. Myslím si, že na první pohled intuitivně chápeš, "co tato instrukce dělá".

```python
piratu_celkem = 128
```

Pojďme si to nyní rozebrat.

- v kódu se v levé části objevuje název proměnné, `piratu_celkem`
- vpravo od něj je použito "rovnítko" (`=`), což je **operátor** přiřazení; Python interpretru tím říkáme, 
  že do proměnné `piratu_celkem` má přiřadit hodnotu, která je vpravo za rovnítkem
- vpravo od rovnítka je uvedená číselná hodnota 128

Na těchto třech výrocích můžeme nyní demonstrovat několik důležitých principů, kterými se Python řídí.

#### Co je to proměnná: hodnotu ukládáme do paměti

Vzpomínáš si na druhou kapitolu, kde jsme si představili princip [von Neumannovy architektury?](../kapitola-02/readme.md##von-neumannova-architektura).
Tak ten princip je ve skutečnosti docela důležitý.

Každá **hodnota**, ať už to je číslo, nebo text, se kterou tvůj program nějak zachází, je uložená v **paměti** počítače.
Musí to tak být. Koneckonců, i ty, pokud chceš vědět, kdy dostaneš příští dárek k svátku, nebo k narozeninám (a ano, asi to 
bude nějak souviset s [hustou melou](https://www.zatrolene-hry.cz/spolecenska-hra/husta-mela-2762/), musíš zapátrat v paměti,
kdy že to zatraceně ten svátek máš.

A když si vzpomínáš, kdy že to bude, musíš si uvědomit, že hledáš datum svého svátku.

V téhle analogii:

- datum je **hodnota**
- a fakt, že jde o svátek, a ne o narozeniny, je **proměnná**

Nebo ještě jinak a možná lépe.

```
  ┌────────────────────────────────────────┐
  │                                        │
  │  PAMĚŤ (RAM) jako skladiště            │
  │  ---------------------------------     │
  │  Každý box je papírová krabice.        │
  │  Představuje určitou část paměti.      │
  │                                        │
  │  ┌────────┐  ┌────────┐  ┌────────┐    │
  │  │ 128    │  │ ....   │  │ ....   │    │
  │  └────▲───┘  └────────┘  └────────┘    │
  │       │                                │
  └───────┼────────────────────────────────┘
          │
  ┌───────┴───────┐
  │ piratu_celkem │   
  └───────────────┘
````

Představ si, že jsi skladník zavřený ve skladu moderního umění.
Do skladu přijel s ještěrkou tvůj kolega, a má na ní docela velkou skulpturu čísla 128. 
Je to umělecké dílo nazvané "pirátů celkem". Máš za úkol ho uložit, ochránit 
ho před poškozením, a až přijde pravý čas, tak ho zase ze skladu dostat ven (nejspíš do muzea).

Co v takové situaci jako dobrý skladník uděláš?

- sošku uložíš do přiměřeně velké krabice, a tu odložíš na polici
- na krabici nalepíš papírový štítek, a na něj napíšeš něco jako *soška*, *dřevěná*: *pirátů* *celkem*

Ta dřevěná soška je v téhle analogii hodnota, která se ukládá do paměti počítače.
Počítačová paměť je skladiště, které máš na skladišti. Ty, skladník, jsi počítačový program,
a ten papírový štítek s nápisem *pirátů* *celkem* je proměnná.

Proměnná je vlastně štítek, je to název, který dáváš nějaké hodnotě.


#### Co je to proměnná: hodnotu chceme získat zpět z paměti




#### Všechno je objekt
