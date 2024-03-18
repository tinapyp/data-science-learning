import csv


def read_data(file_path):
    with open(file_path, "r") as file:
        Day54Totals = csv.DictReader(file)
        return list(Day54Totals)


def calculating_rev(data):
    rev = 0
    for row in data:
        rev += float(row["Cost"]) * float(row["Quantity"])
    return rev


def main():
    Day54Totals = read_data("Day54Totals.csv")
    rev = calculating_rev(Day54Totals)
    print(f"Your shop took £{rev:.2f} today.")


if __name__ == "__main__":
    print("🌟Shop $$ Tracker🌟\n")
    main()
