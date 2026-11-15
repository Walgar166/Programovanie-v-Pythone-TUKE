# ==================================================
# VSTUPNÉ DÁTA
# ==================================================

names = ["Anna", "Peter", "Lucia", "Martin"]
points = [92, 67, 81, 45]
active = [True, True, False, True]
allowed_names = ["Anna", "Lucia", "Eva"]

# ==================================================
# Úloha 4.1 – Pôvodná verzia
# ==================================================

# Funguje, ale je ťažkopádna. Spustite ju a zapamätajte si výstup.

rows = []
i = 0
while i < len(names):
    found = False
    for allowed in allowed_names:
        if allowed == names[i]:
            found = True

    if active[i] == True:
        status = "active"
    else:
        status = "inactive"

    row = {
        "index": i,
        "name": names[i],
        "points": points[i],
        "allowed": found,
        "status": status,
    }
    rows.append(row)
    i = i + 1

passed = []
for row in rows:
    if row["points"] >= 51:
        passed.append(row)

passed = sorted(passed, key=lambda row: row["points"])
passed.reverse()

for row in passed:
    print(row)

# ==================================================
# Úloha 4.2 – Pythonic verzia
# ==================================================

# TODO: prepíšte kód z úlohy 4.1. Výstup musí zostať rovnaký.
#       Keď je hotový, pôvodnú verziu zakomentujte alebo zmažte.

# ==================================================
# Úloha 4.3 – Zlepšenia
# ==================================================

# TODO: zapíšte aspoň tri konkrétne zlepšenia:
# 1.
# 2.
# 3.
