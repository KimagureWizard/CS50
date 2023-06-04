import sys
import csv

def main():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") != True:
            print("Not a CSV file")
            sys.exit()
        try:
            table = []
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(", ")
                    table.append({"first": first, "last": last, "house": row["house"]})
            with open(sys.argv[2], "a") as file:
                for student in sorted(table, key=lambda student: student["first"]):
                    file.write(f"{student['first']},{student['last']},{student['house']}\n")
        except FileNotFoundError:
            print(f"Could not read {sys.argv[1]}")
            sys.exit()
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()




if __name__ == "__main__":
    main()