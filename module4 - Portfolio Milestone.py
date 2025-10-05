#Step 1:  Build the ItemToPurchase class
class ItemToPurchase: 
    def __init__(self): #default constructor
        self.item_name = "none" #attribute 1
        self.item_price = 0 #attribute 2
        self.item_quantity = 0 #attribute 3
    
    def print_item_cost(self): #method print_item_cost()
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}") #output as required Example of print_item_cost() output: - Bottled Water 10 @ $1 = $10

#Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
#first prompt:
print("Item 1")
name1 = input("Enter the item name:\n")
price1 = float(input("Enter the item price:\n"))
quantity1 = int(input("Enter the item quantity:\n"))

#first ItemToPurchase object
item1 = ItemToPurchase()
item1.item_name = name1
item1.item_price = price1
item1.item_quantity = quantity1

#second prompt
print("\nItem 2")
name2 = input("Enter the item name:\n")
price2 = float(input("Enter the item price:\n"))
quantity2 = int(input("Enter the item quantity:\n"))

#second ItemToPurchase object
item2 = ItemToPurchase()
item2.item_name = name2
item2.item_price = price2
item2.item_quantity = quantity2


#Step 3: Add the costs of the two items together and output the total cost.

print("\nTOTAL COST")
item1.print_item_cost() #print first item as per method created
item2.print_item_cost() #print second item as per method created

#calculate and print total
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost:.0f}")