# ----- Part 1 -----

#food price
price = float(input("How much was the food?"))

#calculate 18% tip
tip = price * 0.18

#calculate 7% sales tax
tax = price * 0.07

#calculate total price
total = price + tip + tax

# Display all amounts
print("Sumamry of food cost, tip and tax:")
print(f"Food cost: ${price:.2f}")
print(f"Tip amount (18%): ${tip:.2f}")
print(f"Tax amount (7%): ${tax:.2f}")
print(f"Total amount: ${total:.2f}")

# ----- Part 2 -----

#get current time
ctime = int(input("\n\nWhat is the current hour in 24 hour clock format?"))
#get alarm hours
ahours = int(input("How many hours do you want to wait before the alarm goes off?"))
#calculate the hour the alarm will go off
alarm = (ctime + ahours) % 24

#provide user with the time the alarm will go off
print(f"The alarm will go off at {alarm}:00")