from main import borrower

def promptMore():
    borrowMore = input("Do you want to borrow more books [y/n]? => ")
    if borrowMore == 'y' or borrowMore == 'Y':
        borrower()
    elif borrowMore == 'n' or borrowMore == 'N':
        print("Thank you!")
    else:
        print("Please select a valid value! (Y/N)")
        
