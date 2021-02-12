#!/usr/bin/python3
"""create a table within Oracle DB"""

# importing module 
import sqlite3

# Create a table with sqlite3 
try:
    # Connect string format
    con = sqlite3.connect("test.db")

    # Now execute the sqlquery 
    cursor = con.cursor()

    # Creating a table student srollno heading which is number 
    cursor.execute("create table student(srollno number, name varchar2(10), efees number(10, 2))")

    print("Table Created successful")

except Exception as e:
    print("There is a problem with sqlite", e)

# by writing finally if any error occurs 
# then also we can close the all database operation 
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

