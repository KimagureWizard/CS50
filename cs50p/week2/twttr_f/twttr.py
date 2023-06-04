def main():
    words = input("")
    print(shorten(words))


def shorten(words):
    new_words = ""
    for word in words:
        if word.lower() in "aeiou":
            new_words += ""
        else:
            new_words += word
    return new_words



if __name__ == "__main__":
    main()