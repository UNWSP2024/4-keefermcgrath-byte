# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0      # initialize for while loop
    total = 0.0

    # Get monthly budget
    budget = float(input("Enter your monthly budget: "))

    # Loop to collect expenses
    while spent != 0:
        spent = float(input("Enter an expense (0 to finish): "))
        total += spent

    # Calculate difference
    difference = budget - total

    # Display results
    if difference > 0:
        print("You are under budget by $" + format(difference, ".2f"))
    elif difference < 0:
        print("You are over budget by $" + format(abs(difference), ".2f"))
    else:
        print("You spent exactly your budget.")


if __name__ == '__main__':
    main()