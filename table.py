def table(cursor):
    
    # SQL query to create the table
    create_table = """CREATE TABLE IF NOT EXISTS STUDENT(
    ID INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    NAME VARCHAR(50) NOT NULL,
    AGE INT NOT NULL,
    EMAIL VARCHAR(100) NOT NULL,
    ADDRESS VARCHAR(100),
    GENDER ENUM("M","F","O"),
    PASSWORD VARCHAR(100) NOT NULL,
    USER_NAME VARCHAR(100) NOT NULL
    );"""
    cursor.execute(create_table)  # Execute the query to create the table