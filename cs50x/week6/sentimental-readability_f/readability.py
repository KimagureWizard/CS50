# TODO
def main():
    letters, words, sentences, grade = count(input("Text: "))
    print(f"Letters count: {letters}\n"f"Words count: {words}\n"f"Sentences count: {sentences}")

    if(grade < 1):
        print("Before Grade 1")
    elif(grade > 16):
        print("Grade 16+")
    else:
        print(f"Grade: {grade}")


def count(prompt):
    letters = sum(c.isalpha() for c in prompt)
    words = len(prompt.split(" "))
    sentences = prompt.count('.') + prompt.count('!') + prompt.count('?')
    L = (letters / words) * 100
    S = (sentences / words) * 100
    grade = int(round((0.0588 * L) - (0.296 * S) - 15.8))

    return letters, words, sentences, grade


if __name__ == "__main__":
    main()