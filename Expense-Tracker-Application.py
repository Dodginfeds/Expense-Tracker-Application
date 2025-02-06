# ---------------------------------------------
# Expense Tracker Application
# ---------------------------------------------
# This program allows users to:
# 1. Add expenses: Enter a description and an amount.
# 2. View all expenses: Display all expenses with their total cost.
# 3. Remove an expense: Remove an expense by its description.
# 4. Save expenses to a file (optional).
# 5. Quit the program when done.
# ---------------------------------------------

import json

# Dictionary to store expenses
expenses = {}

# ---------------------------------------------
# Function to Add an Expense
# ---------------------------------------------

def add_expense():
    """
    Adds an expense with a description and a price.
    """
    try:
        description = input("Enter the expense description: ").strip().lower()

        if description.isnumeric():
            raise ValueError("Expense description cannot be a numeric value!")

        price = float(input("Enter the price of the expense: "))

        if description in expenses:
            expenses[description].append(price)
        else:
            expenses[description] = [price]

        print(f"Expense '{description}' of ${price:.2f} has been added!")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")

# ---------------------------------------------
# Function to View Expenses
# ---------------------------------------------

def view_expenses():
    """
    Displays all recorded expenses along with the total amount.
    """
    if not expenses:
        print("\nYou don't have any expenses recorded.")
    else:
        print("\nYour Current Expenses:")
        total = 0
        for i, (description, amounts) in enumerate(expenses.items(), start=1):
            for price in amounts:
                print(f"{i}. {description}: ${price:.2f}")
                total += price

        print(f"\nTotal Expenses: ${total:.2f}")

# ---------------------------------------------
# Function to Remove an Expense
# ---------------------------------------------

def remove_expense():
    """
    Removes a specific expense or clears all expenses.
    """
    try:
        if not expenses:
            print("\nThere are no expenses to remove!")
            return
        
        question = input("\nEnter the expense you want to remove (or type 'C' to clear all): ").strip().lower()

        if question.isnumeric():
            raise ValueError("You cannot enter a number as an expense name.")

        if question == 'c':
            confirmation = input("Are you sure you want to clear your entire expense list? (Y/N): ").strip().lower()
            if confirmation == "y":
                expenses.clear()
                print("All expenses have been cleared!")
            else:
                print("Returning to the menu...")
        
        elif question not in expenses:
            raise KeyError(f"'{question}' is not in your expense list.")

        else:
            expenses.pop(question)
            print(f"'{question}' has been removed from your list!")

    except Exception as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to Save Expenses to a File (Optional)
# ---------------------------------------------

def save_expenses():
    """
    Saves the current expense list to a JSON file.
    """
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!")

# ---------------------------------------------
# Function to Load Expenses from a File (Optional)
# ---------------------------------------------

def load_expenses():
    """
    Loads expenses from a JSON file if available.
    """
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        print("Previous expenses loaded successfully!")
    except FileNotFoundError:
        print("No previous expense records found. Starting fresh!")

# ---------------------------------------------
# Function to Handle User Menu Choices
# ---------------------------------------------

def menu():
    """
    Provides an interactive menu for managing expenses.
    """
    load_expenses()  # Load expenses at program start

    while True:
        try:
            print("\n--- Expense Tracker Menu ---")
            print("1. Add an Expense")
            print("2. View Expenses")
            print("3. Remove an Expense")
            print("4. Save & Quit")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                remove_expense()
            elif choice == 4:
                save_expenses()
                confirm = input("Are you sure you want to quit? (Y/N): ").strip().lower()
                if confirm == "y":
                    print("Thank you for using the Expense Tracker! Goodbye! 👋")
                    break
                else:
                    print("Returning to the menu...")
            else:
                print("Invalid option! Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Expense Tracker App!")
    menu()
