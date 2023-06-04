import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    for _ in re.findall(r"\bum\b", s.lower()):
        counter += 1
    return counter



if __name__ == "__main__":
    main()