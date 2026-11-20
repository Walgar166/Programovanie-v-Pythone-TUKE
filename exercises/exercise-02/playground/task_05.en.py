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
# Task 5.1 – Input check
# ==================================================

# TODO: a function that rejects a missing path and a path to a file
#       and prints: CHYBA: vstup nie je existujúci priečinok: <path>

# ==================================================
# Task 5.2 – Processing valid input only
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: perform no further operation for invalid input

# ==================================================
# Task 5.3 – Test inputs
# ==================================================

# TODO: try Path("neexistuje"), Path("subory/report.pdf") and SOURCE
