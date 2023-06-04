import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py") != True:
            print("Not a Python file")
            sys.exit()
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
                counter = 0
                for line in lines:
                    line = line.rstrip()
                    if line.startswith("#") == True or not line.strip():
                        continue
                    else:
                        counter += 1
            file.close()
            return print(counter)
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