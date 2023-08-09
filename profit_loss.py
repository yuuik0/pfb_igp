import csv
from pathlib import Path
# print(Path.cwd())
fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
fp1 = Path.cwd()/"csv_reports"/"profit-and-loss-usd (1).csv"
fp2 = Path.cwd()/"csv_reports"/"profit-and-loss-usd (2).csv"


# print(fp.exists())
# print(fp1.exists())
# print(fp2.exists())

# create an empty list to store profit and loss records
pnlRecords = []

# read data from the first CSV file (fp)
with fp.open(mode="r", encoding= "UTF-8", newline= "") as file:
    reader = csv.reader(file)
    next(reader)

# Iterate through the rows in the CSV and append relevant columns
    for row in reader:
        pnlRecords.append([row[0], row[1], row[2], row[3], row[4]])

with fp1.open(mode="r", encoding= "UTF-8", newline= "") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        pnlRecords.append([row[0], row[1], row[2], row[3], row[4]])

with fp2.open(mode="r", encoding= "UTF-8", newline= "") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        pnlRecords.append([row[0], row[1], row[2], row[3], row[4]])

# print(pnlRecords)

day = []
for item in pnlRecords:
    if item[0] not in day:
        day.append(item[0])
# print(day)

daily_amt = {}
def daily_amounts(pnlRecords):
    # Calculate daily net profits and store them in the daily_amt dictionary 
    for item in pnlRecords:
        day = item[0]
        # sales = int(item[1])
        # trading_prof = int(item[2])
        # operating_exp = int(item[3])
        net_prof = int(item[4])

        if day in daily_amt:
            daily_amt[day] += net_prof
        else:
            daily_amt[day] = net_prof

    return daily_amt

# Calculate daily net profits using the daily amounts function
daily_amounts(pnlRecords)

def profitloss_function():
    netProfit_surplus = True
    highest_surplus = 0
    day_with_highest_surplus = None
    deficits = {}

    previous_np = None
    daily_diff = {}
    for day, netprofit in daily_amt.items():
        if previous_np is not None:
            diff = netprofit - previous_np
            daily_diff[day] = diff

          # check if the difference is deficit or surplus
            if diff < 0:
                netProfit_surplus = False
                deficits[day] = -diff
            elif diff > highest_surplus:
                highest_surplus = diff
                day_with_highest_surplus = day

        previous_np = netprofit

    result = ""

  # generate the result string based on net profit surplus or deficits
    if netProfit_surplus:
        result += f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        result += f"[HIGHEST NET PROFIT SURPLUS] DAY:{day_with_highest_surplus}, AMOUNT: USD{highest_surplus}"    
    else:
        for day, deficit in deficits.items():
            result += f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n"
    
    return result

print(profitloss_function())
