import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fontList = figlet.getFonts()

def main():

    if len(sys.argv) == 1:
        f = random.choice(fontList)
        figlet.setFont(font=f)

    elif len(sys.argv) == 3 and sys.argv[2] in fontList:

        if sys.argv[1] == "-f" or sys.argv[1] == "--":
            f = sys.argv[2]
            figlet.setFont(font=f)

        else:
            print("Invalid usage")
            sys.exit()

    else:
        print("Invalid usage")
        sys.exit()

    words = input("Input: ")

    print(figlet.renderText(words))




main()