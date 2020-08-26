#!/usr/bin/env python3
# date: 1 March 2019
# NAME

import sqlite3

###################################
# connect to the database
sqlite3Filename ="myCampusDB.sqlite3"

#open my database connection
#conn = sqlite3.connect("myCampusDB.sqlite3")
conn = sqlite3.connect(sqlite3Filename)
print(" My database has been loaded")



# Modify this code to handle database support. For this, get the database code from class and add it to this file to connect to your database file. The below code is to help you keep track of how many attributes here are in each table. Remember, for an INSERT, you will need to know each piece of information for each attribute of a table.


# use a dictionary to keep track of how many attributes there are per table.
tables_dict = {"instructor": 5,
"teaches":5,
"student": 4,
"course": 4,
"department": 3
}

# define a function to get user-in put for the name of the table
def getTableName():
    """Function to get the table name from the user"""
    prmpt = "  Enter table name: "
    tableToEdit = input(prmpt) # enter input
    tableToEdit = tableToEdit.lower() # put text in to lower case

    while(tableToEdit not in tables_dict):
        print(  "The entered table does not exist in the dictionary. Please re-enter the name")
        tableToEdit = input(prmpt) # enter input
        tableToEdit = tableToEdit.lower() # put text in to lower case
    return tableToEdit
# end of getTableName()

# the program actually starts here. The dictionary and the function have already been read and are in memory.
print("  Welcome to my database automation program!")
#myTable_str = getTableName()
#print(" + Note: There are <", tables_dict[myTable_str],"> attributes associated with table <",myTable_str,">.")
#print("  -- End of program --")


def query1(conn): # function in python3
    """shows the content of the table in the database"""
    prmpt = "  Enter table name: "
    #print(prmpt)
    tableToShow = input(prmpt) # enter input
    #tableToShow = tableToEdit.lower() # put text in to lower case
    sqlCommand2 = " SELECT * FROM " + tableToShow
    print("My command is: ", sqlCommand2)

    # run my query
    result = conn.execute(sqlCommand2)

    print("  Result is:", result)

    # collect my results and parse them
    tables = result.fetchall()

    # print the content to the screen
    print("  Raw tables data :", tables)
    #for i in tables: # i is the index of the object ("list")
        #print(" i=", i," column 4 of the table :", i[3])


def update1(conn): # function in python3
    """update the content of the table in the database"""
    prmpt = "what are we going to updata?"
    whatUpdata = input(prmpt)
    if whatUpdata == "courseId":
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " Where are we going to update: "
        whereUpdata = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Course SET courseId = \"{A}\" WHERE courseId == \"{B}\" ".format(A = whatUpdataTo, B = whereUpdata)
        print("My command is: ", sqlCommand2)
    else:
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " whatId is it? "
        ID = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Course SET \"{C}\" = \"{A}\" WHERE courseId == \"{B}\" ".format(A = whatUpdataTo, B = ID, C = whatUpdata)
        print("My command is: ", sqlCommand2)

    # run my query
    cur = conn.cursor()
    cur.execute(sqlCommand2)
    conn.commit()


def update2(conn): # function in python3
    """update the content of the table in the database"""
    prmpt = "what are we going to updata?"
    whatUpdata = input(prmpt)
    if whatUpdata == "ID":
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " Where are we going to update: "
        whereUpdata = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Instructor SET ID = \"{A}\" WHERE ID == \"{B}\" ".format(A = whatUpdataTo, B = whereUpdata)
        print("My command is: ", sqlCommand2)
    else:
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " what ID is it? "
        ID = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE instructor SET \"{C}\" = \"{A}\" WHERE ID == \"{B}\" ".format(A = whatUpdataTo, B = ID, C = whatUpdata)
        print("My command is: ", sqlCommand2)

    # run my query
    cur = conn.cursor()
    cur.execute(sqlCommand2)
    conn.commit()


def update3(conn): # function in python3
    """update the content of the table in the database"""
    prmpt = "what are we going to updata?"
    whatUpdata = input(prmpt)
    if whatUpdata == "ID":
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " Where are we going to update: "
        whereUpdata = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Teaches SET ID = \"{A}\" WHERE ID == \"{B}\" ".format(A = whatUpdataTo, B = whereUpdata)
        print("My command is: ", sqlCommand2)
    else:
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " what ID is it? "
        ID = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Teaches SET \"{C}\" = \"{A}\" WHERE ID == \"{B}\" ".format(A = whatUpdataTo, B = ID, C = whatUpdata)
        print("My command is: ", sqlCommand2)

    # run my query
    cur = conn.cursor()
    cur.execute(sqlCommand2)
    conn.commit()


def update4(conn): # function in python3
    """update the content of the table in the database"""
    prmpt = "what are we going to updata?"
    whatUpdata = input(prmpt)
    if whatUpdata == "courseId":
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " Where are we going to update: "
        whereUpdata = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Department SET courseId = \"{A}\" WHERE courseId == \"{B}\" ".format(A = whatUpdataTo, B = whereUpdata)
        print("My command is: ", sqlCommand2)
    else:
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " whatId is it? "
        ID = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Department SET \"{C}\" = \"{A}\" WHERE courseId == \"{B}\" ".format(A = whatUpdataTo, B = ID, C = whatUpdata)
        print("My command is: ", sqlCommand2)

    # run my query
    cur = conn.cursor()
    cur.execute(sqlCommand2)
    conn.commit()


def update5(conn): # function in python3
    """update the content of the table in the database"""
    prmpt = "what are we going to updata?"
    whatUpdata = input(prmpt)
    if whatUpdata == "ID":
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " Where are we going to update: "
        whereUpdata = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Student SET ID = \"{A}\" WHERE ID == \"{B}\" ".format(A = whatUpdataTo, B = whereUpdata)
        print("My command is: ", sqlCommand2)
    else:
        prmpt = " What are we going to update to? "
        whatUpdataTo = input(prmpt)
        prmpt = " what ID is it? "
        ID = input(prmpt)
    #tableToShow = tableToEdit.lower() # put text in to lower case
    #qlCommand2 = " UPDATE Course SET courseid = " + whatUpdata + " WHERE title == " + whereUpdata
        sqlCommand2 = " UPDATE Student SET \"{C}\" = \"{A}\" WHERE ID == \"{B}\" ".format(A = whatUpdataTo, B = ID, C = whatUpdata)
        print("My command is: ", sqlCommand2)

    # run my query
    cur = conn.cursor()
    cur.execute(sqlCommand2)
    conn.commit()




    #print("  Result is:", result)

    # collect my results and parse them

    # print the content to the screen
    #print("  Raw tables data :", tables)
    #for i in tables: # i is the index of the object ("list")
        #print(" i=", i," column 4 of the table :", i[3])


def insert1(conn):
    """insert information to tables"""
    #prmpt = "  Enter table name: "
    #tableToInsert = input(prmpt) # enter input
    #print("we are working on table:", tableToInsert)

    prmpt = " Insert PersonID: "
    PersonID = input(prmpt)
    prmpt = " Insert name: "
    name = input(prmpt)
    prmpt = " Insert student: "
    student = input(prmpt)
    prmpt = " Insert deptName: "
    deptName = input(prmpt)
    prmpt = " Insert salary: "
    salary =  input(prmpt)
    #all on one line

    myInsert2 = "INSERT INTO Instructor VALUES(\"{A}\",\"{B}\",\"{C}\",\"{D}\",\"{E}\")".format(A = PersonID, B = name, C = student, D = deptName, E = salary)

    print("  Running this command:\n  ",myInsert2)

    result = conn.execute(myInsert2)
    conn.commit() #save the changes
#end of insert1()

def insert2(conn):
    """insert information to tables"""
    #prmpt = "  Enter table name: "
    #tableToInsert = input(prmpt) # enter input
    #print("we are working on table:", tableToInsert)

    prmpt = " Insert courseId: "
    courseId = input(prmpt)
    prmpt = " Insert title: "
    title = input(prmpt)
    prmpt = " Insert deptName: "
    deptName = input(prmpt)
    prmpt = " Insert credits: "
    credits = input(prmpt)
    #all on one line

    myInsert2 = "INSERT INTO course VALUES(\"{A}\",\"{B}\",\"{C}\",\"{D}\")".format(A = courseId, B = title, C = deptName, D = credits)

    print("  Running this command:\n  ",myInsert2)

    result = conn.execute(myInsert2)
    conn.commit() #save the changes
#end of insert2()

def insert3(conn):
    """insert information to tables"""
    #prmpt = "  Enter table name: "
    #tableToInsert = input(prmpt) # enter input
    #print("we are working on table:", tableToInsert)

    prmpt = " Insert ID: "
    ID = input(prmpt)
    prmpt = " Insert courseId: "
    courseId = input(prmpt)
    prmpt = " Insert secId: "
    secId = input(prmpt)
    prmpt = " Insert semester: "
    semester = input(prmpt)
    prmpt = " Insert year: "
    year = input(prmpt)
    #all on one line

    myInsert2 = "INSERT INTO Teaches VALUES(\"{A}\",\"{B}\",\"{C}\",\"{D}\",\"{E}\")".format(A = ID, B = courseId, C = secId, D = semester, E = year)

    print("  Running this command:\n  ",myInsert2)

    result = conn.execute(myInsert2)
    conn.commit() #save the changes
#end of insert1()
def insert4(conn):
    """insert information to tables"""
    #prmpt = "  Enter table name: "
    #tableToInsert = input(prmpt) # enter input
    #print("we are working on table:", tableToInsert)

    prmpt = " Insert courseId: "
    courseId = input(prmpt)
    prmpt = " Insert courseType: "
    courseType = input(prmpt)
    prmpt = " Insert deptName: "
    deptName = input(prmpt)
    #all on one line

    myInsert2 = "INSERT INTO Department VALUES(\"{A}\",\"{B}\",\"{C}\")".format(A = courseId, B = courseType, C = deptName)

    print("  Running this command:\n  ",myInsert2)

    result = conn.execute(myInsert2)
    conn.commit() #save the changes
#end of insert2()
def insert5(conn):
    """insert information to tables"""
    #prmpt = "  Enter table name: "
    #tableToInsert = input(prmpt) # enter input
    #print("we are working on table:", tableToInsert)

    prmpt = " Insert ID: "
    ID = input(prmpt)
    prmpt = " Insert name: "
    name = input(prmpt)
    prmpt = " Insert deptName: "
    deptName = input(prmpt)
    prmpt = " Insert totCred: "
    totCred = input(prmpt)
    #all on one line

    myInsert2 = "INSERT INTO Student VALUES(\"{A}\",\"{B}\",\"{C}\",\"{D}\")".format(A = ID, B = name, C = deptName, D = totCred)

    print("  Running this command:\n  ",myInsert2)

    result = conn.execute(myInsert2)
    conn.commit() #save the changes
#end of insert2()



prmpt = "what would you like to do taody \n1 for query \n2 for insert \n3 for edit\n: "
#print (prmpt)
resp = input(prmpt)
if int(resp) == 1:
    print (" user types in 1 ")
    query1(conn)
if int(resp) == 2:
    print ("user types in 2 ")
    prmpt = " what table? "
    getTableName = input(prmpt)
    getTableName = getTableName.lower()
    if getTableName == "instructor":
        insert1(conn)
    if getTableName == "course":
        insert2(conn)
    if getTableName == "teaches":
        insert3(conn)
    if getTableName == "department":
        insert4(conn)
    if getTableName == "student":
        insert5(conn)
if int(resp) == 3:
    print ("user types in 3 ")
    prmpt = " what table? "
    updateTable = input(prmpt)
    updateTable = updateTable.lower()
    if updateTable == "course":
        update1(conn)
    if updateTable == "teaches":
        update3(conn)
    if updateTable == "department":
        update4(conn)
    if updateTable == "student":
        update5(conn)
    if updateTable == "instructor":
        update2(conn)
