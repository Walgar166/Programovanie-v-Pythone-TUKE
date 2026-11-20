from pathlib import Path

# ==================================================
# INPUT DATA
# ==================================================

# The editor has its own test directory subory/. It is restored to its
# original state before every run, so you can safely move files around.
# Nothing changes on your computer.
#
#   subory/
#   ├── FOTO.JPG
#   ├── report.pdf
#   ├── poznamky.txt
#   ├── README
#   └── podklady/

SOURCE = Path("subory")

# ==================================================
# Task 3.1 – Destination paths
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: build a relative destination path for every file, e.g. jpg/FOTO.JPG

# ==================================================
# Task 3.2 – Printing the plan
# ==================================================

# TODO: print lines like PLAN: FOTO.JPG -> jpg/FOTO.JPG

# ==================================================
# Task 3.3 – Check that nothing changed
# ==================================================

# TODO: verify that the contents of SOURCE are the same after the run as before
