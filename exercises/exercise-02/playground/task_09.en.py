import argparse
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
# Task 9.1 – Argument parser
# ==================================================

# TODO: ArgumentParser(prog="organizer.py") with a required path and a --vykonat flag

# ==================================================
# Task 9.2 – The main function
# ==================================================

# Copy the functions from the previous tasks here from your own solution.
# TODO: main(argv) parses the arguments, checks the input and runs the plan
#       or the execution depending on --vykonat

# ==================================================
# Task 9.3 – Running from the command line
# ==================================================

# The editor has no command line. The command
#   python organizer.py subory --vykonat
# corresponds to the call main(["subory", "--vykonat"]).
# TODO: try a relative path, an absolute path (Path.cwd() / "subory"),
#       the --vykonat flag and a run without a path
