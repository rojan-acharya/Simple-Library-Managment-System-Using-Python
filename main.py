from borrowMore import *
import datetime
import os
from name import getName
from notes import genNotes, getCurrentTime, libdict, readBooks

def borrower():
    borrowerName = []
    bookID = int(input("Enter your preferred bookID: "))
    if bookID in currentDict.keys():
        print("The book is in stock. Please fill out the information below!")

        name = getName()
        qty = int(input("Enter the quantity of the books: "))
        if qty <= int(currentDict[bookID][2]) and qty != 0:
            print("Name:", name, "\n The book you have borrowed:",
                  currentDict[bookID][0], "\n Date and Time:", getCurrentTime())
            price = qty * float(currentDict[bookID][3])
            print("Total Price: ", "$", price)
            date1 = getCurrentTime()
            aaa = int(currentDict[bookID][2])-qty
            currentDict[bookID][2] = aaa
            borrowerName.append(name)
            saveFile = open("notes.txt", "a")
            saveFile.write(name)
            saveFile.write(",")
            saveFile.write(currentDict[bookID][0])
            saveFile.write(",")
            saveFile.write(str(qty))
            saveFile.write(",")
            saveFile.write(str(price))
            saveFile.write(",")
            saveFile.write(getCurrentTime())
            saveFile.write("\n")
            saveFile.close()
            promptMore()
            s = genNotes()
            bFile = open("stock.txt", "w")
            bFile.write("")

            for values in currentDict.values():
                cFile = open("stock.txt", "a")
                cFile.write(str(values[0])+","+str(values[1]) +
                            ","+str(values[2])+","+str(values[3]))
                cFile.write("\n")
            cFile.close()

        elif qty == 0:
            print("Please input a valid option!")
            dispMenu()
        else:
            print("Sorry, we don't have ", qty, " books in stock.")
            dispMenu()
    else:
        print("Sorry, the book you asked for is not available.")
        dispMenu()
    return borrowerName

def promptMore():
    borrowMore = input("Do you want to borrow more books [y/n]? => ")
    if borrowMore == 'y' or borrowMore == 'Y':
        borrower()
    elif borrowMore == 'n' or borrowMore == 'N':
        print("Thank you!")
    else:
        print("Please select a valid value! (Y/N)")
        promptMore()

def dispMenu():
    pick = 0
    while True:
        try:
            print("""\n
            *************************************************
            *  Welcome to Rojans Library Management System  *
            *************************************************
            1. Borrow a book
            2. Return a book
            3. Exit 
            -------------------------------------------------\n""")
            pick = int(input("Select the option from the menu above!! (1-3) => "))
            if pick == 1:
                readBooks()
                borrowerName = borrower()

            elif pick == 2:
                checkName = getName()
                borrowBookID = int(input("Enter the bookID: "))

                notesList = []
                borrowerName = []
                booksList = []
                borrowList = []
                timeList = []

                with open("notes.txt") as f:
                    for row in f:
                        borrowerName.append(row.split(",")[0])
                        booksList.append(row.split(",")[1])
                        borrowList.append(row.split(",")[2])
                        timeList.append(row.split(",")[4])

                for i in range(len(borrowerName)):
                    if checkName == borrowerName[i]:
                        print("\nYou have borrowed a book.")
                        time = abs((datetime.datetime.strptime(getCurrentTime().split()[0], "%Y-%m-%d")-datetime.datetime.strptime(timeList[i].split()[0], "%Y-%m-%d")).days)
                        if time >= 10 and time != 0:
                            timed = time - 10
                            fineAmt = timed * 2
                            print("You have been fined $", fineAmt,
                                "for not returning the books in time.")
                        else:
                            fineAmt = 0
                            print("You have returned the book in time.")

                        qtyEx = borrowList[i]
                        print("Quantity of books borrowed: ", qtyEx)
                        extra = int(qtyEx) + int(currentDict[borrowBookID][2])
                        currentDict[borrowBookID][2] = str(extra)
                        dFile = open("stock.txt", "w")
                        dFile.write("")

                        for values in currentDict.values():
                            eFile = open("stock.txt", "a")
                            eFile.write(
                                str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                            eFile.write("\n")
                        eFile.close()

                        with open("notes.txt", "w") as fp:
                            for number, line in enumerate(notesList):
                                if number != i:
                                    fp.write(line)
                        
                        print("\nName of Borrower: {}\nBook Name: {}\nBook Quantity: {}\nFine Amount: ${}".format(checkName, currentDict[borrowBookID][0], str(qtyEx), fineAmt))
                    else:
                        print("\nYou have not borrowed a book.")
                        exit()

            elif pick == 3:
                print("\nThank you for visiting the library!")
                os._exit(0)

            else:
                print("\nPlease enter a valid choice!")
                dispMenu()

        except:
            print("\nPlease enter a valid choice!")

if __name__ == "__main__":
    currentDict = libdict({}).copy()
    dispMenu()