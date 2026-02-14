# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    years = int(input("Enter the number of years: "))
    
    total_rainfall = 0.0
    total_months = 0

    # Outer loop (for each year)
    for year in range(1, years + 1):
        print("\nYear", year)

        # Inner loop (12 months)
        for month in range(1, 13):
            rainfall = float(input(f"Enter rainfall for month {month}: "))
            total_rainfall += rainfall
            total_months += 1

    # Calculate average
    average_rainfall = total_rainfall / total_months

    # Display results
    print("\nNumber of months:", total_months)
    print("Total rainfall:", total_rainfall, "inches")
    print("Average rainfall per month:", format(average_rainfall, ".2f"), "inches")


if __name__ == '__main__':
    main()