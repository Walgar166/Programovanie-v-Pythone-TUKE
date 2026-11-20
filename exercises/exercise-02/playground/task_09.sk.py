import argparse
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
# Úloha 9.1 – Parser argumentov
# ==================================================

# TODO: ArgumentParser(prog="organizer.py") s povinnou cestou a prepínačom --vykonat

# ==================================================
# Úloha 9.2 – Funkcia main
# ==================================================

# Funkcie z predchádzajúcich úloh si sem skopírujte zo svojho riešenia.
# TODO: main(argv) spracuje argumenty, skontroluje vstup a spustí plán
#       alebo vykonanie podľa --vykonat

# ==================================================
# Úloha 9.3 – Spustenie z príkazového riadku
# ==================================================

# V editore nie je príkazový riadok. Príkaz
#   python organizer.py subory --vykonat
# zodpovedá volaniu main(["subory", "--vykonat"]).
# TODO: vyskúšajte relatívnu cestu, absolútnu cestu (Path.cwd() / "subory"),
#       prepínač --vykonat a spustenie bez cesty
