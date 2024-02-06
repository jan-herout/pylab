- [Dvoustavová (booleanovská) logika](#dvoustavová-booleanovská-logika)
  - [George Boole](#george-boole)
  - [Pravda a nepravda jako výsledek porovnání](#pravda-a-nepravda-jako-výsledek-porovnání)
  - [Operátory logických hodnot](#operátory-logických-hodnot)
  - [Zdroje](#zdroje)
    - [Anglicky](#anglicky)


# Dvoustavová (booleanovská) logika

Počítače vidí svět černobíle. Počítač má problém s chápáním toho, co znamená "možná". 
Něco pro ně buď pravda je, nebo to pravda není.

V jazyce Python se něco, co je pravda, označí jako `True`, a něco, co pravda není, se
označí jako `False`. Hodnoty `True` a `False` jsou hodnoty typu `bool`. 

## George Boole

George Boole je slavný matematik, který je známý především pro svou práci v oblasti logiky. 
Jeho nejvýznamnějším přínosem je vytvoření booleovské algebry, která posloužila jako základ 
pro vývoj digitálního počítače a moderního informačního věku. Jeho práce z roku 1854, 
"An Investigation of the Laws of Thought" (Průzkum zákonů myšlení), položila základy 
symbolické logiky a zavedla algebraický systém pro práci s logickými hodnotami pravda a nepravda, 
který byl klíčový pro vývoj digitálních obvodů a binárního počítačového systému. 

Booleovská algebra se stala základem moderní digitální logiky, a tím i pro fungování 
moderních počítačů a informačních systémů. Díky jeho práci se Boole stal jedním z klíčových 
myslitelů v oblasti informatiky a jeho dědictví má trvalý dopad na technologický svět.

## Pravda a nepravda jako výsledek porovnání

Vždy, kdyř mezi sebou porovnáš dvě hodnoty (takové, které **jdou** porovnat), výsledkem 
je buď pravda (`True`) nebo nepravda (`False`).

Tak například, zkus si tohle. Založ si nový notebook v adresáři `kapitola-07`.

```python
cislo = 10
print("cislo < 10:", cislo < 10) # False
print("cislo je 10:", cislo == 10) # True
```

Všimni si: nejdřív do proměnné `cislo` přiřadíme hodnotu 10, a potom se na tuto hodnotu
ptáme.

V jazyce Python je možné provést následující porovnání:

| operace  | příklad         | význam                                      |
| -------- | --------------- | ------------------------------------------- |
| `<`      | `3 < 5`         | menší než                                   |
| `<=`     | `5 <= 5`        | menší **nebo rovno**                        |
| `==`     | `4 == 4`        | přesně rovno                                |
| `>=`     | `4 >= 4`        | větší **nebo rovno**                        |
| `>`      | `5 > 4`         | větší než                                   |
| `!=`     | `5 != 4`        | **není rovno**                              |
| `in`     | `"a" in "abc"`  | `"a"` je v `"abc"`                          |
| `is`     | `cislo is None` | platí, že je hodnota `cislo` None?          |
| `is not` | `cislo is None` | platí, že je hodnota `cislo` **není** None? |

Co je to `None`, si povíme později. Prozatím stačí říct, že `None` znamená 
"nenadefinovanou hodnotu."

Výsledek porovnání můžeš přímo testovat, například podmínkou `if` (o tom později),
nebo ho můžeš přiřadit do nějaké proměnné. Například:

```python
cislo_a = 1
cislo_b = 2
a_mensi_nez_b = cislo_a < cislo_b
print(a_mensi_nez_b)
```

## Operátory logických hodnot


## Zdroje

### Anglicky

- [Boolean Operations — and, or, not](https://docs.python.org/3/library/stdtypes.html#boolean)
- [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)