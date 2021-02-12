#!/usr/bin/python3
"""create a table within Oracle DB"""

# importing module 
import cx_Oracle  
  
  
# Create a table in Oracle database 
try: 
    # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
    con = cx_Oracle.connect("system/mysecurepassword@//10.5.19.206:51521/XEPDB1") 
      
    # Now execute the sqlquery 
    cursor = con.cursor() 
      
    # Creating a table student srollno heading which is number 
    cursor.execute("create table plk_student(srollno number, name varchar2(10), efees number(10, 2))") 
                      
    print("Table Created successful") 
      
except cx_Oracle.DatabaseError as e: 
    print("There is a problem with Oracle", e) 
  
# by writing finally if any error occurs 
# then also we can close the all database operation 
finally: 
    if cursor: 
        cursor.close() 
    if con: 
        con.close() 

