def convert(n):
    n = n.replace(":)", "🙂").replace(":(", "🙁")
    return n

def main():
    x = convert(input(""))
    print(f"{x}")



main()