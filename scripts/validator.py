import sys


def load_values(file_path):
    values = []
    with open(file_path, "r") as f:
        for line in f:
            values.append(int(line.strip()))
    return values


def validate(values, threshold):
    expected_alerts = []
    invalid_values = []

    for v in values:
        if v < 0:
            invalid_values.append(v)
        if v > threshold:
            expected_alerts.append(v)

    return expected_alerts, invalid_values


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 validator.py <file> <threshold>")
        sys.exit(1)

    file_path = sys.argv[1]
    threshold = int(sys.argv[2])

    values = load_values(file_path)
    alerts, invalids = validate(values, threshold)

    print("Expected Alerts:", alerts)
    print("Invalid Values:", invalids)


if __name__ == "__main__":
    main()