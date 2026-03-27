import random
import sys


def generate_tests(file_path, size, min_val, max_val):
    with open(file_path, "w") as f:
        for _ in range(size):
            value = random.randint(min_val, max_val)
            f.write(f"{value}\n")


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 test_generator.py <file> <size> [min] [max]")
        sys.exit(1)

    file_path = sys.argv[1]
    size = int(sys.argv[2])

    min_val = int(sys.argv[3]) if len(sys.argv) > 3 else -20
    max_val = int(sys.argv[4]) if len(sys.argv) > 4 else 120

    generate_tests(file_path, size, min_val, max_val)
    print(f"Generated {size} values in {file_path}")


if __name__ == "__main__":
    main()