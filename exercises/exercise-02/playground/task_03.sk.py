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
# Úloha 3.1 – Cieľové cesty
# ==================================================

# Funkcie z predchádzajúcich úloh si sem skopírujte zo svojho riešenia.
# TODO: pre každý súbor zostavte relatívnu cieľovú cestu, napr. jpg/FOTO.JPG

# ==================================================
# Úloha 3.2 – Výpis plánu
# ==================================================

# TODO: vypíšte riadky v tvare PLAN: FOTO.JPG -> jpg/FOTO.JPG

# ==================================================
# Úloha 3.3 – Overenie bez zmeny
# ==================================================

# TODO: overte, že obsah SOURCE je po spustení rovnaký ako pred ním
