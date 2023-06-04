# TODO
def main():
    while True:
        try:
            card = input("Card number: ")
            return calculate(card)
        except ValueError:
            print("NOT A NUMBER")


def calculate(n):
    sum = 0
    c = int(n)

    for _ in range(len(n)):
        num = int(((c % 100)) / 10) * 2
        sum += ((num % 10) + (int((num % 100) / 10)) + (c % 10))
        c = int(c / 100)

    if sum % 10 == 0 and len(n) in [13, 15, 16]:
        if 34 <= int(n[:2]) <= 37:
            print("AMEX")
        elif 51 <= int(n[:2]) <= 55:
            print("MASTERCARD")
        elif int(n[:1]) == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()