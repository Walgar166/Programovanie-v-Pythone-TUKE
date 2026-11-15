# ==================================================
# Task 8.1 – Buggy version
# ==================================================

# Predict the output before running. Then run the code and reproduce the bug.


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
# Task 8.2 – Explanation
# ==================================================

# TODO: why is the history shared between reports?
#

# ==================================================
# Task 8.3 – Fix
# ==================================================

# TODO: fix the function without a shared mutable default

# ==================================================
# Task 8.4 – Test scenario
# ==================================================

# TODO: prove that two independent histories no longer mix
