M_START = "Jsi na startu"
M_CIL = "Jsi v cíli"


def main():
    mistnost = M_START

    while True:
        print(mistnost)
        command = input(">>> ")

        if command.startswith("jdi"):
            command_parts = command.split(" ")
            kam = command_parts[1]

            if kam == "cíl":
                mistnost = M_CIL
                continue

            print(f"Tam nemlžeš jít: {kam}, ale můžeš jít do cíle.")
            print("Zkus zadat: jdi cíl")
            continue

        if command == "konec":
            break

        print(f"Nerozumím, napsal jsi: {command}")


if __name__ == "__main__":
    main()
