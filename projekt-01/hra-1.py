M_ZAKLAD = {
    "jmeno": "start",
    "popis": "Stojíš na místě kde jsi poprvé začal své dobrodružství.",
    "vychody": ["les"],
}
M_LES = {
    "jmeno": "les",
    "popis": "došel jsi do lesa.",
    "vychody": ["start", "les"],
}
MISTNOSTI = {
    "start": M_ZAKLAD,
    "les": M_LES,
}


def uprav_command(command: str):
    while True:
        command_old = command
        command = command.replace("  ", " ")
        if command_old == command:
            return command


def commands():
    command = input("Co budeš dělat: ")
    command = command.lower()
    command = uprav_command(command)
    return command


def main():
    mistnost = M_ZAKLAD
    while True:
        print(mistnost["popis"])
        command = commands()

        if command == "konec":
            break

        if command.startswith("jdi"):
            command_parts = command.split(" ")
            try:
                kam = command_parts[1]
                mistnost = MISTNOSTI[kam]
            except IndexError:
                print("Nezadal jsi kam chceš jít.")
            except KeyError:
                print("tam nemůžeš jít, ale můžeš jít do ", mistnost["vychody"])
            continue

        print("Nerozumím, napsal jsi: ", command)


if __name__ == "__main__":
    main()
