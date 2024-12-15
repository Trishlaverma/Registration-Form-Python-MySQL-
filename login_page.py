from read_data import read_data
from insert_data import insert_data
def login_page(cursor):
    
    open_reg = input("Do you want to login Enter YES\n Enter NEW for new registration")
    if open_reg =="YES" or open_reg =="yes":
        print("Enter your name for login")
        print("-------------------------------")
        read_data(cursor)

    elif open_reg =="NEW" or "new":
        print("Enter your details for new registration")
        print("-------------------------------------------")
        insert_data(cursor)
        
        print("your registration is complete now you Enter yes for login\n")
        print("------------------------------------------------------------")
        read = input("enter Yes for Login")
        if read =="YES" or read == "yes":
            print("Enter your name for login")
            print("-------------------------------")
            read_data(cursor)
        else:
            print("invalid input")
            print("-------------------------------")

    else:
        print("try again")
        print("-------------------------------")