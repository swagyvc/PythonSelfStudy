import json
import os
#User Story
#I want owner can login to see if they have account or no
#                                                => yes -> ask username & password
#                                                => no -> ask enter username & passwords
#                                                       => it will save username & passowds so that they can login and check later
#if yes, they can review their inventory, they can either choose to edit inventory (add/remove/change price)
#after edit they can hit save and review inventory.

#Get ready for apply OOP for this project, add login feature (sign in/up for this application)


#---note---
#I want to build a application like a clone amazon, where people can login and add item
# and other people can buy product from others

#Tech stack
#Django

user_input = input("Do you have an account? (y/n): ")

FILE_NAME = "Owner_list.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

#This is for owner sign up
def ownerSignUp():
    print("---NEW OWNER SIGN UP---")
    owner_usernames = input("Please Enter New Ownername: ")
    owner_passwords = input("Please Enter New Passwords: ")

    new_owner = {
        "Ownername" : owner_usernames,
        "OwnerPasswords": owner_passwords
    }
    
    with open(FILE_NAME, "r") as file:
        current_list = json.load(file)
    
        current_list.append(new_owner)
    
    with open(FILE_NAME, 'w') as file:
        json.dump(current_list, file, indent = 4)

    print("Sign Up Successfull!")

#this is for people who already has account
#Figuring out how to check owner if they already has account -> show you are here or pass
#                                if they don't have account -> you try to pivot they to sign up page
def ownerSignIn():
    print("---OWNER SIGN IN---")
    user_usernames = input("Please Enter Ownername: ")
    owner_passwords = input("Please Enter Passwords: ")