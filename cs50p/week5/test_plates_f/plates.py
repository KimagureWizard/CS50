def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s.isalnum() == False:
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0:2].isalpha() == False:
        return False

    for i in range(len(s)):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            elif s[i : len(s)].isdigit() == False:
                return False
            else:
                return True


if __name__ == "__main__":
    main()