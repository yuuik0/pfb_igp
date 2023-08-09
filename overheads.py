import csv
from pathlib import Path
fp = Path.cwd()/"csv_reports"/"overheads.csv" #defines the file path to the csv report
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
day = [] # creates an empty list
for item in expenseRecords: 
    # if item not in day, append item to day
    if item[0] not in day:
        day.append(item[0])
# print(day)

expense = [] #creates and empty list
for item in expenseRecords:
    # if item not in expense, append item to day
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
    """
    - calculates the total expense from each categories
    - parameter required: expenseRecords (list of expenses through the days)
    """
    total_exp = 0 #creates variable and assigns it with the value 0
    for item in expenseRecords: #iterates the items in expenseRecords
        expense_categories[item[1]] += int(item[2]) #calculates the expenses from the different categories and adds them up per category
        total_exp += int(item[2]) # calculates the total expenses by summing up all the amounts from every transaction

    return total_exp #returns the total expenses from the different categories
total_expense(expenseRecords)

def overhead_function(expense_categories):
    """
    - Finds out which expense category is the highest along with its percentage
    - parameters required: expense_categories 
    """
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
        expense_categories[item[1]] += int(item[2]) #calculates the expenses from the different categories and adds them up per category
    # Initialise variables to track the highest expense category and highest amount
    highest_expenseCategory = None 
    highest_amount = 0 #creates variable and assigns it with the value of 0
    for expense, amount in expense_categories.items(): 
        if amount > highest_amount: # Check if the current amount is greater than the highest_amount
            # If the condition is met, the key(expense), from the dictionary will be updated into the variable
            highest_expenseCategory = expense
            # If the condition is met, the amount from the value pair of the dictionary will be updated into the variable
            highest_amount = amount
     #retruns the highest expense category, as well as the expense incurred in percentage over the total expenses 
    return f"[HIGHEST OVERHEAD] {str(highest_expenseCategory).upper()}: {round(highest_amount/ total_expense(expenseRecords) * 100, 2)}%\n"

print(overhead_function(expense_categories))

