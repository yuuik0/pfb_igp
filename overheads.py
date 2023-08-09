import csv
from pathlib import Path
fp = Path.cwd()/"csv_reports"/"overheads.csv" #defines the file path to the cvs report
# print(fp.exists())

#create an object named "reader" to read the csv file if the path exists
with fp.open(mode="r", encoding= "UTF-8", newline= "") as file: 
    reader = csv.reader(file) # created object named "reader"
    next(reader) #skips the header row

    expenseRecords = []

    for row in reader:
        # appends the respective rows from the overheads csv to into the expenseRecords
        expenseRecords.append([row[0], row[1], row[3]])
# print(expenseRecords)

# creates a list of unique days from expenseRecords
day = []
for item in expenseRecords:
    if item[0] not in day:
        day.append(item[0])
# print(day)

expense = []
for item in expenseRecords:
    if item[1] not in expense:
        expense.append(item[1])
# print(expense)

expense_categories = {
    "Salary Expense": 0,
    "Marketing Expense": 0,
    "Shipping Expense": 0,
    "Rental Expense": 0,
    "Human Resource Expense": 0,
    "Maintenance Expense": 0,
    "Overflow Expense - Retail": 0,
    "Depreciation Expense": 0,
    "Interest Expense ": 0,
    "Penalty Expense": 0,
}

def total_expense(expenseRecords):
    total_exp = 0
    for item in expenseRecords:
        expense_categories[item[1]] += int(item[2])
        total_exp += int(item[2])

    return total_exp
total_expense(expenseRecords)

def overhead_function(expense_categories):
    expense_categories = {
        "Salary Expense": 0,
        "Marketing Expense": 0,
        "Shipping Expense": 0,
        "Rental Expense": 0,
        "Human Resource Expense": 0,
        "Maintenance Expense": 0,
        "Overflow Expense - Retail": 0,
        "Depreciation Expense": 0,
        "Interest Expense ": 0,
        "Penalty Expense": 0,
    }
    for item in expenseRecords:
        expense_categories[item[1]] += int(item[2])
    highest_expenseCategory = None
    highest_amount = 0
    for expense, amount in expense_categories.items():
        if amount > highest_amount:
            highest_expenseCategory = expense
            highest_amount = amount
    return f"[HIGHEST OVERHEAD] {str(highest_expenseCategory).upper()}: {round(highest_amount/ total_expense(expenseRecords) * 100, 2)}%\n"

print(overhead_function(expense_categories))

