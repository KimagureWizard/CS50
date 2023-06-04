def main():

    time = input("")

    if convert(time) == 7:
        print("breakfast time")

    elif convert(time) == 12:
        print("lunch time")

    elif convert(time) == 18:
        print("dinner time")

    else
        print("Hungry already?")


def convert(time):

    if time.find("p.m.") < 0:

        hours, minutes = time.split(":")

        hours = int(hours)

        return hours

    else:

        hours, minutes = time.split(":")

        hours = int(hours)

        return hours + 12


main()