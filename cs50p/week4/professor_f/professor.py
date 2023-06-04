import random


def main():

    key = get_level("Level: ")

    generate_integer(key)



def get_level(prompt):
    while True:
        try:
            key = int(input(prompt))
            if key > 3 or key < 1:
                continue

            else:
                return key

        except ValueError:
            pass



def generate_integer(key):

    score = 0

    for i in range(10):

        digit_1 = random.randint(((10 ** key) / 10), ((10 ** key) - 1))
        digit_2 = random.randint(((10 ** key) / 10), ((10 ** key) - 1))

        result = digit_1 + digit_2

        while True:
            try:

                for j in range(3):

                    answer = int(input(f"{digit_1} + {digit_2} = "))

                    if j == 2:
                        print(result)
                        break

                    elif result == answer:
                        score+=1
                        break

                    else:
                        print("EEE")

            except ValueError:
                continue

            else:
                break


    print(score)




main()