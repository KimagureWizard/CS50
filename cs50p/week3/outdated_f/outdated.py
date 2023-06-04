month = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    turn("Date: ")


def turn(prompt):
    while True:
        try:
            x, y, z = input(prompt).replace(",", " ").replace("/", " ").split()

            if x in month and 999 < int(z) < 2024 and 0 < int(y) < 32:
                x = int(month[x])
                y = int(y)
                return print(f"{z}-{x:02}-{y:02}")

            elif 0 < int(x) < 13 and 999 < int(z) < 2024 and 0 < int(y) < 32:
                x = int(x)
                y = int(y)
                return print(f"{z}-{x:02}-{y:02}")

            else:
                pass

        except (ValueError, EOFError):
            pass


main()