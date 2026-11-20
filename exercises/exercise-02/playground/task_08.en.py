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
# Task 8.1 – Execute mode
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: add a parameter that enables the real move

# ==================================================
# Task 8.2 – Moving without overwriting
# ==================================================

# TODO: create the destination directory, move the file and report every change;
#       an existing target must not be overwritten

# ==================================================
# Task 8.3 – Resulting structure
# ==================================================

# TODO: print the resulting structure of SOURCE
