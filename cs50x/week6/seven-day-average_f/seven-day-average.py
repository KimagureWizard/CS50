import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    RECENT = 15
    case_dict = {}
    for row in reader:
        state = row["state"]
        case = int(row["cases"])
        if state not in case_dict:
            case_dict[state] = [case]
        else:
            if len(case_dict[state]) < RECENT:
                case_dict[state].append(case)
            else:
                case_dict[state].pop(0)
                case_dict[state].append(case)
    for state in case_dict:
        for i in range(14, -1, -1):
            if i == 0:
                case_dict[state].pop(0)
            else:
                case_dict[state][i] -= case_dict[state][i-1]
    return case_dict


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        if state in new_cases:
            t_average = round(sum(new_cases[state][7:13]) / 7)
            l_average = round(sum(new_cases[state][0:6]) / 7)
            try:
                percent = (t_average - l_average) / l_average
            except(ZeroDivisionError):
                percent = 0
            if percent > 0:
                print(f"{state} had a 7-day average of {t_average} and an increase of {percent:.2f}%.")
            elif percent < 0:
                print(f"{state} had a 7-day average of {t_average} and an decrease of {-percent:.2f}%.")
            else:
                print(f"{state} had a 7-day average of {t_average} and no increase or decrease.")



main()
