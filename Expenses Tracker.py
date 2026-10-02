import json
from datetime import datetime

FILE = "expenses.json"

def load_expenses():
    try: 
        with open(FILE,"r")as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expenses(expenses):
    amount = float(input("Enter amount :"))
    category = input("Enter category (Food/Traval/Shopping/etc.):")
    note = input("Enter  note : ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    save_expenses(expenses)
    
    print("Expenses added Successfully !")

def show_expenses(expenses):
    if not expenses:
        print ("No expenses recorded.")
        return
    
        print("\n------ Your Expenses ------")

        for i, expense in enumerate(expenses, 1):
            print(
                f"{i}.{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['note']} | "
                f"{expense['date']}"
            )
def show_total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: {total:.2f}")
def main():
    expenses = load_expenses()
    while True:
        print("\n------ Expense Tracker ------")
        print("1. Add Expenses")
        print("2. Show Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_total_expenses(expenses)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")  


if __name__ == "__main__":
    main()
