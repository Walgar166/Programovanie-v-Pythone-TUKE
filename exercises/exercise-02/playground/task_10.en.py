from collections import Counter
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
# Task 10.1 – Counters
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: while processing, count processed, planned or moved and skipped
#       files and counts by category

# ==================================================
# Task 10.2 – Summary
# ==================================================

# TODO: print the SÚHRN at the end of the run as in the expected output

# ==================================================
# Task 10.3 – Repeated run
# ==================================================

# TODO: run the plan, then the execution and then the execution once more;
#       the second execution must not process the created categories
