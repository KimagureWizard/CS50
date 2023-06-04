def main():
    get("Fraction: ")




def get(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            z = round(int(x) / int(y) * 100)

            if z == 1 or z == 0:
                return print(f"E")

            elif z == 99 or z == 100:
                return print(f"F")

            elif z > 1 and z < 99:
                return print(f"{z}%")

            else:
                pass

        except (ValueError, ZeroDivisionError, NameError):
            pass





main()