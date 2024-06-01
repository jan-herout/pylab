# Nejdřív nadefinujeme tři místnosti, každá z nich má popis, a východy.
M_START = {
    "popis": "Stojíš na startu",
    "vychody": ["jezirko", "les"],
}

M_JEZIRKO = {
    "popis": "Jsi u jezírka",
    "vychody": ["start"],
}

M_LES = {
    "popis": "Jsi v lese",
    "vychody": ["start"],
}

# Potřebujeme vědět, jaké všechny místnosti na naší mapě existují.
# Každá z nich má jméno (klíč v našem dictionary) a definici (což je další dictionary).
# Názvy místností musí odpovídat východům, které používáme v definici místností.
MAPA = {
    "start": M_START,
    "les": M_LES,
    "jezirko": M_JEZIRKO,
}


def get_command() -> str:
    """Funkce získá od uživatele příkaz, normalizuje ho, a vrátí ho.
    Příkaz se převede na lowercase, a zajistí se, že slova příkazu jsou
    oddělená jednou mezerou.

    Returns:
        str: říkaz, který uživatel zadal
    """
    command = input(">>> ")
    command = command.lower()

    # pro šťouraly: reálně bych tady použil "list comprehension",
    # ale o ní jsme si zatím nic neříkali
    command_parts = []
    # rozděl zadaný příkaz přes mezeru
    for c in command.split(" "):
        # pokud tato část příkazu není prázdná, přidej ji k částem příkazu
        if c:
            command_parts.append(c)
    # znovu slož příkaz z jeho částí, oddělovačem je mezera
    command = " ".join(command_parts)
    return command


def main():
    # na začátku jsme na startu
    mistnost = M_START

    while True:
        print(mistnost["popis"])

        # pro šťouraly: tohle by šlo určitě napsat líp
        # get_command() interně text rozděluje a zase skládá,
        # a následně ho u příkazu "jdi" znovu rozdělujeme
        # ale pro ilustraci to asi stačí
        command = get_command()
        if command.startswith("jdi"):
            try:
                # za slovem jdi bude mezera, a za ní bude místnost kam chceme jít
                command_parts = command.split(" ")
                # tohle může selhat, pokud command není složený aspoň ze dvou slov
                # chyba by byla IndexError
                kam = command_parts[1]
                # tohle může selhat, pokud místnost kam jdeme, není na mapě
                # chyba by byla KeyError
                mistnost = MAPA[kam]
            except IndexError:
                print("Neřekl jsi, kam chceš jít.")
            except KeyError:
                print(f"Tam nemůžeš jít ({kam}), můžeš jít do", mistnost["vychody"])
            continue

        if command == "konec":
            break

        print(f"Nerozumím, napsal jsi: {command}")


if __name__ == "__main__":
    main()
