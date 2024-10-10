"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    get_income(incomes, number_of_months)

    display_report(incomes, number_of_months)


def get_income(incomes, number_of_months):
    """Get the income from user"""
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)


def display_report(incomes, number_of_months):
    """Display the income report data to the user"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month} - Income: ${income:6}  Total: ${total:6}")


main()