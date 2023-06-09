import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    file = open(sys.argv[2], "r")

    # TODO: Read DNA sequence file into a variable
    for line in file:
        sample = line.strip()

    # TODO: Find longest match of each STR in DNA sequence
    sample_list = {}
    sub_list = ["AGATC","TTTTTTCT","AATG","TCTAG","GATA","TATC","GAAA","TCTG"]
    for i in sub_list:
        sample_list[i] = longest_match(sample, i)

    # TODO: Check database for matching profiles
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for i in range(len(sub_list)):
                if int(sample_list[sub_list[i]]) == int(row[sub_list[i]]) and i == len(sub_list)-1:
                    return print(row["name"])
                elif int(sample_list[sub_list[i]]) != int(row[sub_list[i]]):
                    break
        return print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
