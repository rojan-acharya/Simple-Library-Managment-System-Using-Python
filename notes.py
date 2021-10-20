import datetime

def libdict(x):
    ldict = {}
    count = 1
    library = open("stock.txt", "r")
    for line in library:
        line = line.replace("\n", "")
        line = line.replace("$", "")
        ldict[count] = line.split(",")
        count = count+1
    return ldict

def readBooks():
    print("_____________________________________________________________________________________________________")
    print("Books ID\tBooks List\t    Author's Name\t\t   Quantity   \t  Price")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    file = open("stock.txt", "r")
    id = 1

    for line in file:
        print(id, "\t\t"+line.replace(",", "\t\t"))
        id = id+1
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def genNotes():
    print("_____________________________________________________________________________________________________")
    print("Name\t\t  Books Id\t\tQuantity\t\tPrice\t\tDate")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    file = open("notes.txt", "r")
    for line in file:
        print("" + line.replace(",", "\t\t  "))


def getCurrentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")