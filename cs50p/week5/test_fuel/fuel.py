def main():
    fraction = convert("Fraction: ")
    print(gauge(fraction))


def convert(prompt):
    while True:
        try:
            x, y = prompt.split("/")
            z = round((int(x) / int(y)) * 100)
            if z >= 0 and z <= 100:
                return z
            else:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            prompt = input("Fraction: ")


def gauge(z):
    if z == 1 or z == 0:
        return "E"
    elif z == 99 or z == 100:
        return "F"
    else:
        return f"{z}%"




if __name__ == "__main__":
    main()