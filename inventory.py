import os
import msvcrt

#========The beginning of the class Shoe==========
# class shoe is initialized with object country, code, name (product in text file), price (cost in text file) and quantity 
class Shoe:

    def __init__(self, country, code, name, price, quantity):
       
       self.country = country
       self.code = code
       self.name = name
       self.price = price 
       self.quantity = quantity
# this methot return price for product
    def get_price(self):
        
        return self.price
# this method return quantity of product 
    def get_quantity(self):
        
        return self.quantity
# this method return a string to display. Is used in func 'view all' 
    def __str__(self):
        
        return f'''
    Country:            {self.country}
    Code:               {self.code}
    Product:            {self.name}
    Price:              {self.price}
    Quantity:           {self.quantity}
                '''

#=============Shoe list global variable of total objects ===========

shoe_list = []
message = 'Select option and press enter:' # message used for user input from menu 
#==========Functions outside the class==============
# display_menu - is called with option select to display diferent menu for each part of the program
def display_menu(option_select):

    if option_select == 0: # main menu
        os.system('cls') # clear terminal befre display
        print('''
================================\n
    MENU\n
    ================================\n
        1 - View all shoes\n
        2 - Restock shoe\n
        3 - Search for shoe\n
        4 - Calculate stock value\n
        5 - Display shoe with highest or lowest stock value\n
        6 - Exit\n
        ================================\n
              ''')
    elif option_select == 1: # search main menu 
        os.system('cls')
        print('''================================\n
            SEARCH SUBMENU\n
               ================================\n
               1 - Search by country\n
               2 - Search by code\n
               3 - Search by product name\n
               4 - Search by price\n
               5 - Search by stock quanity\n
               6 - Return to main menu\n
               ================================\n
              ''')
    elif option_select == 2: # search submenu 
        print('''================================\n
            WOULD YOU LIKE TO:\n
               ================================\n
               1 - Search and item by code to restock\n
               2 - View all items and select\n
               3 - Return to main menu\n
               ================================\n
              ''')
    elif option_select == 3:    # product with lowest or highest stock main menu 
        print('''================================\n
            WOULD YOU LIKE TO:\n
               ================================\n
               1 - Display product with lowest stock\n
               2 - Display product with highest stock\n
               3 - Return to main menu\n
               ================================\n
              ''')
    elif option_select == 4:    # product with lowest or highest stock submenu
        print('''================================\n
            WOULD YOU LIKE TO RESTOCK:\n
               ================================\n
               1 - Yes\n
               2 - No\n
               ================================\n
              ''')
    elif option_select == 5: # sub menu for highest stock menu above (option 2) 
        print('''================================\n
            WOULD YOU LIKE TO DISCOUNT THE PRICE:\n
               ================================\n
               1 - Yes\n
               2 - No\n
               ================================\n
              ''')
    elif option_select == 6:    # menu if search fave returned no results 
        print('''================================\n
            WOULD YOU LIKE TO:\n
               ================================\n
               1 - Start again\n
               2 - Return to main menu\n
               ================================\n
              ''')
    elif option_select == 7: # first run program menu 
        print('''================================\n
            HELLO! WAHT WOULD YOU LIKE TO DO:\n
               ================================\n
               1 - Open original inventory\n
               2 - Open last updated inventory\n
               ================================\n
              ''')

# function below validate user input options (for options with numbers only) - is reused for menus and data inputs
# it take max_option - parameter to check for number of option depend on the case 
# eg: if max option is 3 we only can enter options up to 3 else return error 
# # menu - display menu depend of the case eg: 'Select option and press enter' 
def user_menu_selection(max_option, menu):

    while True:
        try:
            option_select = int(input(menu))
            while option_select < 1 or option_select > max_option:
                print(f"Please select one option from 1 to {max_option} !")
                option_select = int(input(menu))
            break
        except ValueError:
            print("Your selection need to ne an integer number!")
    return option_select

# function bellow ask user to enter space to continue without pressing enter 
# switch is by default 0 but can be adjusted for other keys if required future 
# by adding more options for switch  
def press_key(switch):
    if switch == 0:
        key = 'a' 
        while key != ' ':
            print("Press space to clear and return to main menu.")
            clear = msvcrt.getch()
            if clear == b' ':
                display_menu(0)
                break
            else:
                print("Press space to clear and return to main menu.")

#function bellow is for selecting the options from main menu 
def menu():
    option_select = 0
    display_menu(0)
    while option_select != 6:
        option_select = user_menu_selection(6, message) # select from main menu (6 elements max)
        if option_select == 1:
            view_all(shoe_list)
            press_key(0)
        
        elif option_select == 2:
            re_stock(0, shoe_list)

        elif option_select == 3:
            search_shoe()

        elif option_select == 4:
            value_per_item()

        elif option_select == 5:
            highest_qty()
# if user press 6 to exit we offer the option to save the changes in an updated_inventory file if required
        elif option_select == 6:
            while True:
                save = input("Would you like to save changes in updated database (Y / N): ").lower()
                if save == 'y':
                    save_inventory()
                    break
                elif save == 'n':
                    break
                else:
                    continue
            print("Goodbye!")
            exit()

# function bellow open and read the inventory file and return the result as a list
# it offer 2 option to the user: 
# 1 - to read from original inventory( inventory.txt) or 2 - to read from last updated inventory (updated_inventory) 
# option 2 can modify the updated_inventory.txt each time we run the program 
# if no file is present return error and offer the option to open original inventory or leave the program
# take as parameter name of the fle to open - this permit futer adjustment in the futer for other options 
def read_shoes_data(text_file):
    dir = os.getcwd()
    os.chdir(dir)
    fo = None
    try:
        inventory_content = []
        fo = open(text_file, "r")
        inventory_content = fo.readlines()
        fo.close()
    except FileNotFoundError:   # return error if file not found and offer the option to open original inventory
        print("\n **** Inventory file not found!*** \n")
        while True: 
            user_input = input('''Would you like to open original inventory?
                                    Y - open original inventory
                                    N - exit program
                            ''').lower()
            if user_input == 'y':
                capture_shoes(0)
                menu()
                break
            elif user_input == 'n': # else offer the option to leave program 
                print("\n ***Goodbye! *** \n")
                exit()
            else:
                continue
    finally:
        if fo is not None:
            fo.close()
    inventory_content.pop(0)
    return inventory_content

# function bellow save the inventory if option 6 in main menu is selected and option 'Y' to save
# it save all changes the user have made in the run in updated_inventory.txt to be used later on if required
def save_inventory():
    update_data = 'Country,Code,Product,Cost,Quantity\n'
    for x in shoe_list:
        update_data += x.country + ',' + x.code + ','+ x.name + ',' 
        update_data += str(x.price) + ',' + str(x.quantity) + "\n"
    with open('updated_inventory.txt', 'w') as f:
        f.write(update_data)

# function bellow create a list 'shoe_list' with all the data from text file 
# text file is read in read_shoe_data 
# it take parameter switch to select and transmit which file we read depend of user choice at the first run of program         
def capture_shoes(switch):
    if switch == 0:
        inventory_content = read_shoes_data('inventory.txt')
    else:
        inventory_content = read_shoes_data('updated_inventory.txt')
    for item in inventory_content:
        item2 = item.strip('\n')
        item1 = item2.split(',')
        shoe_list.append(Shoe(item1[0], item1[1], item1[2], item1[3], item1[4]))

# function bellow display all product from the list (stock)
# take the list of objects as argument 
# use enumerate to show number of items in the same time 
def view_all(data):
    for pos, value in enumerate(data):
        print(f"{'-' * 20}[{pos + 1}]{'-' * 20} \n")
        print(value, "\n")

# function bellow change stock value of a product (entered by user) 
# offer 3 options : 
# 1 - to find the product to restock by product code 
# 2 - ti display all products and select product by number 
# 3 - to return to main menu
# take switch - an option that can change based from where we calling the function and the stock list
# function can be reused for other options if required    
def re_stock(switch, data):
    t = False #detect if no product has been found 
    option_select = 0
    message1 = 'Enter new quantity: '
    if switch == 0: # we only use this option for main menu selection 
        display_menu(2)
        option_select = user_menu_selection(3, message)
    else:       
        option_select = 2   # this option is used for menu selection and used by other function (lowest and highest)
    if option_select == 1:  # offer the option to search by product code
        product_code = input("Enter product code: ").lower()
        for p in shoe_list:
            x=p.code
            if x.lower() == product_code:
                p.quantity = user_menu_selection(float('inf'), message1)
                t = True
        if not t:
            print("\n **Product code not found in database!** \n")
            press_key(0)
        else:
            print("\n **Restock succesfully!** \n")
            press_key(0)
    elif option_select == 2: #offer option to select from a list of all items 
        view_all(data)
        message2 = 'Enter item number that you would like to restock: '
        end = len(data)
        item_nr = user_menu_selection(end, message2 )
        item = data[item_nr - 1]
        item.quantity = user_menu_selection(float('inf'), message1)
        print("\n ** Restock succesfuly! ** \n")
        press_key(0)
    elif option_select == 3:
        display_menu(0)
    else:
        print("\n ** No option otion selected from menu** \n")
        re_stock(0, data)

# this function search for a shoe in shoe list 
# allows the user to search by every aspect of the object (country, code, name, price, quantity)
def search_shoe():
    display_menu(1)
    option_select = user_menu_selection(6, message) # take input of max 6 elements
    t = False
    if option_select == 1:
        u_input = input(f"Product country: ").lower()
        for x in shoe_list:
            if x.country.lower() == u_input:
                print(x, "\n")
                t = True
        if t:               # control variable await for user to press space bar. Allow time to read the results
            press_key(0)
    elif option_select == 2: 
        u_input = input(f"Product code: ").lower()
        for x in shoe_list:
            if x.code.lower() == u_input:
                print(x, "\n")
                t = True
        if t:
            press_key(0)
    elif option_select == 3:     
        u_input = input(f"Product name: ").lower()
        for x in shoe_list:
            if x.name.lower() == u_input:
                print(x, "\n")
                t = True
        if t:
            press_key(0)
    elif option_select == 4:
        u_input = input(f"Product price: ").lower()
        for x in shoe_list:
            if x.price.lower() == u_input:
                print(x, "\n")
                t = True
        if t:
            press_key(0)
    elif option_select == 5:
        u_input = input(f"Product quantity: ").lower()
        for x in shoe_list:
            if x.quantity.lower() == u_input:
                print(x, "\n")
                t = True
        if t:
            press_key(0)
    elif option_select == 6:
        display_menu(0)
        t = True
# if no product found (t = False) return the option to search again (restart function)
# or the option to return to main menu 
    if not t:   
        print("\n ** No product found with this search criteria! **\n")
        display_menu(6)
        o = user_menu_selection(2, message)
        if o == 1:
            search_shoe()
        else:
            display_menu(0)

#  the bellow function display the value stock for each product
# it also display the total stock 
# allow user to read the results (ask for space bar in order to exit)      
def value_per_item():  
    total_stock = 0 # count total stock as we go through function 
    i = 1
    for x in shoe_list:
        s_value = float(x.get_price()) * int(x.get_quantity())
        print(f"Item [{i}] {'-' * 50}")
        print(f'''{x}  
Stock Value:            {s_value} \n''')
        total_stock += s_value 
        i += 1
    print(f"\n ** Total stock value is {total_stock} **\n")
    press_key(0)

# the function bellow display the the product(s) with lowest quantity and highest quantity in list
# it can display multiple products if they are of the same max or min value 
# once found the min stock product offer the option to restock by calling func. re_stock
# it make use of the function view all - to display lowest and highest quantity products 
# also take in account that we can have more low or high quant. items with the same quant value 
# make use of fuck display menu - to display menu and submenu 
#make use of function price discount to change price of the highest quant. item 
# if changes have to be made it allow the user to select the item they want to modify
def highest_qty():
    qtt = []
    for x in shoe_list:
        qtt.append(x.quantity)
    qtt = [int(x) for x in qtt]
    lowest = min(qtt)
    highest = max(qtt)
    del qtt
    lowest_qtt_prod = [] # register all lowest products (if more with same value)
    highest_qtt_prod = [] # register all highes quant products (if more with same value)
    for x in shoe_list:
        if x.get_quantity() == str(lowest):
            lowest_qtt_prod.append(x)
        elif x.get_quantity() == str(highest):
            highest_qtt_prod.append(x)
        else:
            continue
    display_menu(3)
    sel = user_menu_selection(3, message)
    if sel == 1:  # display prod with lowest stock and allow operations 
        print("Product(s) with lowest stock: ")
        view_all(lowest_qtt_prod)
        display_menu(4)
        op = user_menu_selection(2, message)
        if op == 1:
            re_stock(1, lowest_qtt_prod)
        else:
            display_menu(0)
    elif sel == 2: # display products with highest stock and allow operations 
        print("Products with highest stock: ")
        view_all(highest_qtt_prod)
        display_menu(5)
        op = user_menu_selection(2, message)
        if op == 1:
            price_discount(highest_qtt_prod)
            display_menu(0)
        else:
            display_menu(0)
    else:           # return to main menu 
        display_menu(0)

# the func bellow allow user to modify price ( discount)
# it also display the procentage has been discounted 
def price_discount(data):
    mess = 'Which item would you like to discount:'
    op = user_menu_selection(len(data), mess) - 1
    new_price = float(input("New price: "))
    to_change = data[op]
    for x in shoe_list:
        if x.name == to_change.name:
            old_price = float(x.price)
            x.price = new_price
            procentage = (1 - (new_price / old_price)) * 100
            print("\n **Discount applied succesfuly ** \n")
            print(f" This represent a discount of {int(procentage)}% of the previous price!\n")
            press_key(0)

#========== Main function =============
os.system('cls')
display_menu(7) # let user load original or updated inventory file 
user_input = user_menu_selection(2, message)
if user_input == 1:
    capture_shoes(0)
else:
    capture_shoes(1)
menu()
