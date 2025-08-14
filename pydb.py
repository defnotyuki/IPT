import pymysql as my

#CREATE DB AND CONFIG
db_server_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '2004',
    'charset' : 'utf8'
}

def create_database():
    conn = my.connect(**db_server_config)
    try:
        with conn.cursor() as cur:
            query = "CREATE DATABASE IF NOT EXISTS dbteresa" 
            cur.execute(query)
            print("Database created successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.open: 
            conn.close()

#CREATE TABLE AND CONFIG
db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '2004',
    'database': 'dbteresa',
    'charset' : 'utf8'
}

def create_table():
    conn = my.connect(**db_config)
    try:
        with conn.cursor() as cur:
            query = """ 
                CREATE TABLE IF NOT EXISTS tbl_student(
                    SID INT(100) PRIMARY KEY AUTO_INCREMENT,
                    fullname VARCHAR(255),
                    course VARCHAR(50),
                    year VARCHAR(20)
                )
            """

            cur.execute(query)
            print("Table Created Successfully")
    finally:
        if conn.open:
            conn.close()

#INSERT DATA
def insert_student( fname, course, yr):
    conn = my.connect(**db_config)
    try:
        with conn.cursor() as cur:
            query = """ 
                INSERT INTO tbl_student
                (fullname, course, year)
                VALUES (%s, %s, %s)
            """
            cur.execute(query, (fname, course, yr))
            conn.commit()
            print("Record saved successfully.")
    finally:
        if conn.open:
            conn.close()
    
def display_student():
    conn = my.connect(**db_config)
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM tbl_student"
            cur.execute(query)
            result = cur.fetchall()
            print(f"{'ID':<5} | {'NAME':<10} | {'COURSE':<5} | {'YEAR':<10}")
            for row in result:
                print(f"{row[0]:<5} | {row[1]:<10} | {row[2]:<6} | {row[3]:<10}")
    finally:
        if conn.open:
            conn.close()

def update_student(id, fname, course, year):
    conn = my.connect(**db_config)
    try:
        with conn.cursor() as cur:
            query = """ 
                UPDATE tbl_student SET
                fullname = %s, course = %s, year = %s
                WHERE SID = %s 
            """
            cur.execute(query, (fname, course, year, id))
            conn.commit()
            print("Record Updated Successfully.")
    finally:
        if conn.open:
            conn.close()


def delete_student(sid):
    conn = my.connect(**db_config)
    try: 
        with conn.cursor() as cur:
            query = "DELETE FROM tbl_student WHERE SID = %s"
            cur.execute(query, (sid))
            conn.commit()
            print("Record Deleted Successfully.")
    finally:
        if conn.open:
            conn.close()

if __name__ == "__main__":
    while True:
        #create_database()
        #create_table()
        #fullname = input("Enter fullname: ")
        #course = input("Enter course: ")
        #year = input("Enter year: ")
        #insert_student(fullname, course, year)
        display_student()
        #id = input("Enter ID to update: ")
        #fullname = input("Enter new fullname: ")
        #course = input("Enter new course: ")
        #year = input("Enter new year: ")
        #update_student(id, fullname, course, year)
        #display_student()
        #id = input("Enter ID to delete: ")
        #delete_student(id)


