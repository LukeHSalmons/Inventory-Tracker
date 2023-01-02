#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Returns cost of the shoes
    def get_cost(self):
        return self.cost

    # Returns quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # Returns string representation of the class
    def __str__(self):
        return f"Country: {self.country} || Code: {self.code} || Product: {self.product} || Cost: {self.cost} || Quantity: {self.quantity}"


#=============Shoe list===========
shoe_list = []


#==========Functions outside the class==============
# Read inventory.txt file, create objects and append to shoe list
def read_shoes_data():
    try:
        with open("inventory.txt", "r+") as file:
            next(file)
            # Split each line into seperate elements
            for line in file:
                line = line.strip().split(",")
                country = line[0]
                code = line[1]
                product = line[2]
                cost = int(line[3])
                quantity = int(line[4])

                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    # Print error if file not found
    except FileNotFoundError:
        print("\nSorry, this file can not be found!")


def capture_shoes():
        # Get user input
        country = input("Please enter the country the shoe is from: ")
        code = input("Please enter the code of the shoe: ")
        product = input("Please enter the product type of the shoe: ")
        cost = int(input("Please enter the cost of the shoe: "))
        quantity = int(input("Please enter the quantity of the shoe: "))

        # Append new shoe to inventory.txt file
        with open("inventory.txt", "a+") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")

        # Instantiate Shoe object and append object to shoe list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        print("\nThank you! This shoe has been added to the inventory.")


def view_all():
    # Print out __str__ method for each shoe object
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    # Set lowest quantity and lowest quantity shoe object to first shoe in list as default
    lowest_quantity = shoe_list[0].quantity
    lowest = shoe_list[0]

    # Loop through each shoe in shoe list, updating lowest & lowest_quantity with the lowest value
    for shoe in shoe_list:
        if shoe.quantity < lowest_quantity:
            lowest_quantity = shoe.quantity
            lowest = shoe

    print(f"\nThe lowest quantity of shoe is {lowest.product} with a quantity of {lowest.quantity}")
    decision = int(input("\nPlease enter the amount you would like to increase quantity by or enter -1 to keep quantity as is: "))

    # Update shoe quantity based on user input
    if decision == -1:
        return "\nThank you! The quantity has not been changed"
    elif decision > 0:
        lowest.quantity += decision
    else:
        return "\nSorry, you did not enter a valid number"

    # Overwrite inventory.txt file with data from shoe list
    with open("inventory.txt", "w+") as file:
        file.write("Country,Code,Product,Cost,Quantity")
        for my_shoe in shoe_list:
            file.write(f"\n{my_shoe.country},{my_shoe.code},{my_shoe.product},{my_shoe.cost},{my_shoe.quantity}")

    return f"\nThank you! The is show now has a quantity of {lowest.quantity} units."


def search_shoe():
    choice = input("\nWould you like to search by 'code' or 'product'? ")
    
    # Loop through shoe.code in shoe list searching for user input
    if choice == "code":
        code = input("Please enter the shoe code you would like to search for: ")
        for shoe in shoe_list:
            if shoe.code == code:
                return shoe
        return "\nSorry, this shoe code is not in the inventory!"

    # Loop through shoe.product in shoe list searching for user input
    elif choice == "product":
        product = input("Please enter the shoe product you would like to search for: ")
        for shoe in shoe_list:
            if shoe.product == product:
                return shoe
        return "\nSorry, this shoe product is not in the inventory!"

    else:
        return "\nSorry that is an invalid input"

# Loop through each shoe in shoe list displaying the total value of each shoe
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Country: {shoe.country}, Code: {shoe.code}, Product: {shoe.product}, Value: {value}")


def highest_qty():
    # Set highest quantity and highest quantity shoe object to first shoe in list as default
    highest_quantity = shoe_list[0].quantity
    highest = shoe_list[0]

    # Loop through each shoe in shoe list, updating highest & highest_quantity with the highest value
    for shoe in shoe_list:
        if shoe.quantity > highest_quantity:
            highest_quantity = shoe.quantity
            highest = shoe

    print(f"\nYou have a high quantity of {highest.product} with {highest.quantity} units. This shoe should go on sale.")


#==========Main Menu=============
# Run function to read data from inventory so shoe_list can be viewed/altered below
read_shoes_data()

# Get user input for menu
while True:
    choice = input('''\nPlease choose from the following options:
Add - Add to the list
View - View all items in the inventory
Re-stock - Restock the lowest quantity
Search - Search for shoe in inventory
Values - Display values for each shoe in inventory
Highest - Display the shoe with the highest quantity
Quit - Quit the application
''').lower()

    if choice == "add":
        capture_shoes()
    elif choice == "view":
        view_all()
    elif choice == "re-stock":
        print(re_stock())
    elif choice == "search":
        print(search_shoe())
    elif choice == "values":
        value_per_item()
    elif choice == "highest":
        highest_qty()
    elif choice == "quit":
        break
    else:
        print("\nSorry, that is not a valid input! Please try again...")