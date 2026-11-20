from pathlib import Path

# ==================================================
# VSTUPNÉ DÁTA
# ==================================================

# Editor má vlastný testovací priečinok subory/. Pred každým spustením
# sa obnoví do pôvodného stavu, takže súbory môžete pokojne presúvať.
# Na vašom počítači sa nič nemení.
#
#   subory/
#   ├── FOTO.JPG
#   ├── report.pdf
#   ├── poznamky.txt
#   ├── README
#   └── podklady/

SOURCE = Path("subory")

# ==================================================
# Úloha 2.1 – Pravidlo kategórie
# ==================================================

# TODO: funkcia, ktorá pre súbor vráti názov cieľovej kategórie
#       (prípona bez bodky, bez ohľadu na veľkosť písmen, inak bez_pripony)

# ==================================================
# Úloha 2.2 – Overenie na súboroch zo startera
# ==================================================

# TODO: vypíšte kategóriu pre každý súbor v SOURCE
