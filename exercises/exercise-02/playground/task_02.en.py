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
# Task 2.1 – Category rule
# ==================================================

# TODO: a function that returns the destination category name for a file
#       (suffix without the dot, case-insensitive, otherwise bez_pripony)

# ==================================================
# Task 2.2 – Check on the starter files
# ==================================================

# TODO: print the category of every file in SOURCE
