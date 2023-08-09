import csv
from pathlib import Path

fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv" #printing the file path of the csv
# print(fp.exists())

# create an object named 'reader' to print the line if the path exists
with fp.open(mode="r", encoding= "UTF-8", newline= "") as file:
    reader = csv.reader(file)
    next(reader)

    cashRecords = [] #create an empty list to store the information from the cash_on_hand csv

    for row in reader:
        cashRecords.append([row[0], row[3]]) 
        #appends the day(row[0]) and amount(row[3]) from each row in the cash_on_hand csv into the cashRecords list
# print(cashRecords)

# gets a list of unique days
day_list = [] #create an empty list, day_list
for item in cashRecords:
    #if day is not in day_list, append day into day_list
    if item[0] not in day_list:
        day_list.append(item[0])
day_list.reverse() #changes the order of the days in day_list to go from smallest to largest
# print(day_list)

# calculation of total cash on hand over 90 days
total_coh = 0 # created a variable, total_coh and assigned it to the value 0
for item in cashRecords: #now, the code will go through the items in the cashRecords 
    total_coh += int(item[1]) 
    # adds up all the values of the cash on hand amounts from the cashRecords list and adds it back to the variable to get the total cash on hand
# print(total_coh)

#calculates the daily amount of cash on hand
def daily_coh(cashRecords):
    daily_cash = {} #creates an empty dictionary to store the daily cash earned
    for item in cashRecords:
        day = item[0]
        cash = int(item[1])

        if day in daily_cash:
            daily_cash[day] += cash
        else:
            daily_cash[day] = cash

    return daily_cash

daily_cash = daily_coh(cashRecords)

reversed_daily_cash = {}
previous_total = 0
for day, cash in reversed(daily_cash.items()):
    previous_total += cash
    reversed_daily_cash[day] = previous_total

# print(reversed_daily_cash)


def coh_function():
    cash_surplus = True
    highest_surplus = 0
    day_with_highest_surplus = None
    deficits = {}

    previous_cash = None
    daily_diff = {}
    for day, cash in reversed_daily_cash.items():
        if previous_cash is not None:
            diff = cash - previous_cash
            daily_diff[day] = diff

            if diff < 0:
                cash_surplus = False
                deficits[day] = -diff
            elif diff > highest_surplus:
                highest_surplus = diff
                day_with_highest_surplus = day

        previous_cash = cash

    result = ""
    if cash_surplus:
        result += f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        result += f"[HIGHEST CASH SURPLUS] DAY: {day_with_highest_surplus}, AMOUNT: USD{highest_surplus}"
    else:
        for day, deficit in deficits.items():
            result += (f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n")
    return result

print(coh_function())
