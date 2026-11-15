# ==================================================
# INPUT DATA
# ==================================================

names = ["Anna", "Peter", "Lucia", "Martin"]
points = [92, 67, 81, 45]
active = [True, True, False, True]
allowed_names = ["Anna", "Lucia", "Eva"]

# ==================================================
# Task 4.1 – Original version
# ==================================================

# It works, but it is clumsy. Run it and note the output.

rows = []
i = 0
while i < len(names):
    found = False
    for allowed in allowed_names:
        if allowed == names[i]:
            found = True

    if active[i] == True:
        status = "active"
    else:
        status = "inactive"

    row = {
        "index": i,
        "name": names[i],
        "points": points[i],
        "allowed": found,
        "status": status,
    }
    rows.append(row)
    i = i + 1

passed = []
for row in rows:
    if row["points"] >= 51:
        passed.append(row)

passed = sorted(passed, key=lambda row: row["points"])
passed.reverse()

for row in passed:
    print(row)

# ==================================================
# Task 4.2 – Pythonic version
# ==================================================

# TODO: rewrite the code from task 4.1. The output must stay the same.
#       When you are done, comment out or delete the original version.

# ==================================================
# Task 4.3 – Improvements
# ==================================================

# TODO: write down at least three concrete improvements:
# 1.
# 2.
# 3.
