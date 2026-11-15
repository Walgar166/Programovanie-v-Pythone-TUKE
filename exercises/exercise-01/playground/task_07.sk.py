# ==================================================
# VSTUPNÉ DÁTA
# ==================================================

orders = [
    ("A100", "Anna", 129.90, "paid"),
    ("A101", "Peter", 59.00, "pending"),
    ("A102", "Anna", 15.90, "paid"),
    ("A103", "Lucia", 220.00, "cancelled"),
    ("A104", "Peter", 35.50, "paid"),
    ("A105", "Eva", 89.90, "paid"),
    ("A106", "Anna", 42.00, "pending"),
]

# Funkcie navrhnite s type hints. Dáta im odovzdajte ako argument,
# vo vnútri funkcií nečítajte globálnu premennú orders.

# ==================================================
# Úloha 7.1 – Objednávky jedného zákazníka
# ==================================================

# TODO

# ==================================================
# Úloha 7.2 – Tržba iba zo zaplatených objednávok
# ==================================================

# TODO

# ==================================================
# Úloha 7.3 – Filter podľa statusu a minimálnej sumy
# ==================================================

# TODO

# ==================================================
# Úloha 7.4 – Summary status -> počet objednávok
# ==================================================

# TODO

# ==================================================
# Úloha 7.5 – Zákazník s najvyššou zaplatenou sumou
# ==================================================

# TODO

# ==================================================
# Úloha 7.6 – Príklad použitia
# ==================================================


def main() -> None:
    # TODO: zavolajte svoje funkcie, aspoň raz s keyword argumentom
    print("Počet objednávok:", len(orders))


if __name__ == "__main__":
    main()
