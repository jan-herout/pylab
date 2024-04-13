import pathlib


def mereni() -> list[str]:
    m = (pathlib.Path(__file__).parent / "mereni.txt").read_text(encoding="utf-8")
    return m.splitlines()
