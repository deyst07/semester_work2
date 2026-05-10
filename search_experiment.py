import csv
import random
import time
import os

from TwoThreeTree import TwoThreeTree


with open("data/numbers.txt") as file:
    numbers = [int(line.strip()) for line in file]

tree = TwoThreeTree()

for number in numbers:
    tree.insert(number)

search_values = random.sample(numbers, 100)

os.makedirs("results", exist_ok=True)

with open("results/search_results.csv",
          "w",
          newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Index",
        "Value",
        "Found",
        "Time",
        "Iterations"
    ])

    for index, value in enumerate(search_values, start=1):
        start = time.perf_counter()
        found = tree.search(value)
        end = time.perf_counter()
        elapsed = end - start
        writer.writerow([
            index,
            value,
            found,
            elapsed,
            tree.iterations
        ])


print("Search experiment completed")