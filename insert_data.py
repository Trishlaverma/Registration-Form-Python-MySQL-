from valid_password import valid_password
def insert_data(cursor):

    # SQL query to insert data
    insert_data_query = """INSERT INTO STUDENT (NAME,AGE,EMAIL,ADDRESS,GENDER,PASSWORD, USER_NAME)
    VALUES(%s, %s,%s, %s, %s,%s,%s)
    """
    # Data to be inserted into the table  
    print("--------------------------------")
    NAME = input("Enter Your Name : ")
    print("--------------------------------")
    AGE = int(input("Enter Your Age : "))
    print("--------------------------------")
    EMAIL = input("enter you email : ")
    print("--------------------------------")
    ADDRESS = input("Enter your address : ")
    print("--------------------------------")
    GENDER = input("Enter Your Gender : ")
    print("--------------------------------")
    USER_NAME = input("Enter your USER_NAME : ")
    
    
    while True:
        PASSWORD = input("Enter your password (8 characters, 1 uppercase, 1 digit, 1 special character) :")

        if valid_password(PASSWORD):        
            print("Password is valid.")
            break  
        else:
            print("invalid password please")

    
    
    insert_data =(NAME,AGE,EMAIL,ADDRESS,GENDER,PASSWORD,USER_NAME)
    cursor.execute(insert_data_query,insert_data)