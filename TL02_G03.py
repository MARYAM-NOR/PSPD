# *********************************************************
# Program: TL02_G03.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Tutorial Section: TL2L Group: G03
# Trimester: 2215
# Year: 2022/23 Trimester 1
# Member_1: 1211112294 | PHARTHIBAN A/L KUMARHESAN
# Member_2: 1211112286 | NUR ADIBAH BINTI KHAIRUL ANUAR
# Member_3: 1211111809 | MARYAM BINTI NORAZMAN
# *********************************************************
# Task Distribution
# Member_1: All parts for the main function, and classes as following: main_functions(), administrator(), new_user_signup() and guest()
# Member_2: Functions under the class registered_user(): order_page(), coupon_func(), coupon_codes(), rating() and payment().
# Member_3: Functions under the class registered_user(): user_logout(), userLogin(), userPage() and display_menu()
# *********************************************************



import os  # Used in this program to refresh/clear the terminal screen before starting a new function or specific instruction (os.system("cls"))
import time  # Used to let the system sleep for a designated time (time.sleep("time in seconds"))
from operator import itemgetter  # Used to sort list using a key in the list's item
import getpass # Used to hide password when typing it for security purposes
import datetime # Used to get the local version of date and time and display when printing receipt
import random # Used to generate random number in a range determined for order number when printing receipt


# PHARTHIBAN A/L KUMARHESAN
class main_functions():

    # PHARTHIBAN A/L KUMARHESAN
    # Displays a welcome page to all kind of users including administrators, users and guests before login/signup
    def welcomePage():
        os.system("cls")
        welcome_text = " WELCOME TO THE RESTAURANT'S DRIVE-THRU SYSTEM "
        print("\n" + welcome_text.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        login_options = [">> 1. ADMINISTRATOR", ">> 2. USER", ">> 3. GUEST"]
        signup_option = ">> A. NEW USER"
        print("OPTIONS TO [LOGIN]:")
        for i in login_options:
            print(i)
        print("\nOPTIONS TO [SIGNUP]:\n" + signup_option + "\n")
        print("OTHER OPTIONS:\n>> E. EXIT\n\n")

        # Choose an option to signup, login or exit
        condition = True
        while condition == True:
            login_select = input("-->  SELECT AN OPTION [1|2|3|A|E]: ")
            if login_select == "1":
                administrator.adminLogin()
                condition = False
            elif login_select == "2":
                registered_user.userLogin()
                condition = False
            elif login_select == "3":
                guest.guestLogin()
                condition = False
            elif login_select.upper() == "A":
                new_user_signup.userSignUp()
                condition = False
            elif login_select.upper() == "E":
                main_functions.exitPage()
                condition = False
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True
        
    # PHARTHIBAN A/L KUMARHESAN
    # Displays warning message and gets confirmation/validation before exiting the system
    def exitPage():
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  DO YOU WANT TO QUIT THE SYSTEM? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                print("\n\n" + " THANK YOU FROM ANGEL'S HAIR RESTAURANT! ".center(70, "-"))
                print(" SEE YOU AGAIN! ".center(70) + "\n\n")
                time.sleep(2)
                exit()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                main_functions.welcomePage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True


# PHARTHIBAN A/L KUMARHESAN
class administrator():

    # PHARTHIBAN A/L KUMARHESAN
    # Login page for administrators
    def adminLogin():
        os.system("cls")
        welcome_admin_login = "  <<  ADMINISTRATOR LOGIN PAGE  >>  "
        print("\n" + welcome_admin_login.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        admins = {}
        usernames_admin = []
        passwords_admin = []

        # Reads data from text files and converts to dictionary that includes keys(usernames of admins) and values(passwords of admins)
        with open("./Text_file/users.txt") as file:
            for line in file:
                (key, val) = line.split()
                usernames_admin.append(key)
                passwords_admin.append(val)
                admins[key] = val

        print(">>  TO GO BACK TO WELCOME PAGE: TYPE [TO BACK] - APPLICABLE TO USERNAME FIELD ONLY\n")  
        # Input for admin's username and validation      
        valid_username = "Not Found"
        while valid_username == "Not Found":
            user_admin = input("-->  ENTER USERNAME OF ADMIN: ")

            for user in usernames_admin:
                print(user)
                if user_admin == user:
                    # Input for admin's password and validation
                    correct_pass = "False"
                    while correct_pass == "False":
                        # Using getpass module to get password and hiding it while being typed
                        pass_admin = getpass.getpass(prompt="-->  ENTER PASSWORD [TYPE 'X' TO CHANGE USERNAME]: ", stream = None)
                        if pass_admin == admins[user]:
                            administrator.adminPage()
                            correct_pass = "True"
                            valid_username = "Found"
                            break
                        elif pass_admin.upper() == "X":
                            administrator.adminLogin()
                            correct_pass = "True"
                            valid_username = "Found"
                            break
                        else:
                            print("-->  INVALID PASSWORD !", end = "\r")
                            time.sleep(1)
                            correct_pass = "False"
                            valid_username = "Found"
                elif user_admin.upper() == "TO BACK":
                    main_functions.welcomePage()
                    correct_pass = "True"
                    valid_username = "Found"
                    break
                else:
                    continue
            if valid_username == "Found" and correct_pass == "True":
                continue
            else:
                print("-->  USERNAME NOT FOUND !", end = "\r")
                time.sleep(1)
                valid_username = "Not Found"

    # PHARTHIBAN A/L KUMARHESAN
    def adminPage():
        os.system("cls")
        welcome_admin = "  <<  ADMINISTRATOR'S PAGE  >>  "
        print("\n" + welcome_admin.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
        
        # Option display for admin features
        print(">>  1. ADD ITEMS TO FOOD MENU\n>>  2. DELETE ITEMS FROM FOOD MENU\n>>  3. CHANGE PASSWORD OF USERS\n>>  4. CHECK BANK ACCOUNT BALANCE\n>>  5. ORDER HISTORY\n>>  6. LOGOUT\n\n")
        
        # Option selection for administrator's features
        condition = True
        while condition == True:
            option_select = input("-->  SELECT AN OPTION [1|2|3|4|5|6]: ")
            if option_select == "1":
                administrator.add_item()
                condition = False
            elif option_select == "2":
                administrator.delete_item()
                condition = False
            elif option_select == "3":
                administrator.change_user_pass()
                condition = False
            elif option_select == "4":
                administrator.account_balance()
                condition = False
            elif option_select == "5":
                administrator.order_history()
                condition = False
            elif option_select == "6":
                administrator.admin_logout()
                condition = False
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # PHARTHIBAN A/L KUMARHESAN
    def add_item():
        os.system("cls")
        welcome_add = "  <<  ADD ITEMS TO ORDER MENU  >>  "
        print("\n" + welcome_add.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        print(">>  TO GO BACK TO ADMINISTRATOR'S PAGE: TYPE [TO BACK]\n")

        # Input for collecting new item's detail to be added in food/order menu 
        item_found = "Not Found"
        while item_found == "Not Found":
            item_code = input("-->  ENTER ITEM'S CODE: ").upper()
            if item_code == "TO BACK":
                administrator.adminPage()
                break
            item_name = input("-->  ENTER ITEM'S NAME: ").upper()
            if item_name == "TO BACK":
                administrator.adminPage()
                break
            try:
                item_price = float(input("-->  ENTER ITEM'S PRICE: RM"))
                if item_price == "TO BACK":
                    administrator.adminPage()
                    break
            except ValueError:
                print("\n--> INVALID INPUT FOR PRICE! TRY AGAIN.")
                time.sleep(1)
                administrator.add_item()
            item = (", ".join([item_code, item_name, str(item_price)]))
            item_found = "Not Found"
            if item_found == "Not Found":
                with open("./text_files/menu.txt") as file:
                    for line in file:
                        menu_detail = list(line.split(", "))
                        if menu_detail[0] == item_code or menu_detail[1] == item_name:
                            print("\n--> ITEM ALREADY EXISTS! TRY AGAIN.")
                            time.sleep(1)
                            administrator.add_item()
                            break
                        else:
                            item_found = "Found"
                    # Adding items into the existing text file
                    if item_found == "Found":
                        menu_file = open("./text_files/menu.txt", "a")
                        menu_file.write(item + "\n")
                        menu_file.close()
                    else:
                        continue

            # Reading the updated text file
            data_file  = open("./text_files/menu.txt",'r')
            lines = data_file.readlines()
            data_file.close()

            # Sorting the lines in text file using the item code using the built-in function itemgetter()
            menus_1 = []
            write_file = open("./text_files/menu.txt",'w')
            for line in lines:
                menu_info = line.split(", ")
                menus_1.append(menu_info)
            menus_1.sort(key = itemgetter(0))
            for i in menus_1:
                write_file.write(", ".join(i))
            write_file.close()

            print("\n\n  >>  ITEM HAS BEEN ADDED TO MENU !")
            time.sleep(2)

        # Getting confirmation to add more items to the food/order menu
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  DO YOU WANT TO ADD MORE ITEMS? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                administrator.add_item()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                administrator.adminPage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True
        
    # PHARTHIBAN A/L KUMARHESAN
    def delete_item():
        os.system("cls")
        welcome_delete = "  <<  DELETE ITEMS FROM ORDER MENU  >>  "
        print("\n" + welcome_delete.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        print(">>  TO GO BACK TO ADMINISTRATOR'S PAGE: TYPE [TO BACK]\n")

        item_found = "Not Found"
        # Finding and deleting the item in the food/order menu using its code
        while item_found == "Not Found":
            item_code = input("-->  ENTER ITEM'S CODE: ").upper()
            if item_code == "TO BACK":
                administrator.adminPage()
                break
            item_found = "Not Found"
            if item_found == "Not Found":
                with open("./text_files/menu.txt") as file:
                    for line in file:
                        menu_detail = list(line.split(", "))
                        if menu_detail[0] == item_code:

                            data_file  = open("./text_files/menu.txt",'r')
                            lines = data_file.readlines()
                            data_file.close()

                            write_file = open("./text_files/menu.txt",'w')
                            for menu in lines:
                                menu_info = menu.split(", ")
                                menu_code = menu_info[0]
                                if item_code != menu_code:
                                    write_file.write(menu)
                            write_file.close()

                            print("\n\n  >>  ITEM HAS BEEN DELETED !")
                            time.sleep(2)

                            item_found = "Found"
                            break
                        else:
                            item_found = "Not Found"
                    
                    if item_found == "Not Found":
                        print("-->  ITEM NOT FOUND !", end = "\r")
                        time.sleep(1)
                        administrator.delete_item()
                        break
                    else:
                        continue
        
        # Getting validation to delete more items from the food/order menu
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  DO YOU WANT TO DELETE MORE ITEMS? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                administrator.delete_item()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                administrator.adminPage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # PHARTHIBAN A/L KUMARHESAN
    def change_user_pass():
        os.system("cls")
        change_pass_page = "  <<  CHANGE USER PASSWORD  >>  "
        print("\n" + change_pass_page.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        print(">>  TO GO BACK TO WELCOME PAGE: TYPE [TO BACK] - APPLICABLE TO USERNAME FIELD ONLY\n")  

        # Reading user data from text file and converting to dictionary with keys(usernames) and values(passwords)
        users = {}
        usernames_user = []
        passwords_user = []

        with open("./text_files/users.txt") as file:
            for line in file:
                (key, val) = line.split()
                usernames_user.append(key)
                passwords_user.append(val)
                users[key] = val

        # Finding the user to change the password
        user_data = "Not Found"
        while user_data == "Not Found":
            user_name = input("-->  WHICH USER'S PASSWORD IS NEED TO BE CHANGED? : ")
            if user_name.upper() == "TO BACK":
                administrator.adminPage()
                break
            else:
                for user in usernames_user:
                    # Changing to a new password
                    if user == user_name:
                        valid_pass = "No"
                        while valid_pass == "No":
                            password_in = input("-->  ENTER NEW PASSWORD [TYPE 'X' TO CHANGE USERNAME]: ")
                            if password_in.upper() == "X":
                                administrator.change_user_pass()
                                valid_pass = "Yes"
                                user_data = "Found"
                            elif (" " in password_in) == True:
                                valid_pass = "No"
                                print("--> INVALID PASSWORD! TRY AGAIN", end = "\r")
                                time.sleep(1)
                            elif len(password_in) < 6:
                                valid_pass = "No"
                                print("--> PASSWORD LENGTH SHOULD BE 6/MORE", end = "\r")
                                time.sleep(1)
                            else:
                                # Writing data back to text file including updated password for the specific user
                                read_file  = open("./text_files/users.txt",'r')
                                lines = read_file.readlines()
                                read_file.close()

                                write_file = open("./text_files/users.txt",'w')
                                for line in lines:
                                    user_info = line.split()
                                    user_id = user_info[0]
                                    if user != user_id:
                                        write_file.write(line)
                                write_file.close()
                                
                                new_user_info = (user + " " + password_in)
                                user_info_file = open("./text_files/users.txt", "a")
                                user_info_file.write(new_user_info + "\n")
                                user_info_file.close()

                                os.system("cls")

                                print("\n\n  >>  USER PASSWORD HAS BEEN CHANGED!")
                                print("      RETURNING TO ADMINISTRATOR'S PAGE.\n\n")

                                time.sleep(3)
                                os.system("cls")
                                administrator.adminPage()
                                valid_pass = "Yes"
                                user_data = "Found"
                                break
                    
                if user_data == "Found" and valid_pass == "Yes":
                    continue
                else:
                    print("-->  USERNAME NOT FOUND !", end = "\r")
                    time.sleep(1)
                    user_data = "Not Found"
                    continue

    # PHARTHIBAN A/L KUMARHESAN
    def account_balance():
        os.system("cls")
        change_pass_page = "  <<  ACCOUNT  >>  "
        print("\n" + change_pass_page.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        data_file  = open("./text_files/account.txt",'r')
        lines = data_file.readlines()
        data_file.close()

        # Display the total earned money, balance money and withdrawn amount. The amounts are based on transaction made through this program only.
        for line in lines:
            account = line.split(", ")
            if account[0] == "total earned":
                print(" >>  TOTAL EARNED".ljust(25) + ": RM " + account[1][:-1])
            elif account[0] == "balance":
                print(" >>  ACCOUNT BALANCE".ljust(25) + ": RM " + account[1][:-1])
            elif account[0] == "withdrawn":
                print(" >>  WITHDRAWN AMOUNT".ljust(25) + ": RM " + account[1][:-1])
        print("\n")

        # Getting validation to withdraw money from the account balance
        print("\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  WANT TO WITHDRAW MONEY? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                administrator.withdraw()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                administrator.adminPage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # PHARTHIBAN A/L KUMARHESAN
    def withdraw():
        os.system("cls")
        change_pass_page = "  <<  MONEY WITHDRAWAL  >>  "
        print("\n" + change_pass_page.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        data_file  = open("./text_files/account.txt",'r')
        lines = data_file.readlines()
        data_file.close()

        # Displaying the current account balance
        for line in lines:
            account = line.split(", ")
            if account[0] == "balance":
                balance = float(account[1][:-1])
                print(" >>  ACCOUNT BALANCE".ljust(25) + ": RM " + account[1][:-1])
            elif account[0] == "withdrawn":
                withdrawn = float(account[1][:-1])

        # Getting input for the amount of money that need to be withdrawn
        amount = "Not Valid"
        while amount == "Not Valid":
            try:
                amount_to_withdraw = float(input("\n-->  HOW MUCH DO YOU WANT TO WITHDRAW: RM"))
                # Validating whether can withdraw money based on the current account balance
                if amount_to_withdraw <= balance:
                    data_file  = open("./text_files/account.txt",'r')
                    lines = data_file.readlines()
                    data_file.close()
                    # Deducting withdrawn amount from current balance
                    new_bal = balance - amount_to_withdraw
                    new_withdrawn = amount_to_withdraw + withdrawn
                    write_file = open("./text_files/account.txt",'w')
                    # Updating the data in text file
                    for line in lines:
                        account = line.split(", ")
                        account_type = account[0]
                        if account_type == "balance":
                            write_file.write("balance, " + '{:.2f}'.format(new_bal) + "\n")
                        elif account_type == "withdrawn":
                            write_file.write("withdrawn, " + '{:.2f}'.format(new_withdrawn) + "\n")
                        else:
                            write_file.write(line)
                    write_file.close()

                    print("\n\n  >>  MONEY WITHDRAWN SUCCESSFULLY!")
                    time.sleep(1)

                    amount = "Valid"
                else:
                    print("-->  INVALID AMOUNT! TRY AGAIN.", end = "\r")
                    time.sleep(1)
                    amount = "Not Valid"
            except ValueError:
                print("-->  INVALID INPUT! TRY AGAIN.", end = "\r")
                time.sleep(1)
                amount == "Valid"
                administrator.withdraw()


        # Getting validation to withdraw more money
        print("\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  WANT TO WITHDRAW MORE MONEY? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                administrator.withdraw()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                administrator.adminPage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # PHARTHIBAN A/L KUMARHESAN
    def order_history():
        os.system("cls")
        change_pass_page = "  <<  ORDER HISTORY  >>  "
        print("\n" + change_pass_page.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n")

        data_file  = open("./text_files/history.txt",'r')
        lines = data_file.readlines()
        data_file.close()

        # Printing the header of the table
        print("\n" + " " + "-" * 70)
        print(" | "+"NUM".center(5)+" | "+"USERNAME".center(22)+" | "+"NUM. OF ITEMS".center(15)+" | "+"PRICE (RM)".center(15)+" | ")
        print(" " + "-" * 70)
        i = 0
        # Printing the menu read from the text file
        for line in lines:
            i = i + 1
            history = line.split(", ")
            history_price = "RM "+ history[2][:-1]
            print(" | "+str(i).center(5)+" | "+history[0].ljust(22)+" | "+history[1].center(15)+" | "+history_price.center(15)+" | ")
        print(" " + "-" * 70 + "\n")

        # Getting validation to go back to administrator's page
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n")
        condition = True
        while condition == True:
            confirmation = input("-->  GO BACK TO ADMINISTRATOR'S PAGE? [Y]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                administrator.adminPage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # PHARTHIBAN A/L KUMARHESAN
    def admin_logout():
        # Validation to logout as administrator and return back to main page/welcome page
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  DO YOU WANT TO LOGOUT (ADMIN)? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                main_functions.welcomePage()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                administrator.adminPage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True


# NUR ADIBAH BINTI KHAIRUL ANUAR
# MARYAM BINTI NORAZMAN
class registered_user():

    # MARYAM BINTI NORAZMAN
    def user_logout(username_history):
        # Getting validation to logout as user and return to the main page/welcome page
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        condition = True
        while condition == True:
            confirmation = input("-->  DO YOU WANT TO LOGOUT (USER)? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                main_functions.welcomePage()
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                registered_user.userPage(username_history)
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # MARYAM BINTI NORAZMAN
    def userLogin():
        os.system("cls")
        welcome_user_login = "  <<  USER LOGIN PAGE  >>  "
        print("\n" + welcome_user_login.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        # Reading user data from text file and converting to dictionary with keys(usernames) and values(passwords)
        users = {}
        usernames_user = []
        passwords_user = []

        with open("./text_files/users.txt") as file:
            for line in file:
                (key, val) = line.split()
                usernames_user.append(key)
                passwords_user.append(val)
                users[key] = val

        print(">>  TO GO BACK TO WELCOME PAGE: TYPE [TO BACK] - APPLICABLE TO USERNAME FIELD ONLY\n>>  IF YOU FORGOT YOUR PASSWORD: TYPE [?] - APPLICABLE TO PASSWORD FIELD ONLY\n")        
        # Getting input for username and validation
        valid_username = "Not Found"
        while valid_username == "Not Found":
            user_user = input("-->  ENTER USERNAME OF USER: ")
            for user in usernames_user:
                if user_user == user:
                    # Getting password for the username and validation
                    correct_pass = "False"
                    while correct_pass == "False":
                        # Using getpass module to get password and hiding it while being typed
                        pass_user = getpass.getpass(prompt="-->  ENTER PASSWORD [TYPE 'X' TO CHANGE USERNAME]: ", stream = None)
                        if pass_user == users[user]:
                            username_history = user
                            registered_user.userPage(username_history)
                            correct_pass = "True"
                            valid_username = "Found"
                            break
                        elif pass_user.upper() == "X":
                            registered_user.userLogin()
                            correct_pass = "True"
                            valid_username = "Found"
                            break
                        # Forgot password
                        # Prompts administrators to login to change the user's password
                        elif pass_user == "?":
                            print("\n\n\nNOTICE: ADMINISTRATOR HAS BEEN NOTIIFIED.\nPLEASE BE PATIENT UNTIL OUR ADMIN SOLVES THIS ISSUE, THANK YOU!\n")
                            print("-->  REDIRECTING TO ADMIN PAGE.", end = "\r")
                            time.sleep(2)
                            print("-->  REDIRECTING TO ADMIN PAGE..", end = "\r")
                            time.sleep(2)
                            print("-->  REDIRECTING TO ADMIN PAGE...", end = "\r")
                            time.sleep(2)
                            os.system("cls")
                            administrator.adminLogin()
                        else:
                            print("-->  INVALID PASSWORD !", end = "\r")
                            time.sleep(1)
                            correct_pass = "False"
                            valid_username = "Found"
                elif user_user.upper() == "TO BACK":
                    main_functions.welcomePage()
                    correct_pass = "True"
                    valid_username = "Found"
                    break
                else:
                    continue
            if valid_username == "Found" and correct_pass == "True":
                continue
            else:
                print("-->  USERNAME NOT FOUND !", end = "\r")
                time.sleep(1)
                valid_username = "Not Found"

    # MARYAM BINTI NORAZMAN
    def userPage(username_history):
        os.system("cls")
        welcome_user = "  <<  USER'S PAGE  >>  "
        print("\n" + welcome_user.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
        
        # Displays options for users to select and go to
        print(">>  1. START TO ORDER\n>>  2. DISPLAY MENU\n>>  3. SEE AVAILABLE COUPON CODES\n>>  4. RATE OUR SERVICE\n>>  5. LOGOUT\n\n")
    
        condition = True
        while condition == True:
            option_select = input("-->  SELECT AN OPTION [1|2|3|4|5]: ")
            if option_select == "1":
                registered_user.order_page(username_history)
                condition = False
            elif option_select == "2":
                registered_user.display_menu(username_history)
                condition = False
            elif option_select == "3":
                registered_user.coupon_codes(username_history)
                condition = False
            elif option_select == "4":
                registered_user.rating(username_history)
                condition = False
            elif option_select == "5":
                registered_user.user_logout(username_history)
                condition = False
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def order_page(username_history):
        os.system("cls")
        welcome_user = "  <<  ORDER PAGE  >>  "
        print("\n" + welcome_user.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        # Reads data from text file
        data_file = open("./text_files/menu.txt", "r")
        lines = data_file.readlines()
        data_file.close()

        # Displays the food/order menu according to their types (main dishes, snacks, desserts and beverages)
        print("-" * 62)
        print(f"""|  CODE  |            MAIN DISHES              |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "A" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        print("-" * 62)
        print(f"""|  CODE  |               SNACKS                |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "B" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        print("-" * 62)
        print(f"""|  CODE  |              DESSERTS               |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "C" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        print("-" * 62)
        print(f"""|  CODE  |              BEVERAGES              |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "D" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        # Getting validation to start ordering
        subtotal = 0
        menu_details = []
        order = input("\n\n-->  DO YOU WANT TO ORDER NOW? [Y/N]: ").lower()
        print(" ")
        if order == "y" or order == "yes":
            # Ordering items from food/order menu
            addition = "y"
            while addition == "y":
                code_input = input("-->  WHAT IS THE CODE?: ").upper()
                menu_found = "no"
                for line in lines:
                    menu_info_order = line.split(", ")
                    if code_input in menu_info_order:
                        menu_price_order = menu_info_order[2][:-1]
                        # Try - except function used to handle the error when input for the quantity is not integer
                        try:
                            quantity_food = int(input("-->  QUANTITY [NUMBERS]: "))
                            total_price = float(menu_price_order) * int(quantity_food)
                            subtotal = float(subtotal) + total_price
                            subtotal = '{:.2f}'.format(subtotal)
                            print(f"""\n>>  YOUR CURRENT TOTAL IS RM{subtotal}\n\n""")
                            input_valid = "n"
                            while input_valid == "n":
                                # Validation to add more items into order
                                addition = input("--> DO YOU WANT TO ADD MORE? [Y/N]: ").lower()
                                if addition != "y" and addition != "n" and addition != "yes" and addition != "no":
                                    print("-->  INVALID INPUT!", end = "\r")
                                    time.sleep(1)
                                    input_valid = "n"
                                else:
                                    input_valid = "y"
                            print(" ")
                            quantity_food = str(quantity_food)
                            total_price = float('{:.2f}'.format(total_price))
                            menu_details.append([code_input, menu_info_order[1], quantity_food, total_price])  
                            menu_found = "yes"
                        except ValueError:
                            print("\n-->  WRONG INPUT FORMAT!", end = "\r")
                            time.sleep(1)
                            addition = "y"
                            menu_found = "yes"
                    
                if menu_found == "no":
                    addition = "y"
                    print("-->  CODE NOT FOUND!", end = "\r")
                    time.sleep(1)

            # Displays the total for current order
            print(f"\n>> YOUR TOTAL IS RM{subtotal} !\n")
            # Gets input for coupon code (user will get discount for their order if entered an available coupon code)
            print("\n>>  COUPON CODE [IF ANY] :\n    - TYPE [X] TO SKIP THIS SECTION\n")
            registered_user.coupon_func(subtotal, menu_details, username_history)

        elif order == "n":
            print("-->  REDIRECTING TO USER PAGE.", end = "\r")
            time.sleep(1)
            print("-->  REDIRECTING TO USER PAGE..", end = "\r")
            time.sleep(1)
            print("-->  REDIRECTING TO USER PAGE...", end = "\r")
            time.sleep(1)
            os.system("cls")
            registered_user.userPage(username_history)
        else:
            print("-->  INVALID INPUT! TRY AGAIN.", end = "\r")
            time.sleep(1)
            os.system("cls")
            registered_user.order_page(username_history)

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def coupon_func(subtotal, menu_details, username_history):
        # Reads coupon codes, its discount(%) and quantity from the text file
        coupon_file = open("./text_files/coupon.txt", "r")
        lines_coupon = coupon_file.readlines()
        coupon_file.close()
        coupon_found = "No"
        while coupon_found == "No":
            # Gets input for the coupon code from user
            coupon_code = input("-->  ENTER THE COUPON CODE [TYPE [X] TO SKIP]: ").upper()
            # Checking coupon code and its availability
            if coupon_code == "X":
                discount = 0
                grand_total = subtotal
                registered_user.payment(grand_total, menu_details, discount, subtotal, username_history)
                break
            for line_coupon in lines_coupon: 
                coupon_info = line_coupon.split(", ")
                coupon_price = coupon_info[1][:-1]
                coupon_quantity = int(coupon_info[2][:-1])
                # Checks coupon code's availability
                if coupon_code in coupon_info:
                    coupon_percentage = float(coupon_price)/100
                    discount = float(coupon_price)
                    coupon_price = coupon_price + "%"
                    coupon_new_quantity = coupon_quantity - 1
                    coupon_new_quantity = str(coupon_new_quantity) + "\n"
                    if coupon_new_quantity == "-1\n":
                        print("-->  SORRY, THIS COUPON IS NOT AVAILABLE!", end = "\r")
                        time.sleep(1)
                        coupon_found = "No"
                    else:
                        # Updates current availability of coupon codes
                        replace_text = (", ".join([coupon_code, coupon_price, coupon_new_quantity]))
                        write_file = open("./text_files/coupon.txt",'w')
                        for coupon_line in lines_coupon:
                            if coupon_line[0] != replace_text[0]:
                                write_file.write(coupon_line)
                            else:
                                write_file.write(replace_text)
                        write_file.close()
                        coupon_found = "Yes"
                        # Calculates total after discount from coupon code
                        grand_total = float(subtotal) - (float(subtotal) * (discount/100))
                        valid_code = "Yes"
                        print("\n\n")
                        print("-->  REDIRECTING TO PAYMENT PAGE.", end = "\r")
                        time.sleep(1)
                        print("-->  REDIRECTING TO PAYMENT PAGE..", end = "\r")
                        time.sleep(1)
                        print("-->  REDIRECTING TO PAYMENT PAGE...", end = "\r")
                        time.sleep(1)
                        registered_user.payment(grand_total, menu_details, discount, subtotal, username_history)
                        break
                else:
                    valid_code = "No"
            if valid_code == "No":
                print("-->  INVALID COUPON CODE!", end="\r")
                time.sleep(1)
                coupon_found = "Yes"
                registered_user.coupon_func(subtotal, menu_details, username_history)

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def rating(username_history):
        os.system("cls")
        welcome_user = "  <<  RATE OUR SERVICE  >>  "
        print("\n" + welcome_user.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
        try:
            # Getting rating from users about the restaurant's service
            service = float(input("-->  RATE OUR SERVICE [SCALE - 1 TO 5]: "))
            if service < 1 or service > 5:
                print("-->  INVALID INPUT!", end = "\r")
                time.sleep(1)
                registered_user.rating(username_history)
            # Getting comment from user about the service (optional)
            print("\n>>  ANY SUGGESTIONS ON HOW WE CAN IMPROVE OUR SERVICE?")
            comment = input("-->  GIVE YOUR COMMENT [OR PRESS ENTER TO SKIP]: ")
        except ValueError:
            print("-->  INVALID INPUT!", end = "\r")
            time.sleep(1)
            registered_user.rating(username_history)
        print("\n")
        loop = "Yes"
        while loop == "Yes":
            try:
                # Getting rating from user about the dishes
                input_is = "Valid"
                while input_is == "Valid":
                    food_service = float(input("-->  RATE OUR DISHES [SCALE - 1 TO 5]: "))
                    if food_service < 1 or food_service > 5:
                        print("-->  INVALID INPUT!", end = "\r")
                        time.sleep(1)
                    else:
                        input_is = "Not Valid"
                # Getting comment from user about the dishes (optional)
                print("\n>>  WHAT WE COULD IMPROVE ABOUT THE DISHES?")
                comment = input("-->  GIVE YOUR COMMENT [OR PRESS ENTER TO SKIP]: ")
                loop = "No"
                if service >= 4 and food_service >= 4:
                    print("\n\n>>  THANK YOU SO MUCH! WE LOVE YOU <3\n>>  SEE YOU AGAIN!\n\n\n")
                elif service == 3 or food_service == 3:
                    print("\n\n>>  THANK YOU :)\n\n")
                elif service >= 1 or food_service >= 1:
                    print("\n\n>>  THANK YOU. WE WILL IMPROVE OUR SERVICE IN FUTURE!\n\n\n")
            except ValueError:
                print("-->  INVALID INPUT!", end = "\r")
                time.sleep(1)
            

        print("-->  REDIRECTING TO USER PAGE.", end = "\r")
        time.sleep(1)
        print("-->  REDIRECTING TO USER PAGE..", end = "\r")
        time.sleep(1)
        print("-->  REDIRECTING TO USER PAGE...", end = "\r")
        time.sleep(1)
        os.system("cls")
        registered_user.userPage(username_history)

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def coupon_codes(username_history):
        os.system("cls")
        welcome_user = "  <<  COUPON CODES  >>  "
        print("\n" + welcome_user.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
        # Reading coupon codes from the text file
        coupon_file = open("./text_files/coupon.txt", "r")
        lines = coupon_file.readlines()
        coupon_file.close()
        print("-" * 48)
        # Printing the header of table (to display coupon codes)
        print(f"""|   COUPON'S NAME   |  DISCOUNT(%)  | QUANTITY |""")
        print("-" * 48)
        # Printing the coupon codes
        for line_coupon in lines:
            coupon_info = line_coupon.split(", ")
            coupon_quantity = coupon_info[2][:-1]
            print("| " + coupon_info[0].ljust(18) + "| " + coupon_info[1].center(14) + "|" + coupon_quantity.center(10) + "|")
        print("-" * 48)
        # User need to press enter to go back to user's page
        confirmation = input("\n\n-->  PRESS [ENTER] TO GO BACK: ")
        os.system("cls")
        registered_user.userPage(username_history)

    # NUR ADIBAH BINTI KHAIRUL ANUAR
    def payment(grand_total, menu_details, discount, subtotal, username_history):
        # Function for selecting payment method and printing receipt for the order
        os.system("cls")
        welcome_user = "  <<  PAYMENT AND RECEIPT  >>  "
        print("\n" + welcome_user.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
        # datetime() module is used to get the local version of date and time using the directive - %c when printing receipt
        x = datetime.datetime.now()
        quantity_history = 0
        # Selecting payment method
        print("-----  PAYMENT METHOD  -----\n")
        print(">>  1. CASH\n>>  2. E-WALLET / E-BANKING\n>>  3. CREDIT / DEBIT CARD\n\n")
        payment_method = input("-->  CHOOSE YOUR PAYMENT METHOD [1|2|3]: ").upper()
        # Printing receipt for payment using e-wallet/e-banking and credit/debit card
        if payment_method == "2" or payment_method == "3":
            print("\n\n\n>>  YOU CAN PAY HERE. HERE IS YOUR RECEIPT!")
            if payment_method == "2":
                pay_method = "E-WALLET / E-BANKING"
            elif payment_method == "3":
                pay_method = "CREDIT / DEBIT CARD"
            
            print(F"""
===========================================================
                          RECEIPT

           STORE NAME  : ANGEL'S HAIR RESTAURANT
           DATE & TIME : {x.strftime("%c")}
           USERNAME    : {username_history}""")
            print("="*59)
            print("| " + "CODE".center(6) + " | " +  "ITEM NAME".center(25) + " | " + "QTY".center(5) + " | " + "TOTAL (RM)".center(10) + " | ")
            print("-"*59)
            for menu in menu_details:
                print("| " + menu[0].center(6) + " | " +  menu[1].ljust(25) + " | " + menu[2].center(5) + " | " + '{:.2f}'.format(menu[3]).center(10) + " | ")
                quantity_history = quantity_history + int(menu[2])
            print(F"""===========================================================
            SUBTOTAL               : RM {subtotal}
            DISCOUNT               : {discount} %
            TAX                    : RM 0.00
            TOTAL AMOUNT           : RM {grand_total}

            PAYMENT METHOD         : {pay_method}
===========================================================
                * YOUR QUEUE NUMBER : {random.randint(100, 999)} *

   PLEASE WAIT FOR A WHILE. YOUR FOOD IS BEING PREPARED.
 YOU CAN COLLECT YOUR FOOD IN THE NEXT COUNTER. THANK YOU!
===========================================================
            """)
            
            # Adding order history to the text file - includes (username of user, total quantity of items ordered and the grand total)
            new_line = ", ".join([username_history, str(quantity_history), str(grand_total)])

            history_file = open("./text_files/history.txt", "a")
            history_file.write(new_line + "\n")
            history_file.close()

            data_file  = open("./text_files/account.txt",'r')
            lines = data_file.readlines()
            data_file.close()

            # Updating the total earned and balance money to the text file
            write_file = open("./text_files/account.txt",'w')
            for line in lines:
                account = line.split(", ")
                account_type = account[0]
                if account_type == "balance":
                    new_bal = float(account[1]) + float(grand_total)
                    write_file.write("balance, " + '{:.2f}'.format(new_bal) + "\n")
                elif account_type == "total earned":
                    new_total = float(account[1]) + float(grand_total)
                    write_file.write("total earned, " + '{:.2f}'.format(new_total) + "\n")
                else:
                    write_file.write(line)
            write_file.close()

            # Getting validation to order again (with the same username)
            print("\n\n\n" + " WARNING! ".center(50, "="))
            print("\n>>  Y = YES\n>>  N = NO\n")
            condition = True
            while condition == True:
                confirmation = input("-->  DO YOU WANT TO ORDER AGAIN (USER)? [Y|N]: ")
                if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                    condition = False
                    os.system("cls")
                    registered_user.order_page(username_history)
                elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                    condition = False
                    main_functions.welcomePage()
                else:
                    print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                    time.sleep(1)
                    condition = True

        # Printing receipt for payment using cash
        elif payment_method == "1":
            pay_method = "CASH"
            print("\n\n>>  PLEASE PROCEED TO THE NEXT COUNTER TO PAY. HERE IS YOUR RECEIPT!\n\n")
            print(F"""
===========================================================
                          RECEIPT

           STORE NAME  : ANGEL'S HAIR RESTAURANT
           DATE & TIME : {x.strftime("%c")}
           USERNAME    : {username_history}""")
            print("="*59)
            print("| " + "CODE".center(6) + " | " +  "ITEM NAME".center(25) + " | " + "QTY".center(5) + " | " + "TOTAL (RM)".center(10) + " | ")
            print("-"*59)
            for menu in menu_details:
                print("| " + menu[0].center(6) + " | " +  menu[1].ljust(25) + " | " + menu[2].center(5) + " | " + '{:.2f}'.format(menu[3]).center(10) + " | ")
                quantity_history = quantity_history + int(menu[2])

            print(F"""===========================================================
            SUBTOTAL               : RM {subtotal}
            DISCOUNT               : {discount} %
            TAX                    : RM 0.00
            TOTAL AMOUNT           : RM {grand_total}

            PAYMENT METHOD         : {pay_method}
===========================================================
                * YOUR QUEUE NUMBER : {random.randint(100, 999)} *

   PLEASE WAIT FOR A WHILE. YOUR FOOD IS BEING PREPARED.
 YOU CAN COLLECT YOUR FOOD IN THE NEXT COUNTER. THANK YOU!
===========================================================
            """)

            # Adding order history to the text file - includes (username of user, total quantity of items ordered and the grand total)
            new_line = ", ".join([username_history, str(quantity_history), str(grand_total)])

            history_file = open("./text_files/history.txt", "a")
            history_file.write(new_line + "\n")
            history_file.close()

            # Updating the total earned and balance money to the text file
            data_file  = open("./text_files/account.txt",'r')
            lines = data_file.readlines()
            data_file.close()

            write_file = open("./text_files/account.txt",'w')
            for line in lines:
                account = line.split(", ")
                account_type = account[0]
                if account_type == "balance":
                    new_bal = float(account[1]) + float(grand_total)
                    write_file.write("balance, " + '{:.2f}'.format(new_bal) + "\n")
                elif account_type == "total earned":
                    new_total = float(account[1]) + float(grand_total)
                    write_file.write("total earned, " + '{:.2f}'.format(new_total) + "\n")
                else:
                    write_file.write(line)
            write_file.close()

            # Getting validation to order again (with the same username)
            print("\n\n\n" + " WARNING! ".center(50, "="))
            print("\n>>  Y = YES\n>>  N = NO\n")
            condition = True
            while condition == True:
                confirmation = input("-->  DO YOU WANT TO ORDER AGAIN (USER)? [Y|N]: ")
                if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                    condition = False
                    os.system("cls")
                    registered_user.order_page(username_history)
                elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                    condition = False
                    main_functions.welcomePage()
                else:
                    print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                    time.sleep(1)
                    condition = True
        else:
            print("--> INVALID INPUT! TRY AGAIN.", end = "\r")
            registered_user.payment(grand_total, menu_details, discount, subtotal, username_history)

    # MARYAM BINTI NORAZMAN
    def display_menu(username_history):
        # Displaying menu to viewed by user - this section doesn't continues to order page
        os.system("cls")
        welcome_user = "  <<  MENU  >>  "
        print("\n" + welcome_user.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")

        # Reading food/order menu data from text file and printing according to the menu type (main dishes, snacks, desserts and beverages)
        data_file = open("./text_files/menu.txt", "r")
        lines = data_file.readlines()
        data_file.close()

        print("-" * 62)
        print(f"""|  CODE  |            MAIN DISHES              |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "A" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        print("-" * 62)
        print(f"""|  CODE  |               SNACKS                |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "B" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        print("-" * 62)
        print(f"""|  CODE  |              DESSERTS               |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "C" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        print("-" * 62)
        print(f"""|  CODE  |              BEVERAGES              |  PRICE (RM) |""")
        print("-" * 62)
        for line in lines:
            menu_info = line.split(", ")
            menu_price = menu_info[2][:-1]
            menu_info[2] = menu_price
            if "D" in menu_info[0]:
                print("|" + menu_info[0].center(8) + "| " + menu_info[1].ljust(36) + "|" + menu_price.center(13) + "|")

        to_back = input("\n\n-->  PRESS [ENTER] TO GO BACK TO USER PAGE: ")
        registered_user.userPage(username_history)


# PHARTHIBAN A/L KUMARHESAN
class new_user_signup():

    # PHARTHIBAN A/L KUMARHESAN
    def userSignUp():
        os.system("cls")
        welcome_user_signup = "  <<  USER SIGNUP PAGE  >>  "
        print("\n" + welcome_user_signup.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
        print(">>  TO GO BACK TO WELCOME PAGE: TYPE [TO BACK] - APPLICABLE TO USERNAME FIELD ONLY\n")
        # Displaying boundaries to create a new username and password for user signup
        print(" RULES TO CREATE USERNAME & PASSWORD ".center(50, "="))
        print("\n>>  [USERNAME] : NO SPACES (' ') ARE ALLOWED")
        print(">>  [PASSWORD] : NO SPACES (' ') ARE ALLOWED")
        print("                 SHOULD BE 6/MORE CHARACTERS LONG\n\n")

        # Getting existing users' data from the text file and converting dictionary with keys(usernames) and values(passwords)
        users = {}
        usernames_user = []
        passwords_user = []

        with open("./text_files/users.txt") as file:
            for line in file:
                (key, val) = line.split()
                usernames_user.append(key)
                passwords_user.append(val)
                users[key] = val

        # Getting new username for the new user
        valid_username = "No"
        valid_pass = "Yes"
        while valid_username == "No":
            username_in = input("-->  ENTER NEW USERNAME [USER]: ")
            if username_in.upper() == "TO BACK":
                main_functions.welcomePage()
                valid_username = "Yes"
            elif (" " in username_in) == True:
                valid_username = "No"
                print("--> INVALID USERNAME! TRY AGAIN", end = "\r")
                time.sleep(1)
            else:
                # Checking whether the given username is already taken by another user or already exists
                for user in usernames_user:
                    if user == username_in:
                        print("-->  USERNAME ALREADY EXISTS!", end = "\r")
                        time.sleep(1)
                        new_user_signup.userSignUp()
                        valid_username = "No"
                        break
                valid_username = "Yes"
                valid_pass = "No"
        # Getting new password for the new user
        while valid_pass == "No":
            password_in = input("-->  ENTER NEW PASSWORD [TYPE 'X' TO CHANGE USERNAME]: ")
            if password_in.upper() == "X":
                new_user_signup.userSignUp()
                valid_pass = "Yes"
            elif (" " in password_in) == True:
                valid_pass = "No"
                print("--> INVALID PASSWORD! TRY AGAIN", end = "\r")
                time.sleep(1)
            elif len(password_in) < 6:
                valid_pass = "No"
                print("--> PASSWORD LENGTH SHOULD BE 6/MORE", end = "\r")
                time.sleep(1)
            else:
                # Adding the new user's info to the text file
                new_user_info = (username_in + " " + password_in)
                user_info_file = open("./text_files/users.txt", "a")
                user_info_file.write(new_user_info + "\n")
                user_info_file.close()

                os.system("cls")

                print("\n\n  >>  CONGRATULATIONS! NEW USER HAS BEEN CREATED.")
                print("      PLEASE PROCEED TO LOGIN WITH REGISTERED USERNAME.\n\n")

                time.sleep(3)
                os.system("cls")
                registered_user.userLogin()
                valid_pass = "Yes"
                break
    

# PHARTHIBAN A/L KUMARHESAN
class guest():

    # PHARTHIBAN A/L KUMARHESAN
    def guestLogin():
        # Allows customers who do not want to signup as a new user or login as a user to use the system as a guest
        print("\n\n\n" + " WARNING! ".center(50, "="))
        print("\n>>  Y = YES\n>>  N = NO\n")
        # Validation to use the system as a guest
        condition = True
        while condition == True:
            confirmation = input("-->  DO YOU WANT TO USE THE SYSTEM AS GUEST? [Y|N]: ")
            if confirmation.upper() == "Y" or confirmation.upper() == "YES":
                condition = False
                os.system("cls")
                welcome_guest_login = "  <<  GUEST LOGIN PAGE  >>  "
                print("\n" + welcome_guest_login.center(70, "-") + "\n" + " ANGEL'S HAIR RESTAURANT ".center(70) + "\n\n")
                print(" >>  REDIRECTING YOU TO THE USER PAGE", end = "\r")
                time.sleep(1)
                print(" >>  REDIRECTING YOU TO THE USER PAGE .", end = "\r")
                time.sleep(1)
                print(" >>  REDIRECTING YOU TO THE USER PAGE . .", end = "\r")
                time.sleep(1)
                print(" >>  REDIRECTING YOU TO THE USER PAGE . . .", end = "\r")
                time.sleep(1)
                registered_user.userPage(username_history = "guest")
            elif confirmation.upper() == "N" or confirmation.upper() == "NO":
                condition = False
                main_functions.welcomePage()
            else:
                print("-->  ERROR: CHOOSE A VALID OPTION!", end = "\r")
                time.sleep(1)
                condition = True

       
# Starting the program by calling the welcomePage() function under the class main_functions()
main_functions.welcomePage()