from  create_conn import create_connection 
from table import table
from login_page import login_page
from read_data import read_data
from insert_data import insert_data
def login_page(cursor):
    
    open_reg = input("Do you want to login Enter YES\n-----------------------\nEnter NEW for new registration : ")
    if open_reg =="YES" or open_reg =="yes":
        print("-------------------------------------------------------")
        print("Enter your name for login : ")
        print("-------------------------------")
        read_data(cursor)

    elif open_reg =="NEW" or open_reg== "new":
        print("-------------------------------------------------------")
        print("Enter your details for new registration : ")
        print("-------------------------------------------")
        insert_data(cursor)
        
        print("your registration is complete now you Enter yes for login : ")
        print("------------------------------------------------------------")
        read = input("enter Yes for Login : ")
        print("-------------------------------------------------------")
        if read =="YES" or read == "yes":
            print("-------------------------------------------------------")
            print("Enter your name for login : ")
            print("-------------------------------")
            read_data(cursor)
        else:
            print("invalid input")
            print("-------------------------------")

    else:
        print("Invalid Input please try again")
        print("-------------------------------")

def main():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        table(cursor)
        login_page(cursor)
        connection.commit()

    finally:
        cursor.close()
        connection.close()
        #print("Database Operations Completed Sussessfully.")

if __name__ =="__main__":
    main()