import csv
from pathlib import Path

fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv" # Defines the file path to the csv report
# print(fp.exists())

# create an object named 'reader' to read the CSV file if the path exists
with fp.open(mode="r", encoding= "UTF-8", newline= "") as file:
    reader = csv.reader(file)
    next(reader) # Skips the header row

    cashRecords = [] #create an empty list to store the information from the cash_on_hand csv

    for row in reader:
        cashRecords.append([row[0], row[3]]) 
        #appends the day(row[0]) and amount(row[3]) from each row in the cash_on_hand csv into the cashRecords list
# print(cashRecords)

# creates a list of unique days from cashRecords
day_list = [] #create an empty list, day_list
for item in cashRecords:
    #if day is not in day_list, append day into day_list
    if item[0] not in day_list:
        day_list.append(item[0])
day_list.reverse() #reverses the order of the days in day_list to go from smallest to largest (chronological order)
# print(day_list)

# calculation of total cash on hand over 90 days
total_coh = 0 # created a variable, total_coh and assigned it to the value 0
for item in cashRecords: #now, the code will iterate through the items in the cashRecords list
    total_coh += int(item[1]) 
    # adds up all the values of the cash on hand amounts from the cashRecords list and adds it back to the variable to get the total cash on hand
# print(total_coh)

def daily_coh(cashRecords):
    """
    - one parameter required; cashRecords (list containing of the days and amount of cash per transaction)
    - calculates the daily amount of cash on hand
    """
    daily_cash = {} #creates an empty dictionary to store the daily cash earned
    for item in cashRecords:
        day = item[0] #Extracts the number of days from the cashRecord
        cash = int(item[1]) # Extracts the cash amount from the cashRecords and converts it into an integer 

        #checks if the day is already in the dictionary
        if day in daily_cash:
            #if it is in the dictionary, the cash amount for the day will be added up
            daily_cash[day] += cash
        else:
            #if it is not in the dictionary yet, a new entry would be created.
            daily_cash[day] = cash

    return daily_cash #returns the daily cash amount in the dictionary with day/amount as the key/value pair.

daily_cash = daily_coh(cashRecords)

#created a dictionary to store the daily cash totals reversed
reversed_daily_cash = {}
previous_total = 0
# the code will iterate through the daily_cash dictionary and list out the items in a reversed order
for day, cash in reversed(daily_cash.items()):
    previous_total += cash
    reversed_daily_cash[day] = previous_total

# print(reversed_daily_cash)


def coh_function():
    """
    - No parameters required
    - Analyses cash flow, showing if there is a deficit or surplus of the cash on hand
    """
    cash_surplus = True
    highest_surplus = 0
    day_with_highest_surplus = None
    deficits = {}

    previous_cash = None
    daily_diff = {}

    #iterates through the reversed_daily_cash dictionary
    for day, cash in reversed_daily_cash.items():
        if previous_cash is not None:
            diff = cash - previous_cash
            daily_diff[day] = diff

            #determining if there is a cash deficit or surplus when compared to the previous day
            if diff < 0:
                cash_surplus = False
                deficits[day] = -diff #helps to make the difference in the amount positive
            elif diff > highest_surplus:
                highest_surplus = diff
                day_with_highest_surplus = day

        previous_cash = cash

    result = ""
    # if a cash surplus was present every day, the code will mention that there was a constant cash surplus and state the day with the highest surplus amount.
    if cash_surplus:
        result += f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        result += f"[HIGHEST CASH SURPLUS] DAY: {day_with_highest_surplus}, AMOUNT: USD{highest_surplus}"
    # if there was a cash deficit, the code would iterate through the amounts in the deficits dictionary and print the day as well as the deficit amount out.
    else:
        for day, deficit in deficits.items():
            result += f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n"
    return result

#call for the function and prints the results
print(coh_function())
