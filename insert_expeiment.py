import csv
import time
import os

from TwoThreeTree import TwoThreeTree


with open("data/numbers.txt") as file:
    numbers = [int(line.strip()) for line in file]

tree = TwoThreeTree()

os.makedirs("results", exist_ok=True)

with open("results/insert_results.csv",
          "w",
          newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Index",
        "Value",
        "Time",
        "Iterations"
    ])

    for index, number in enumerate(numbers, start=1):
        start = time.perf_counter()
        tree.insert(number)
        end = time.perf_counter()
        elapsed = end - start
        writer.writerow([
            index,
            number,
            elapsed,
            tree.iterations
        ])


print("Insert experiment completed")