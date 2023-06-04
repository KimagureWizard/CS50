def main():
    sort("")


def sort(prompt):
    s_list = {}

    while True:
        try:
            item = input(prompt).upper()

            if item in s_list:
                s_list[item] += 1
            else:
                s_list[item] = 1

        except EOFError:
            break

    for item in sorted(s_list):
        print(f"{s_list[item]} {item}")


main()