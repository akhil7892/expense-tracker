import csv
import json
import os
from datetime import datetime

CSV_FILE = "expenses.csv"
JSON_FILE = "expenses.json"


# ---------------- CSV FUNCTIONS ----------------

def load_csv_expenses():
    expenses = []

    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    return expenses


def save_csv_expense(expense):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:
        fieldnames = ["date", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(expense)


# ---------------- JSON FUNCTIONS ----------------

def load_json_expenses():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    return []


def save_json_expenses(expenses):
    with open(JSON_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


# ---------------- ADD EXPENSE ----------------

def add_expense():
    print("\n--- Add Expense ---")

    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    # Save to CSV
    save_csv_expense(expense)

    # Save to JSON
    expenses = load_json_expenses()
    expenses.append(expense)
    save_json_expenses(expenses)

    print("\nExpense added successfully!")


# ---------------- VIEW EXPENSES ----------------

def view_expenses():
    expenses = load_json_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n---------------- EXPENSES ----------------")
    print(f"{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<11}"
            f"{expense['description']}"
        )


# ---------------- TOTAL EXPENSE ----------------

def total_expenses():
    expenses = load_json_expenses()

    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    print(f"\nTotal Expenses: ₹{total:.2f}")


# ---------------- CATEGORY SUMMARY ----------------

def category_summary():
    expenses = load_json_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n-------- CATEGORY SUMMARY --------")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


# ---------------- MAIN MENU ----------------

def main():
    while True:

        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Start program
if __name__ == "__main__":
    main()