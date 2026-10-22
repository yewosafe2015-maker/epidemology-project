import csv
import random

random.seed(42)

rows = [["id", "age", "sex", "smoker", "cases"]]
for i in range(1, 21):
    rows.append([i, random.randint(18, 80), random.choice(["M", "F"]),
                 random.choice(["yes", "no"]), random.randint(0, 5)])

with open("sample_data.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

print("Created sample_data.csv with", len(rows) - 1, "records")
