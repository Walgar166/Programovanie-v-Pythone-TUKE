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
# Úloha 6.1 – Testovací stav s kolíziou
# ==================================================

# TODO: vytvorte subory/jpg/FOTO.JPG; pôvodný subory/FOTO.JPG zostane na mieste

# ==================================================
# Úloha 6.2 – Detekcia kolízie
# ==================================================

# Funkcie z predchádzajúcich úloh si sem skopírujte zo svojho riešenia.
# TODO: ak cieľ už existuje, súbor preskočte a pokračujte ďalej

# ==================================================
# Úloha 6.3 – Výpis plánu
# ==================================================

# TODO: vypíšte PRESKOCENE: FOTO.JPG (cieľ už existuje) a PLAN pre ostatné súbory
