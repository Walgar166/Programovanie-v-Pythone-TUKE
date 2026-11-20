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
# Task 4.1 – Test state
# ==================================================

# TODO: create the file subory/podklady/archiv.zip

# ==================================================
# Task 4.2 – Plan of immediate files only
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: the plan must not contain podklady/ or anything inside it

# ==================================================
# Task 4.3 – Check
# ==================================================

# TODO: print the number of planned files and check that archiv.zip is not in the plan
