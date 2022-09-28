# function that iterates user's choice to continue...

def continu():
    cont = input("\nDo you want to continue?? (Y/N)\n - ").lower()
    if cont in ['yes', 'y']:
        pass
    else:
        exit()
