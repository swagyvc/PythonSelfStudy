import json

inventory = {}
#User Story
#I want owner can login to see if they have account or no
#                                                => yes -> ask username & password
#                                                => no -> ask enter username & passwords
#                                                       => it will save username & passowds so that they can login and check later
#if yes, they can review their inventory, they can either choose to edit inventory (add/remove/change price)
#after edit they can hit save and review inventory.

def owner():
    # Owner
    #{"Product Name": Price}
    #{"Shoes": 1000, "Shirt": 500}
    


    while True:
        product_name = input("Enter Product Name: ")
        product_price = int(input("Enter Product Price: "))
    
        inventory[product_name] = product_price
        if input("Do you want to add another product? (y/n): ").lower() != "y":
            break

    print(inventory)

# Customer
def customer():

    customer_cart = []
    while True:
        #customer_cart = ["Shoes", "Shirt"]
        customer_item = input("What would you like to buy? ").title()

        if customer_item in inventory:
            customer_cart.append(customer_item)
        else:
            print("Sorry, we don't have that product.")

        if input("Do you want to buy another item? (y/n): ").lower() != "y":
            break

    total_bill = 0
    for i in customer_cart:
        total_bill += inventory[i]

    print(f"Your cart: {customer_cart}")
    print(f"Total Bill: {total_bill}")

    user_id = input("Enter User ID to save your cart: ")

    with open(f"{user_id}.json", "w") as file:
        json.dump(customer_cart, file)

    user_id = input("Enter User ID to load your cart: ")
    with open(f"{user_id}.json", "r") as file:
        loaded_cart = json.load(file)
    print(f"Loaded Cart: {loaded_cart}")

while True:
    user_desicion = input("Are you an Owner or Customer?\n " \
    "1. Owner\n 2. Customer\n 3. Exit\n " \
    "Enter your choice: ")

    if user_desicion == "1": 
        owner()
    elif user_desicion == "2":
        customer()
    elif user_desicion == "3":
        print("Thank you for visiting our shop!")
        break
    else:
        print("Invalid choice. Please try again.")