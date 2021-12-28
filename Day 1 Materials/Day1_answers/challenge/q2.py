
menu = {'RC': {'description': 'Roast Chicken Sandwich', 'price': 4.50, 'Qty': 5},
        'SB': {'description': 'Spicy Beef Sandwich', 'price': 5.50, 'Qty': 15},
        'MC': {'description': 'Mushroom Cheese Sandwich', 'price': 3.40, 'Qty': 5},
        'CC': {'description': 'Classic Club Sandwich', 'price': 5.70, 'Qty': 0},
        'IM': {'description': 'Impossible Meat Sandwich', 'price': 4.80, 'Qty': 10}}

#print vending machine menu
def displayMenu():
    print('Welcome to Quick Bites Sandwich Vending Machine')
    for key in menu:
        if menu[key]['Qty'] == 0:
            menu[key]['Qty'] = '*out of stock*'
            print(f"{key}.  {menu[key]['description']} ----- ${menu[key]['price']} {menu[key]['Qty']}")
        elif menu[key]['Qty'] != 0:
            print(f"{key}.  {menu[key]['description']} ----- ${menu[key]['price']}")
    print('0.   Exit / Payment')
    print("Select from the following choices to continue:")

#selecting from menu
def selectItem():
    count = 0
    totalPrice = 0
    using = True
    while using:
        choice = input("Enter choice: ").upper()
        if choice in menu:
            if menu[choice]['Qty'] == '*out of stock*':
                print(f"Sorry, the {menu[choice]['description']} is out of stock")
            else:
                count += 1
                price = menu[choice]['price']
                totalPrice += price
                print(f"You have selected the {menu[choice]['description']}")
        elif choice == "0":
            using = False
            if choice == '0' and count >= 1:
                print(f"Please pay ${totalPrice}")
            print("Have a nice day!")
        elif choice not in menu:
            print("Invalid choice, try again!")
            continue

displayMenu()
selectItem()
