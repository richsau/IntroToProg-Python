# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Richard Sauer,5/12/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
strFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection
strTaskTxt = "Task"
strPriorityTxt = "Priority"
seperatorText = "----------------"
strTaskItem = ""
strTaskPriority = ""
bolDirtyFlag = False
bolFoundItem = False


# -- Processing -- #
# Step 1 - When the program starts, load data from a text file
# called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Split() returns a list
    dicRow = {strTaskTxt:lstRow[0], strPriorityTxt:lstRow[1].strip()}  # Convert list to dictionary
    lstTable.append(dicRow)  # Adding dictionary to a table
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    # Print a header followed by each task and priority
    if (strChoice.strip() == '1'):
        print("\n{:25} {:20}".format(strTaskTxt, strPriorityTxt))
        print("{:25} {:20}".format(seperatorText, seperatorText))
        for row in lstTable:
            print("{:25} {:20}".format(row[strTaskTxt], row[strPriorityTxt]))
        continue
    # Step 4 - Add a new item to the list/Table
    # Get task and priority from the user
    # then create a dictionary from the input
    # and then append it to the table.
    elif (strChoice.strip() == '2'):
        strTaskItem = input("Please add a new {0}: ".format(strTaskTxt.lower()))
        strTaskPriority = input("Please set a {0} for \"{1}\": ".format(strPriorityTxt.lower(), strTaskItem))
        dicRow = {strTaskTxt:strTaskItem, strPriorityTxt:strTaskPriority}
        lstTable.append(dicRow)  # adding dictionary to a table
        bolDirtyFlag = True
        continue
    # Step 5 - Remove a new item from the list/Table
    # Get a task to remove from the user
    # then search for the task in the table.
    # If the task is found, remove it from the table else
    # inform the user that the task was not found.
    elif (strChoice.strip() == '3'):
        strTaskItem = input("Enter {0} to be removed: ".format(strTaskTxt.lower()))
        bolFoundItem = False
        for row in lstTable:
            if (row[strTaskTxt].lower() == strTaskItem.lower()):
                lstTable.remove(row)
                print("{0} \"{1}\" has been removed.".format(strTaskTxt, strTaskItem))
                bolDirtyFlag = True
                bolFoundItem = True
        if not (bolFoundItem):
            print("Sorry, {0} \"{1}\" was not found.".format(strTaskTxt.lower(), strTaskItem))
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    # For each row in the table, write the task and priority back to the file.
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row[strTaskTxt]) + ',' + str(row[strPriorityTxt]) + '\n')
        objFile.close()
        bolDirtyFlag = False
        print("Data saved in file \"{0}\".".format(strFile))
        continue
    # Step 7 - Exit program
    # Make sure there was no unsaved data
    # then follow the user's instructions.
    elif (strChoice.strip() == '5'):
        if (bolDirtyFlag):
            strChoice = input("You have unsaved data. Are you sure you want to exit? (y/n) ")
            if strChoice.strip().lower() == "y":
                break  # exit the program
            else:
                continue  # abort exit and return to menu
        break  # and Exit the program
