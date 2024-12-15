def read_data(cursor):
    
    USER_NAME= input("Enter Your User Name")
    PASSWORD = input("Enter Your Password")
    
    select_query = "SELECT * FROM STUDENT where name =%s AND PASSWORD = %s"
    cursor.execute(select_query,(USER_NAME, PASSWORD))
    rows = cursor.fetchone()
    print(rows)
    