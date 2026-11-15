import copy

# ==================================================
# VSTUPNÉ DÁTA
# ==================================================

courses = {
    "Python": ["Anna", "Peter"],
    "Databázy": ["Lucia"],
}

# ==================================================
# Úloha 1.1 – Predpoveď a spustenie
# ==================================================

# Najprv predpovedzte výstup, potom kód spustite.

backup = courses

backup["Python"].append("Martin")
backup["Web"] = ["Eva"]

print("courses:", courses)
print("backup: ", backup)
print("courses is backup:", courses is backup)

# ==================================================
# Úloha 1.2 – Experimenty s kópiami
# ==================================================

# TODO: a) dve mená ukazujúce na ten istý objekt
# TODO: b) shallow copy slovníka a zmena vnoreného zoznamu
# TODO: c) nezávislá kópia vnorených zoznamov

# ==================================================
# Úloha 1.3 – Nezávislá kópia
# ==================================================

# TODO: začnite znova od pôvodných dát a vytvorte kópiu,
#       pri ktorej pridanie študenta do backup["Python"] nezmení courses.
