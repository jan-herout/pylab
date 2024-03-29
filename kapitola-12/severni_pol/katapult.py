from IPython.display import display_markdown
from severni_pol import vetromeric


def vystrel(uhel: int, debug=False):
    if uhel == 0:
        display_markdown("# Nejdřív musíš vypočítat správný úhel.", raw=True)
        return

    mereni = vetromeric.mereni()
    sm = _spravna_mereni(mereni, debug)
    prumer = sum(sm) / len(sm)

    if uhel == prumer:
        display_markdown("# To je správně!", raw=True)
        return

    display_markdown(
        f"""
# To je špatně
                         
![burning-trebuchet.png](./imgs/burning-trebuchet.png)

Katapult se rozpadl v plamenech. Zkus to znovu.

Správný výsledek je: {prumer}
                         """,
        raw=True,
    )


def _spravna_mereni(mereni: list, debug=False):
    """Funkce dostane na vstupu list, a vrací správná měření.
    - jde seznamem měření řádek za řádkem
    - sečte čislici, která je na prvním místě, a číslici která je na konci
    - pokud je součet větší než 5, měření ignoruje, protože je to nějaká odchylka
    - pokud ale součet **není** větší než pět, přidá ho na seznam správných měření
    - potom každé tohle správné pozorování násobí dvanácti, aby získal správný úhel
    - každé správné měření se odloží do seznamu, a na konci se vrátí zpátky

    Args:
        mereni (list): seznam měření v podobě "9daíikem3"

    Returns:
        pouze_spravna (list): seznam správných měření
    """
    # začínáme s prázdným seznamem správných měření
    pouze_spravna = []

    for m in mereni:
        # na první a poslední pozici je číslo
        cislice = [c for c in m if c in "012345689"]
        prvni = int(cislice[0])
        posledni = int(cislice[-1])

        soucet = prvni + posledni
        if debug:
            print(f"{mereni=}")
            print(f"{cislice=}, {prvni=}, {posledni=},{soucet=}")
        if soucet <= 5:
            uhel = soucet * 12
            pouze_spravna.append(uhel)

    return pouze_spravna
