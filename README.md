INTERN ID : CITS8754

# 💰 Expense Tracker

A simple **Python-based Expense Tracker** that allows users to add, view, and analyze their daily expenses. The project stores expense data in both **CSV and JSON formats**.

## 📌 Features

* ➕ Add expenses directly from the terminal
* 📋 View all recorded expenses
* 💰 Calculate total expenses
* 📊 View category-wise expense summary
* 💾 Store data in CSV format
* 🗂️ Store data in JSON format
* 📅 Automatically records the current date
* 🐍 Built completely using Python

## 🛠️ Technologies Used

* **Python 3**
* CSV File Handling
* JSON File Handling
* `datetime` module
* Basic Python concepts:

  * Functions
  * Lists
  * Dictionaries
  * Loops
  * Conditional statements
  * File handling

## 📂 Project Structure

```text
ExpenseTracker/
│
├── expense_tracker.py
├── expenses.csv
├── expenses.json
└── README.md
```

### Files Description

| File                 | Description                    |
| -------------------- | ------------------------------ |
| `expense_tracker.py` | Main Python program            |
| `expenses.csv`       | Stores expenses in CSV format  |
| `expenses.json`      | Stores expenses in JSON format |
| `README.md`          | Project documentation          |

## 🚀 How to Run

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project

```bash
cd ExpenseTracker
```

### Step 3: Run the program

```bash
python expense_tracker.py
```

## 🖥️ Main Menu

When you run the program, you will see:

```text
==============================
       EXPENSE TRACKER
==============================

1. Add Expense
2. View Expenses
3. Show Total Expenses
4. Category Summary
5. Exit

Enter your choice:
```

## ➕ Adding an Expense

Select option `1`.

Example:

```text
Enter your choice: 1

--- Add Expense ---
Enter category: Food
Enter amount: 250
Enter description: Lunch

Expense added successfully!
```

The expense will automatically be saved to both the CSV and JSON files.

## 📋 Viewing Expenses

Select option `2`.

Example output:

```text
---------------- EXPENSES ----------------
Date           Category       Amount      Description
------------------------------------------------------------
2026-09-02     Food           ₹250        Lunch
2026-09-02     Travel         ₹100        Metro
2026-09-02     Shopping       ₹500        T-Shirt
```

## 💰 Total Expenses

Select option `3`.

Example:

```text
Total Expenses: ₹850.00
```

## 📊 Category Summary

Select option `4`.

Example:

```text
-------- CATEGORY SUMMARY --------
Food: ₹250.00
Travel: ₹100.00
Shopping: ₹500.00
```

## 💾 Data Storage

### CSV

Example `expenses.csv`:

```csv
date,category,amount,description
2026-09-02,Food,250,Lunch
2026-09-02,Travel,100,Metro
2026-09-02,Shopping,500,T-Shirt
```

### JSON

Example `expenses.json`:

```json
[
    {
        "date": "2026-09-02",
        "category": "Food",
        "amount": "250",
        "description": "Lunch"
    },
    {
        "date": "2026-09-02",
        "category": "Travel",
        "amount": "100",
        "description": "Metro"
    }
]
```

## 🎯 Project Objective

The main objective of this project is to create a simple personal expense management system using Python. It demonstrates how Python can be used for **file handling and basic data management**.

## 🔮 Future Improvements

The project can be improved by adding:

* 🔐 User login system
* ✏️ Edit expenses
* 🗑️ Delete expenses
* 🔍 Search expenses
* 📅 Monthly expense reports
* 📈 Expense charts and graphs
* 💳 Income and savings tracking
* 🖥️ GUI using Tkinter
* 🌐 Web version using Flask or Django
* 🗄️ Database support using SQLite/MySQL

## 👨‍💻 Author

**Abhijeet Singh**

BCA (AI/ML)

## 📄 License

This project is created for **educational and academic purposes**.
