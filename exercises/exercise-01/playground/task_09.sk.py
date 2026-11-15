from dataclasses import dataclass

# ==================================================
# VSTUPNÉ DÁTA
# ==================================================

products = [
    {"name": "Keyboard", "price": 79.90, "stock": 4, "category": "electronics"},
    {"name": "Mouse", "price": 29.90, "stock": 0, "category": "electronics"},
    {"name": "Monitor", "price": 219.00, "stock": 2, "category": "electronics"},
    {"name": "Notebook", "price": 4.50, "stock": 12, "category": "office"},
    {"name": "Pen", "price": 1.20, "stock": 35, "category": "office"},
    {"name": "Chair", "price": 149.00, "stock": 1, "category": "furniture"},
]

# ==================================================
# Úloha 9.1 – @dataclass Product so skladovou hodnotou
# ==================================================

# TODO

# ==================================================
# Úloha 9.2 – Konverzia na list[Product]
# ==================================================

# TODO

# ==================================================
# Úloha 9.3 – Filtering dostupných produktov
# ==================================================

# TODO

# ==================================================
# Úloha 9.4 – Sorting podľa ceny alebo skladovej hodnoty
# ==================================================

# TODO

# ==================================================
# Úloha 9.5 – Report podľa kategórie
# ==================================================

# TODO

# ==================================================
# Úloha 9.6 – Spustenie
# ==================================================


def main() -> None:
    # TODO: použite model a funkcie z úloh 9.1 – 9.5
    print("Počet produktov:", len(products))


if __name__ == "__main__":
    main()
