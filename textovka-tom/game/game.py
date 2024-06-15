from dataclasses import dataclass
from game import room


@dataclass
class Hra:
    mistnosti: list[room.Mistnost]

    def najdi_mistnost(self, kam: str):
        for m in self.mistnosti:
            if m.jmeno == kam:
                return m

    def hra(self):
        mistnost = self.mistnosti[0]
        while True:
            print(mistnost.popis)
            print("Můžeš jít do", mistnost.vychody)
            prikaz = input(">>>")

            if prikaz == "konec":
                break

            if prikaz.startswith("jdi"):
                kam = prikaz.removeprefix("jdi").strip()
                if not kam in mistnost.vychody:
                    print("Tam nemůžeš jít.")
                    continue

                cilova_mistnost = self.najdi_mistnost(kam)
                if cilova_mistnost:
                    mistnost = cilova_mistnost
                else:
                    print("Taková místnost není!")
                continue


HRA = Hra(
    mistnosti=[
        room.M_START,
        room.M_LES,
    ]
)
