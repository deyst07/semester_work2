import random
import os


def generate_numbers(count=10000,
                     min_value=1,
                     max_value=1_000_000):

    numbers = random.sample(
        range(min_value, max_value),
        count
    )

    return numbers


def save_numbers(filename, numbers):
    with open(filename, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")


def main():
    os.makedirs("data", exist_ok=True)
    numbers = generate_numbers()
    save_numbers("data/numbers.txt", numbers)
    print("Generated 10000 random numbers")


if __name__ == "__main__":
    main()
