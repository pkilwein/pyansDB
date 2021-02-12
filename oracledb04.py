#!/usr/bin/python3
"""Attempt to insert data into our database"""

import cx_Oracle

try:
    # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
    con = cx_Oracle.connect("system/mysecurepassword@//10.5.19.206:51521/XEPDB1")

    # Now execute the sqlquery 
    cursor = con.cursor()

    ## Lets replace the line below with BIND VARS
    #cursor.execute("insert into plk_student values (19585, 'Jon Bowie', 72000)") 

    ## an example of using BIND VARS (named bind vars)
    ## below :add_vals, :add_name, and :add_vals_two are all named bind vars
    bindvars = ("insert into plk_student values (:add_vals, :add_name, :add_vals_two)")
    cursor.execute(bindvars, add_vals = 19585, add_name = 'Jon Bowie', add_vals_two = 72000)

    # commit that insert the provided data 
    con.commit()

    print("value inserted successful")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs 
# then also we can close the all database operation 
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

