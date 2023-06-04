import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) == 3:
        extension = ["jpg", "jpeg", "png"]
        if not sys.argv[1].lower().endswith(tuple(extension)):
            print("Invalid Input")
            sys.exit()
        elif not sys.argv[2].lower().endswith(tuple(extension)):
            print("Invalid Input")
            sys.exit()
        elif sys.argv[1].lower().endswith(tuple(extension)) != sys.argv[2].lower().endswith(tuple(extension)):
            print("Input and output have different extensions")
            sys.exit()
        try:
            with Image.open(sys.argv[1]) as input:
                shirt = Image.open("shirt.png")
                input = ImageOps.fit(input, shirt.size)
                input.paste(shirt, shirt)
                input.save(sys.argv[2])
        except FileNotFoundError:
            print("Input does not exist")
            sys.exit()
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()




if __name__ == "__main__":
    main()