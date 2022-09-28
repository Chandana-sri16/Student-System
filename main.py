""" TEAM -2 STUDENT SYSTEM """
# module created by chandana
# whole code integration
# main module

import mysql.connector
from database import save_data, fetch_info, edit
from cont import continu

print('\n-------------------------** STUDENT SYSTEM **------------------------------')
while True:
    try:
        print("\n* Do want to Register a Student ?? (Press 1) \n* Do you want to see student details ?? (Press 2) ")

        opt_chose = input("--> ")
        if opt_chose == '1':
            print("Fill the below details")
            save_data()
            save = input("\nDo you want to save the info ? (y/n) - ").lower()
            if save in ['y', 'yes']:
                print("Information has been saved....")
                continu()
            elif save in ['n', 'no']:
                print("\nDo you want to edit the info ?? (Press 1) \nDo you want to Quit ? (Press 2) ")
                choice = input("--> ")
                if choice == '1':
                    print('-------Student details-------')
                    edit()
                    print('Information has been successfully changed...')
                    break
                elif choice == '2':
                    break
                else:
                    print("Press 1 or 2 ...")
            else:
                input("Enter just Y/N : ")
        elif opt_chose == '2':
            fetch_info()
            continu()
        else:
            print('Choose your option in 1 or 2...')
    except mysql.connector.errors.ProgrammingError:
        print("Enter the details properly!!")
