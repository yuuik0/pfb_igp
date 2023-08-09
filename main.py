import overheads, cash_on_hand, profit_loss

def main():
    o = overheads.overhead_function(expense_categories= {
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
    })
    c = cash_on_hand.coh_function()
    p = profit_loss.profitloss_function()

    results = f"{o}{c}{p}"
    return results
main()

from pathlib import Path 

# 1. Write the calculated info to the summary_report.txt file.
home = Path.home() 
# print(home) #shows the home directory of my laptop
file_path = home/"OneDrive"/"project_group"/"summary_report.txt"
file_path.touch() #creating summary_report.txt file
# print(file_path)
# print(file_path.exists()) #checking that the file exists in the computer

with file_path.open(mode = "w", encoding = "UTF-8") as file:
    file.writelines(main())

