import random


def main():

    check("Level: ")



def check(prompt):

    while True:

        try:
            key = int(input(prompt))

            if key > 100 or key < 1:
                continue

            else:
                key = random.randrange(1, key)

        except ValueError:
            pass

        else:
            break

    while True:

        try:
            guess = int(input("Guess: "))

            if guess > 100 or guess < 0:
                continue

            elif guess < key:
                print("Too small!")

            elif guess > key:
                print("Too large!")

            else:
                print("Just right!")
                break

        except ValueError:
            pass



main()