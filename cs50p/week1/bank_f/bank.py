def geth(n):

    n = n.lstrip().lower()

    if n.startswith("h"):
        return True

    else:
        return False

def gethello(n):

    n = n.lstrip().lower()

    if n.startswith("hello"):
        return True

    else:
        return False

def main ():

    greeting = input("")


    if gethello(greeting) == True:
        print("$0")

    elif geth(greeting) == True:
        print("$20")

    else:
        print("$100")


main()