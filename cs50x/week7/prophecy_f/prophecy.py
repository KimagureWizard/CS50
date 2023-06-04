from cs50 import SQL
import csv

def main():
    with open("students.csv") as file:
        reader = csv.DictReader(file)

        students = []
        student = {}

        for row in reader:
            name = row["student_name"]
            house = row["house"]
            student = {"name": name, "house": house}
            students.append(student)

    for student in students:
        print(f"{student['name']} is in {student['house']}")

if __name__ == "__main__":
    main()