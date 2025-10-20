#Step 1:  Build the ItemToPurchase class
class ItemToPurchase: 
    def __init__(self): #default constructor
        self.item_name = "none" #attribute 1
        self.item_price = 0 #attribute 2
        self.item_quantity = 0 #attribute 3
        self.item_description = "none" #attribute 4
    
    def print_item_cost(self): #method print_item_cost()
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}") #output as required
    
    def print_item_description(self): #method print_item_description()
        print(f"{self.item_name}: {self.item_description}")


#Step 4: Build the ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"): #parameterized constructor
        self.customer_name = customer_name #attribute 1
        self.current_date = current_date #attribute 2
        self.cart_items = [] #attribute 3
    
    def add_item(self, item): #method add an item with no return
        self.cart_items.append(item) #adds item to cart_items list
    
    def remove_item(self, item_name): #method remove an item with no return if found, else not found
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_modify): #method to modify description, price and/or quantity. no return, unless not found.
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                found = True
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self): #method to return quantity of all items
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self): #method to return total cost
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost
    
    def print_total(self): #method to print totals
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.0f}")
    
    def print_descriptions(self): #method print_descriptions()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


#Step 5: Implement print_menu() function
def print_menu(cart):
    menu = """MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
"""
    
    choice = ''
    while choice != 'q':
        print(menu)
        choice = input()
        
        if choice == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            
            new_item = ItemToPurchase()
            new_item.item_name = item_name
            new_item.item_description = item_description
            new_item.item_price = item_price
            new_item.item_quantity = item_quantity
            cart.add_item(new_item)
            
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
            
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            
            modified_item = ItemToPurchase()
            modified_item.item_name = item_name
            modified_item.item_quantity = new_quantity
            cart.modify_item(modified_item)
            
        elif choice == 'i':
            #Step 6: Output items' descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            print()
            
        elif choice == 'o':
            #Step 6: Output shopping cart
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
            print()
            
        elif choice == 'q':
            break
            
# Main section - testing the code
if __name__ == "__main__":
    # Create test items
    item1 = ItemToPurchase()
    item1.item_name = "Nike Romaleos"
    item1.item_description = "Volt color, Weightlifting shoes"
    item1.item_price = 189
    item1.item_quantity = 2
    
    item2 = ItemToPurchase()
    item2.item_name = "Chocolate Chips"
    item2.item_description = "Semi-sweet"
    item2.item_price = 3
    item2.item_quantity = 5
    
    item3 = ItemToPurchase()
    item3.item_name = "Powerbeats 2 Headphones"
    item3.item_description = "Bluetooth headphones"
    item3.item_price = 128
    item3.item_quantity = 1
    
    # Create shopping cart
    cart = ShoppingCart("John Doe", "February 1, 2020")
    
    # Add items to cart
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    
    # Call print_menu
    print_menu(cart)