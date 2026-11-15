# ==================================================
# INPUT DATA
# ==================================================

results = {
    "Anna": [92, 85, 88],
    "Peter": [45, 67, 51],
    "Lucia": [100, 97, 94],
    "Martin": [35, 40, 42],
    "Eva": [72, 78, 80],
}

groups = [
    [("Anna", "Python", 92), ("Peter", "Python", 67)],
    [("Anna", "Databases", 85), ("Lucia", "Databases", 88)],
]

# ==================================================
# Task 6.1 – Dictionary student -> average
# ==================================================

# TODO

# ==================================================
# Task 6.2 – Set of students with an average of at least 90
# ==================================================

# TODO

# ==================================================
# Task 6.3 – List of passing students (average of at least 51)
# ==================================================

# TODO

# ==================================================
# Task 6.4 – Ranking by average, descending
# ==================================================

# TODO

# ==================================================
# Task 6.5 – Readable rewrite of summary
# ==================================================

# An overly compressed expression. Rewrite it into multi-line code
# and verify that the result stays the same.

summary = {course: sorted({name for group in groups for name, item_course, points in group if item_course == course and points >= 70}) for course in {item_course for group in groups for _, item_course, _ in group}}
print("summary:", summary)
