from datetime import date
import sys
import inflect


p = inflect.engine()


def main():
    try:
        birth = input("Date of Birth: ")
        convert(birth)
    except(ValueError, TypeError):
        sys.exit("Invalid date")


def convert(s):
    s = date.fromisoformat(s)
    delta = date.today() - s
    if int(delta.days) < 0:
        raise TypeError
    minutes = (p.number_to_words(int(delta.days) * 60 * 24, andword="")).capitalize()
    print(minutes + " minutes")


if __name__ == "__main__":
    main()