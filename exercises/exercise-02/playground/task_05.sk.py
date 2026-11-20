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
# Úloha 5.1 – Kontrola vstupu
# ==================================================

# TODO: funkcia, ktorá odmietne neexistujúcu cestu aj cestu na súbor
#       a vypíše: CHYBA: vstup nie je existujúci priečinok: <cesta>

# ==================================================
# Úloha 5.2 – Spracovanie iba platného vstupu
# ==================================================

# Funkcie z predchádzajúcich úloh si sem skopírujte zo svojho riešenia.
# TODO: pri neplatnom vstupe nevykonajte žiadnu ďalšiu operáciu

# ==================================================
# Úloha 5.3 – Testovacie vstupy
# ==================================================

# TODO: vyskúšajte Path("neexistuje"), Path("subory/report.pdf") a SOURCE
