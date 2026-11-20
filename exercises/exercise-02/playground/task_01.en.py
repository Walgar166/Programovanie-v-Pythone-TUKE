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
# Task 1.1 – Iterating over entries
# ==================================================

# TODO: iterate over all immediate entries in SOURCE

# ==================================================
# Task 1.2 – Type and suffix
# ==================================================

# TODO: distinguish a file from a directory and a suffixless file

# ==================================================
# Task 1.3 – Output
# ==================================================

# TODO: print the name, type and suffix in aligned columns
