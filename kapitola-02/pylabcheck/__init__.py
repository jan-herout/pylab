spravne = {
    1: 2,
    2: 3,
    3: 3,
    4: 2,
    5: 2,
    6: 1,
}

def je_spravne(otazka: int, odpoved: int):
    if otazka not in spravne:
        print(f"Špatné číslo otázky, zadal jsi: {otazka}")
        return
    if spravne[otazka] == odpoved:
        print("SPRÁVNĚ!")
    else:
        print("špatně.")
