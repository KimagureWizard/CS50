def math(x, y, z):

    if y == "+":
        return print(float(int(x) + int(z)))

    elif y == "-":
        return print(float(int(x) - int(z)))

    elif y == "*":
        return print(float(int(x) * int(z)))

    elif y == "/":
        return print(float(int(x) / int(z)))

def main():

    num = input("")

    x, y, z = num.split(" ")

    math(x, y, z)



main()