# ==================================================
# Úloha 8.1 – Chybná verzia
# ==================================================

# Pred spustením predpovedzte výstup. Potom kód spustite a reprodukujte chybu.


def add_report_event(
    report_name: str,
    event: str,
    history: list[dict[str, str]] = [],
) -> list[dict[str, str]]:
    history.append({"report": report_name, "event": event})
    return history


morning = add_report_event("attendance", "created")
morning = add_report_event("attendance", "exported", morning)

afternoon = add_report_event("grades", "created")

print("Morning:", morning)
print("Afternoon:", afternoon)

# ==================================================
# Úloha 8.2 – Vysvetlenie
# ==================================================

# TODO: prečo sa história medzi reportmi zdieľa?
#

# ==================================================
# Úloha 8.3 – Oprava
# ==================================================

# TODO: opravte funkciu bez zdieľaného mutabilného defaultu

# ==================================================
# Úloha 8.4 – Testovací scenár
# ==================================================

# TODO: dokážte, že dve nezávislé histórie sa už nemiešajú
