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
# Task 6.1 – Test state with a collision
# ==================================================

# TODO: create subory/jpg/FOTO.JPG; the original subory/FOTO.JPG stays in place

# ==================================================
# Task 6.2 – Detecting the collision
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: if the target already exists, skip the file and continue

# ==================================================
# Task 6.3 – Printing the plan
# ==================================================

# TODO: print PRESKOCENE: FOTO.JPG (cieľ už existuje) and PLAN for the other files
