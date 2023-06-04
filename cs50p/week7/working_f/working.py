import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a, b = s.upper().split("TO")
        a1, a2 = a.split()
        a = a1 + a2
        b1, b2 = b.split()
        b = b1 + b2
        hrs = [a, b]
        if validate_2(a) and validate_2(b):
            for i in range(len(hrs)):
                matches = re.search(r"^(\d+):(\d+)(AM|PM)$", hrs[i])
                hr = int(matches.group(1))
                mn = int(matches.group(2))
                if matches.group(3) == "AM":
                    if hr == 12:
                        hrs[i] = f"00:{mn:02d}"
                    else:
                        hrs[i] = f"{hr:02d}:{mn:02d}"
                elif matches.group(3) == "PM":
                    hr += 12
                    if hr == 24:
                        hrs[i] = f"12:{mn:02d}"
                    else:
                        hrs[i] = f"{hr:02d}:{mn:02d}"
            return f"{hrs[0]} to {hrs[1]}"
        elif validate_1(a) and validate_1(b):
            for i in range(len(hrs)):
                matches = re.search(r"^(\d+)(AM|PM)$", hrs[i])
                hr = int(matches.group(1))
                if matches.group(2) == "AM":
                    if hr == 12:
                        hrs[i] = "00:00"
                    else:
                        hrs[i] = f"{hr:02d}:00"
                elif matches.group(2) == "PM":
                    hr += 12
                    if hr == 24:
                        hrs[i] = f"12:00"
                    else:
                        hrs[i] = f"{hr:02d}:00"
            return f"{hrs[0]} to {hrs[1]}"
        else:
            raise ValueError
    except ValueError:
        sys.exit()



def validate_1(h):
    matches = re.search(r"^(\d+)(AM|PM)$", h)
    if matches and (1 <= int(matches.group(1)) <= 12):
        return True



def validate_2(h):
    matches = re.search(r"^(\d\d?):(\d\d)(AM|PM)$", h)
    if matches and (0 <= int(matches.group(1)) <= 12) and (0 <= int(matches.group(2)) <= 59):
        return True



if __name__ == "__main__":
    main()