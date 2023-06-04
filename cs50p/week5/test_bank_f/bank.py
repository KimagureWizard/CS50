def main ():

    greeting = input("")

    print(value(greeting))


def value(greeting):

    n = greeting.lstrip().lower()

    if n.startswith("hello"):
        return 0
    elif n.startswith("h"):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()