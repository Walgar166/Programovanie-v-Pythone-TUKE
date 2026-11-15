import copy

# ==================================================
# INPUT DATA
# ==================================================

courses = {
    "Python": ["Anna", "Peter"],
    "Databases": ["Lucia"],
}

# ==================================================
# Task 1.1 – Prediction and run
# ==================================================

# Predict the output first, then run the code.

backup = courses

backup["Python"].append("Martin")
backup["Web"] = ["Eva"]

print("courses:", courses)
print("backup: ", backup)
print("courses is backup:", courses is backup)

# ==================================================
# Task 1.2 – Experiments with copies
# ==================================================

# TODO: a) two names referring to the same object
# TODO: b) a shallow copy of the dictionary and a change of a nested list
# TODO: c) an independent copy of the nested lists

# ==================================================
# Task 1.3 – Independent copy
# ==================================================

# TODO: start again from the original data and create a copy where
#       adding a student to backup["Python"] does not change courses.
