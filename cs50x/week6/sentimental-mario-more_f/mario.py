# TODO
while True:
    try:
        height = int(input("Height: "))
        if not 0 < height < 9:
            print("Invalid")
        else:
            for i in range(height):
                print(" " * (height - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1))
            break
    except ValueError:
        print("Invalid")
