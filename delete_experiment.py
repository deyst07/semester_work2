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

delete_values = random.sample(numbers, 1000)

os.makedirs("results", exist_ok=True)

with open("results/delete_results.csv",
          "w",
          newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Index",
        "Value",
        "Time",
        "Iterations"
    ])
    for index, value in enumerate(delete_values, start=1):
        start = time.perf_counter()
        tree.delete(value)
        end = time.perf_counter()
        elapsed = end - start
        writer.writerow([
            index,
            value,
            elapsed,
            tree.iterations
        ])


print("Delete experiment completed")