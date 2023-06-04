import inflect
p = inflect.engine()

def main():

    nameList = []

    while True:
        try:
            name = input("")
            nameList.append(name)

        except EOFError:
            break

    names = p.join((nameList), sep =",")
    print(f"Adieu, adieu, to {names}")




main()