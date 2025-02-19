expenses = []
expense1 = {'amount': '£34.00', 'category': 'creps'}
expenses.append(expense1)
expense2 = {'amount': '£53.00', 'category': 'vbucks'}
expenses.append(expense2)

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("Invalid input. Please try again.")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. List All Expenses")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("-------------------------------------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

if __name__ == "__main__":
    while True:
     ### Prompt the user
     printMenu()
     optionSelected = input("> ")

     if(optionSelected == "1"):
        print("How much was this expense?")
        while True:
            try:
                amountToAdd = input("> ")
                break
            except:
                print("Invalid input. Please try again.")

        print("What category was this expense?")
        while True:
            try:
                category = input("> ")
                break
            except:
                print("Invalid input. Please try again.")

        addExpense(amountToAdd, category)
     elif(optionSelected == "2"):
         removeExpense()
     elif(optionSelected == "3"):
         listExpenses()
     else:
         print("Invalid input. Please try again.")