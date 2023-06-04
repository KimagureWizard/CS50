def main():

    name = input("")

    camel(name)


def camel(n):

    for i in n:

        if i.islower() == False:
            print("_" + i.lower(), end="")

        else:
            print(i, end="")

    print("")



main()