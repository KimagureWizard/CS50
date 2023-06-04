import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(r'^(?:.+)"(?:https?.+youtube.+com/)(?:embed/)(.+?)"(?:.+)$', s)
        if not matches:
            return "None"
        else:
            html = ("https://youtu.be/" + matches.group(1))
            return html

    except(ValueError):
        return "None"




if __name__ == "__main__":
    main()