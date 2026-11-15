# ==================================================
# VSTUPNÉ DÁTA
# ==================================================

results = {
    "Anna": [92, 85, 88],
    "Peter": [45, 67, 51],
    "Lucia": [100, 97, 94],
    "Martin": [35, 40, 42],
    "Eva": [72, 78, 80],
}

groups = [
    [("Anna", "Python", 92), ("Peter", "Python", 67)],
    [("Anna", "Databázy", 85), ("Lucia", "Databázy", 88)],
]

# ==================================================
# Úloha 6.1 – Dictionary student -> priemer
# ==================================================

# TODO

# ==================================================
# Úloha 6.2 – Set študentov s priemerom aspoň 90
# ==================================================

# TODO

# ==================================================
# Úloha 6.3 – List úspešných študentov (priemer aspoň 51)
# ==================================================

# TODO

# ==================================================
# Úloha 6.4 – Ranking podľa priemeru zostupne
# ==================================================

# TODO

# ==================================================
# Úloha 6.5 – Čitateľný prepis summary
# ==================================================

# Príliš stlačený zápis. Prepíšte ho na viacriadkový kód
# a overte, že výsledok zostal rovnaký.

summary = {course: sorted({name for group in groups for name, item_course, points in group if item_course == course and points >= 70}) for course in {item_course for group in groups for _, item_course, _ in group}}
print("summary:", summary)
