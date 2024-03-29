- [Kapitola 02: Co je to Python?](#kapitola-02-co-je-to-python)
  - [Nejdůležitější poznatky](#nejdůležitější-poznatky)
  - [Trocha historie](#trocha-historie)
  - [Python je interpretovaný jazyk](#python-je-interpretovaný-jazyk)
    - [von Neumannova architektura](#von-neumannova-architektura)
    - [Strojový kód a assembler](#strojový-kód-a-assembler)
    - [Kompilované programovací jazyky](#kompilované-programovací-jazyky)
    - [Interpretované programovací jazyky](#interpretované-programovací-jazyky)
  - [Python je dynamický, interpretovaný programovací jazyk](#python-je-dynamický-interpretovaný-programovací-jazyk)
  - [Filozofie Pythonu](#filozofie-pythonu)
  - [Chestertonův plot](#chestertonův-plot)
- [Zdroje](#zdroje)
  - [Česky](#česky)
  - [Anglicky](#anglicky)

# Kapitola 02: Co je to Python?

## Nejdůležitější poznatky

Čtenář tohoto textu by si z něj měl odnést zejména následující poznatky:

- co to znamená, když je program _open source_
- co to je assembler
- jaký je rozdíl mezi kompilovaným, a interpretovaným programovacím jazykem
- Python je dynamický, interpretovaný jazyk; co to přináší za výhody a nevýhody
- proč záleží na čitelnosti programu, jaký je poměr mezi časem stráveným čtením existujícího programového kódu a psaním nového kódu
- Chestertonův plot: co tento princip říká, jak mu rozumět?

## Trocha historie

Programovací jazyk Python vznikl v osmdesátých letech 20. století. Původním autorem jazyka je **Guido van Rossum**.

První verze jazyka (Python 1) byla zveřejněna v roce 1994. Pro kontext, v roce 1991 byla zveřejněna
první verze specifikace protokolu `WWW` (World Wide Web), což je rok který zhruba zformoval Internet do podoby, v jaké
ho známe dnes.

Python se stal populárním s příchodem druhé verze jazyka (Python 2). Python 2 byl zveřejněn v roce 2000.
Dnes již není podporovaný, ale zcela jistě se ještě pořád na některých místech používá.

Aktuální verze jazyka je Python 3. **Vše, co bude dále uvedeno o jazyku Python, platí právě pro Python 3**.
Mezi verzí 2 a verzí 3 jsou určité **syntaktické rozdíly**, které znemožňují spuštění programů psaných pro Python 2
ve verzi Python 3. Tím však výčet rozdílů zdaleka nekončí (pro účely tohoto textu asi nedává smysl se jimi v detailu zabývat).

Python je vyvíjený v [open source](https://cs.wikipedia.org/wiki/Otev%C5%99en%C3%BD_software) modelu. To znamená, že:

- zdrojové kódy samotného jazyka jsou veřejně dostupné
- v podstatě _kdokoliv_ může k údržbě a k vývoji jazyka přispět
- neexistuje žádná firma, ani žádný jednotlivec, který by ručil za "správnost" tohoto jazyka
- pro kritické komponenty (jako je Python) však fakt, že je zdrojový kód otevřený, zpravidla přispívá k vyšší bezpečnosti a menšímu počtu chyb,
  než by tomu bylo u programů, které nemají otevřený zdrojový kód; větší počet lidí ten kód studuje, kdokoliv může ohlásit chyby.

Python se neustále rozvíjí. Psát programy v jazyce Python znamená neustále se vzdělávat, a sledovat (podstatné) změny.

## Python je interpretovaný jazyk

Python je tzv. **interpretovaný programovací jazyk**. Co to znamená?

### von Neumannova architektura

Každý počítač je stroj. Původní návrh toho, z čeho se počítač skládá, vychází z tak zvané von Neumannovy architektury.
Počítač se podle ní skládá z řídící jednotky (dnes se tomu říká CPU, "central processing unit", procesor),
paměti (těch je více typů, ale většinou se mluví o paměti RAM, "random access memory"), a vstupních (klávesnice) a výstupních (monitor)
zařízení.

Počítačový program reálně vykonává právě CPU, a CPU "rozumí" velmi jednoduchému, omezenému, strojovému jazyku
(také se tomu říká strojový kód). Tento strojový jazyk je vlastně sada instrukcí, zaznamenaná formou čísel,
a do tohoto strojového jazyka je nutné **přeložit** každý počítačový program, aby mu CPU "rozuměl".

### Strojový kód a assembler

První počítačové programy byly zapisovány přímo ve strojovém kódu. "Programátor" tedy musel do detailu znát instrukční sadu
daného typu procesoru, a musel ji (s pomocí převodových tabulek) dokázat převést do takové podoby, kterou bylo možné
do počítače zadat. Jako jedna z prvních technologií, které se pro to používala, byl [děrný štítek](https://cs.wikipedia.org/wiki/D%C4%9Brn%C3%BD_%C5%A1t%C3%ADtek),
což byla papírová kartička, do které se pomocí speciálních kleští zaznamenal program přímo v číselném zápisu (ve strojovém kódu).

Děrné štítky se používaly ještě před tím, než vznikl první počítač v pravém slova smyslu. Například v oblasti textilního
průmyslu:
[Jacquardův stroj](https://cs.wikipedia.org/wiki/Joseph_Marie_Jacquard).

Dalším pokrokem bylo zavedení assembleru. [Assembler](https://en.wikipedia.org/wiki/Assembly_language) je symbolický programovací jazyk, který lze bez potíží s pomocí překladače
převést přímo do strojového kódu.

Například, takhle nějak může vypadat program napsaný v assembleru, a přeložený do strojového kódu. Jde o program,
který vypíše "hello world". **Nemusí to tak vypadat**, ale "vynález" assembleru byl obrovský pokrok proti době, kdy byly počítačové
programy zaznamenávány pomocí kleští na děrné štítky.

```
;calling the assembler “nasm”:
;nasm -f elf64 hello_64.asm; ld -m elf_x86_64 -s -o hello_64 hello_64.o
sys_exit  equ 60
sys_write  equ 1

section .text
  global _start               ;must be declared for using gcc
_start:                       ;tell linker entry point
  mov  edx, len               ;message length
  mov  esi, msg               ;message to write
  mov  edi, 1                 ;file descriptor (stdout)
  mov  eax, sys_write         ;system call number (sys_write)
  syscall                     ;call kernel
  xor edi, edi     
  mov  eax, sys_exit          ;system call number (sys_exit)
  syscall                     ;call kernel

section .data

msg  db  'Hello, world!',0xa  ;our dear string
len  equ  $ - msg             ;length of our dear string
```

Takhle nějak vypadá tento program přeložený do strojového kódu.

```
    hello_64:  Dateiformat elf64-x86–64
    Disassembly of section .text:

    00000000004000b0 <.text>:
      4000b0:  ba 0e 00 00 00      mov  edx,0xe
      4000b5:  be d0 00 60 00      mov  esi,0x6000d0
      4000ba:  bf 01 00 00 00      mov  edi,0x1
      4000bf:  b8 01 00 00 00      mov  eax,0x1
      4000c4:  0f 05               syscall
      4000c6:  31 ff               xor  edi,edi
      4000c8:  b8 3c 00 00 00      mov  eax,0x3c
      4000cd:  0f 05               syscall

    Contents of section .data:
     6000d0 48656c6c 6f2c2077 6f726c64 210a  Hello, world!.
```

Assembler se v dnešní době pořád ještě pro některé úlohy používá. To znamená, že jsou programátoři, kteří jsou schopní programy
produkovat přímo v assembleru, to znamená velmi blízko strojovému kódu. Z příkladu nahoře je ale na první pohled zřejmé, že
**nejde o jednoduchý úkol**.

A protože lidé - a zejména programátoři - jsou líní, hledaly cesty, jak tuto situaci dále zjednodušit.

### Kompilované programovací jazyky

V roce 1953 byl firmou IBM zahájen vývoj prvního kompilovaného programovacího jazyka, Fortran. Jeden z jeho autorů později řekl:

> „Většina mé práce vzešla z toho, že jsem líný. Neměl jsem rád psaní programů a tak, když jsem pracoval na IBM 701 a psaní
> programů pro výpočet dráhy raketové střely, začal jsem pracovat na programovacím systému, který mi usnadnil psát programy.“

Poměrně krátce poté se začaly objevovat další programovací jazyky: [COBOL](https://cs.wikipedia.org/wiki/COBOL),
a zejména programovací jazyk [C](https://cs.wikipedia.org/wiki/The_C_Programming_Language).

Všechny tyto programovací jazyky měly tu vlastnost, že zjednodušovaly zápis programů ve srovnání s assemblerem. Všechny tyto programovací jazyky
se v nějaké podobě používají dodnes, byť - například - v jazyce COBOL pravděpodobně mnoho nových programů nevzniká. Současně se dá říci,
že zavedly mnoho konceptů, které se používají dodnes - měly silný vliv na další podobu programování.

Období mezi lety 1953 a 1978 (kdy vyšla kniha popisující jazyk C) velmi, velmi ovlivnilo podobu výpočetní techniky tak, jak ji známe dnes.

Vývoj se však nezastavil, a jsou vymýšleny stále nové, a nové programovací jazyky, které se zpravidla snaží reagovat na některé (vybrané)
nedokonalosti svých předchůdců. Mezi ně může patřit například `C++` (C plus plus), `C#` (C - sharp), `Rust`, `Go` (někdy také Golang), a mnoho,
mnoho dalších. Těchto jazyků existují řádově stovky, některé jsou populární, některé ne.

Program napsaný v **kompilovaném programovací jazyce** je přímo překládán do strojového kódu. To přináší určité výhody, ale také určité nevýhody.

Výhody:

- **Tyto programy jsou zpravidla rychlé.** Tím, že jsou přeloženy do strojového kódu, je možné je přímo spustit na CPU bez nutnosti nějakých doplňujících kroků.
- díky tomu, že je program nutné přeložit do strojového kódu, **dochází při překladu k jeho kontrole.**
  Určité typy chyb je možné během této kontroly odhalit, a upozornit na ně (zastavit překlad).

Nevýhody:

- Díky tomu, že existuje několik různých CPU architektur, a díky existenci různých operačních systémů, nejsou zpravidla tyto kompilované programy
  mezi nimi navzájem přenositelné. Například, ten samý program, pokud má běžet na Microsoft Windows, a na počítači Macintosh (Mac), musí být pro
  každý z těchto operačních systémů (a CPU architektur) přeložen zvlášť.
- Poskytují zpravidla menší flexibilitu, než interpretované programovací jazyky (jako je například Python)
- Obtížné odhalování chyb za běhu

Program napsaný v jazyce C může vypadat zhruba nějak takto:

```C
#include <stdio.h>

int main() {
    char hello[] = "Hello";             // nová proměnná, pole znaků, a její inicializace
    char world[] = "World";             // nová proměnná, pole znaků, a její inicializace

    printf("%s, %s!\n", hello, world);  // vypiš "Hello World!"

    return 0;
}
```

### Interpretované programovací jazyky

- Jedním z prvních interpretovaných programovacích jazyků byl [LISP](https://cs.wikipedia.org/wiki/Lisp).
- V 70-tých letech 20. století se objevil další významný interpretovaný jazyk, [BASIC](https://cs.wikipedia.org/wiki/BASIC).
  Používá se dodnes.
- V 80-tých letech 20. století se objevily programovací jazyky `Perl` a `Python`. Oba se používají dodnes.
- Později se objevily další. `Ruby`, `Tcl`, `JAVA` (která se dá zařadit jak mezi kompilované, tak mezi interpretované programovací jazyky), `JavaScript`, ...

Základním rozdílem oproti **kompilovaným** programovacím jazykům je existence **interpreteru**. **Interpreter** je počítačový program,
který dokáže načíst kód daného jazyka, a _interpretovat_ ho, tj. porozumět "co se po něm chce" a "instrukce vykonat". U některých programovacích
jazyků tohoto typu navíc vzniká jakýsi "virtuální počítač", který tyto instrukce vykonává. Mezi tyto jazyky patří například JAVA, a právě Python.

Interpretované programovací jazyky ve srovnání s kompilovanými mají odlišné vlastnosti.
V určitých situacích mohou tyto vlastnosti být výhodné, ale také nevýhodné.

- **Přenositelnost:**
  - zpravidla je možné ten samý program spustit na různých operačních systémech bez úprav kódu
  - neplatí to 100% vždy, zejména u složitějších programů; ale v ideálním případě to platí
- **Rychlost**
  - stejný program napsaný v interpretovaném jazyce bude zpravidla pomalejší (někdy **řádově** pomalejší)
    než stejný program napsaný v jazyce kompilovaném.
- **Flexibilita:**
  - tyto jazyky zpravidla podporují koncept tzv. _duck_ _typing_; co to znamená: u proměnných není nutné uvádět dopředu datový typ
  - proměnná může za běhu měnit datový typ
  - "když to kváká jako kachna, tak to je kachna" - tj. když do proměnné uložíš číslo, datový typ je číslo; když tam uložíš text, datový typ je text (u kompilovaných programů taková situace končí chybou překladu, program se nepřeloží)
- **Jednoduchost, čitelnost:**
  - interpretované programovací jazyky zpravidla poskytují "mocnější nástroje" než jazyky kompilované
  - to znamená, že "stejného efektu" dosáhneme zapsáním menšího počtu instrukcí v daném programu
  - napsat stejný program v interpretovaném programovacím jazyce bude zpravidla jednodušší, než v jazyce kompilovaném
- **Udržovatelnost:** - níže uvedené je můj názor, založený na osobní zkušenosti (může jít o chybný názor)
  - jednodušší/kratší programy v interpretovaném jazyku jsou na údržbu zpravidla jednodušší, než stejný program v jazyku kompilovaném
  - důvodem je fakt, že interpretované jazyky bývají "jednodušší" než ty kompilované
  - od určité složitosti programu to ale přestává platit
    - daní za vyšší flexibilitu interpretovaného programovacího jazyka jsou naopak vyšší nároky na údržbu
    - například, v Pythonu není nutné deklarovat u proměnných datové typy, a to může vést v programu k různým těžko odhalitelným chybám
    - existují nástroje, které se tento problém snaží odstranit, ale způsobují přitom řadu jiných typů problémů
- **Odhalování chyb za běhu:**
  - interpreter je možné za běhu pozastavit, a "podívat se dovnitř co se tam děje"
  - proto je zpravidla jednodušší v těchto jazycích za běhu program ladit, a hledat v něm chyby

Program napsaný v jazyce Python může vypadat například takto:

```python
hello = "hello"                 # nová proměnná, string
world = "world"                 # nová proměnná, string
print (hello + " " + world)     # vypiš hello world
```

## Python je dynamický, interpretovaný programovací jazyk

Co to znamená:

- v Pythonu napíšete program zpravidla docela rychle
- program bude zpravidla pomalý (ale to nemusí být nutně na škodu)
- od určité složitosti může být tento program těžké udržovat, doplňovat do něj nové funkce
- "ten samý" program bude fungovat na počítači s Windows, ale také na serveru na Linuxu, nebo na Macu

## Filozofie Pythonu

Principy, na kterých je založený Python, jsou shrnuty v tak zvaném [Zen of Python](https://cs.wikipedia.org/wiki/Filozofie_Pythonu).

Z těchto principů bych vyzvedl následující (interpretace je moje vlastní):

- jednoduchý program je lepší, než složitý program
- na čitelnosti záleží; čitelný program je lepší než nečitelný program
- přílišná volnost škodí - jsou věci, které Python umožní udělat, ale to neznamená, 
  že je to dobrý nápad (měl by být jeden způsob, jak věci udělat - a měl by být na 
  první pohled jasný)

Je to takový "seznam přání", kterým je dobré se snažit vyhovět. Ale nejspíš ne za 
každou cenu.

Existuje odhad, který tvrdí, že průměrný programátor stráví cca 60-90% času tím, že 
čte existující kód programu, a snaží se ho pochopit, a teprve čas který zbude stráví tím, 
že píše nový kód (Steve McConnell, Code Complete).

To znamená, že na čitelnosti programu, a na popisu toho co program dělá, 
opravdu **velmi, velmi záleží**.

Pro ilustraci: [tohle](https://gist.github.com/cgoldberg/4332167) je funkční program 
napsaný v jazyce Perl. Je napsaný záměrně tak, aby byl nečitelný, je to takové 
"programátorské umění" (*podívejte se co jsem udělal!*)

Ještě jinak: tohle je také funkční, správný, spustitelný program. Ale ani já, když se
na to podívám, nedokážu na první pohled říct, "co to dělá". A teď si představ, 
"že to nedělá to co má", a že je nutné tam tu chybu najít a opravit. Až jsem se s té
představy zpotil.

```python
(lambda f, n: f(f, n))(
    lambda f, n: [(not n % 3 and "fizz" or "") + (not n % 5 and "buzz" or "") or n]
    + f(f, n + 1)
    if n <= 100
    else [],
    1,
)
```

## Chestertonův plot

Existuje dobře známý princip, který formuloval anglický spisovatel [G. K. Chesterson](https://cs.wikipedia.org/wiki/Gilbert_Keith_Chesterton).
Nikde jsem nenašel doslovný překlad do češtiny, ale dovolím si jej parafrázovat.

> Dejme tomu, že existuje určitá instituce, nebo zákon; pro zjednodušení řekněme, 
> že na cestě je brána, nebo plot. Existují lidé, kteří se považují za **moderní reformátory**, 
> a kteří k tomuto plotu vesele přistoupí, a řeknou:
> "Není mi jasné, proč tady ten plot stojí, nevidím žádný smysl jeho existence. Pojďme ho zbourat."

> Moudrý člověk by na to odpověděl: "Pokud nechápeš smysl existence toho plotu, nedovolím 
> ti ho zbourat. Bež pryč a přemýšlej. Později, až za mnou přijdeš, a řekneš mi, proč tady ten 
> plot stojí, ti možná dovolím ho zbourat."

Autor tuto poučku sice formuloval ve vztahu ke změnám katolické církve, ale ve skutečnosti
jde o hlubokou myšlenku, která má obrovský přesah do všech oblastí lidské činnosti.
I do oblasti psaní počítačových programů.

- programování je velmi, velmi složitá činnost; počítačové systémy jsou zpravidla velmi složité
- proto, pokud existuje nějaký zažitý postup jak věci dělat, není dobré pokoušet se jej změnit,
  pokud člověk nerozumí tomu, co za tímto principem je

Například:

- Existuje poučka, která říká, kolik znaků má mít program na jednom řádku.
- Existují poučky, která říká, jak se v programu má zacházet s chybami.
- Existuje poučka, která říká, že programy by neměly být "příliš košaté" (velký počet odsazení)

A tak by se dalo ještě dlouho, dlouho pokračovat.

# Zdroje

## Česky

- Wikipedia
  - [Von Neumannova architektura](https://cs.wikipedia.org/wiki/Von_Neumannova_architektura)
  - [Děrný štítek](https://cs.wikipedia.org/wiki/D%C4%9Brn%C3%BD_%C5%A1t%C3%ADtek)
  - [Assembler](https://cs.wikipedia.org/wiki/Assembler)
  - [Fortran](https://cs.wikipedia.org/wiki/Fortran)
  - [C](https://cs.wikipedia.org/wiki/The_C_Programming_Language).
  - [BASIC](https://cs.wikipedia.org/wiki/BASIC)
  - [LISP](https://cs.wikipedia.org/wiki/Lisp)
  - [Zen of Python](https://cs.wikipedia.org/wiki/Filozofie_Pythonu)
  - [Jacquardův stroj](https://cs.wikipedia.org/wiki/Joseph_Marie_Jacquard)

## Anglicky

- Wikipedia:
  - [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
  - [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
  - [Assembly language](https://en.wikipedia.org/wiki/Assembly_language)
- Chesterton's fence
  - [Chesterton’s Fence: A Lesson in Second Order Thinking](https://fs.blog/chestertons-fence/)
  - [Chesterson university: Lecture 57: The Thing](https://www.chesterton.org/lecture-57/)