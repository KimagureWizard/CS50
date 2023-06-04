import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv") != True:
            print("Not a CSV file")
            sys.exit()
        try:
            table = []
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
                for line in lines:
                    pizza, small, large = line.rstrip().split(",")
                    menu = {"pizza": pizza, "small": small, "large": large}
                    table.append(menu)
            file.close()
            return print(tabulate(table, tablefmt="grid"))
        except FileNotFoundError:
            print("File does not exist")
            sys.exit()
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()




if __name__ == "__main__":
    main()