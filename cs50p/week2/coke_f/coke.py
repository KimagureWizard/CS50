def main():

    counter = 0

    while counter < 50:

        n = get()

        if n == 5 or n == 10 or n == 25:
            counter += n

            if counter >= 50:
                break
            
            print("Amount Due: $" + str(50 - counter))

        else:
            print("Please insert 5, 10, or 25 cents.")

    print("Change Owed: $" + str(counter - 50))



def get():

    n = input("Insert Coins: $")

    return int(n)



main()