
#Part1: Rainfall Calculator
def rainfall_calculator():
    #years count
    years = int(input("Enter the number of years: "))
    
    #create variables
    total_rainfall = 0.0
    total_months = 0
    
    #outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        
        #inner loop for each month
        for month in range(1, 13):
            #get rainfall by month
            rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
            #calculate total rainfall
            total_rainfall += rainfall
            #month counter
            total_months += 1
    
    #avg rainfall
    average_rainfall = total_rainfall / total_months
    
    #results
    print(f"Number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

#Part 2: Bookstore Points Calculator
def bookstore_points():
    #number of books purchased
    books = int(input("Enter the number of books purchased this month: "))
    
    #points counter
    if books <= 1:
        points = 0
    #2 or 3 points gives 5
    elif books <= 3:
        points = 5
    #5 or 4 points gets 15
    elif books <= 5:
        points = 15
    #7 or 6 points gets 30
    elif books <= 7:
        points = 30
    #8 or more gets 60 points
    elif books >= 8:
        points = 60
    else:
        #calculating these odd values because it doesn't make sense to get zero points when at odd numbers
        points = 0
    
    #results
    print(f"Books purchased: {books}")
    print(f"Points awarded: {points}")


#create a router to select program to use
def main():
    print("Main menu to select which program to run.")
    while True:
        print("\n" + "Select a Program")
        print("1. Rainfall Calculator")
        print("2. Bookstore Points Calculator")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            rainfall_calculator()
        elif choice == '2':
            bookstore_points()
        elif choice == '3':
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


#run the program
if __name__ == "__main__":
    main()