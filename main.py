# Importing each of the required python file as modules
import overheads, cash_on_hand, profit_loss

# assists in modularizing the program
def main():
    """
    - No parameter required
    - Imports, coordinates, and executes the functions from overheads, cash_on_hand, and profit_loss modules, returning the combined result of the functions as a string
    """
    # the functions in each module are being called for in this main function
    overhead = overheads.overhead_function(expense_categories= {
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
    coh = cash_on_hand.coh_function()
    pnl = profit_loss.profitloss_function()

    # the results of all three modules are then combined, converted into an f string, and returned by the function
    results = f"{overhead}{coh}{pnl}"
    return results
# Execution of main function
main()

from pathlib import Path 

# Writes the calculated info to the summary_report.txt file.
home = Path.home() 
# print(home) #shows the home directory of my laptop
file_path = home/"OneDrive"/"project_group"/"summary_report.txt"
file_path.touch() #creating summary_report.txt file if it doesnt exist
# print(file_path)
# print(file_path.exists()) #checking that the file exists in the computer

# opens file with .open() to create a file object
with file_path.open(mode = "w", encoding = "UTF-8") as file:
    # uses .writelines() to write down the multiple lines of results from the main() function into the summary_report.txt file
    file.writelines(main())

