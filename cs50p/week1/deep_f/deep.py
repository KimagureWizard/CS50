def check(n):
    
    if n.lower().replace("-", " ") == "forty two" or n == "42":
        return True

    else:
        return False


def main():

    answer = input("")

    if check(answer) == True:
        print("Yes")

    else:
        print("No")



main()