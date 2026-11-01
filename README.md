#  Personal Finance Tracker

A beginner-friendly desktop application built with Python and Tkinter to track income, expenses, and personal finances.

##  About the Project

The Personal Finance Tracker helps users record their income and expenses through a simple graphical interface. It automatically calculates total income, total expenses, and the remaining balance.

Transactions are saved in a JSON file, so they remain available when the application is reopened.

##  Features

- Add income transactions.
- Record expenses.
- View total income and expenses.
- Calculate the remaining balance automatically.
- Display transactions in a table.
- Delete selected transactions.
- Save transaction data locally.
- Validate descriptions and amounts.
- Display warning messages for invalid inputs.
- Simple desktop graphical interface.

##  Technologies Used

- Python
- Tkinter
- JSON
- File Handling

##  Project Structure

```text
finance_tracker_gui/
│
├── app.py
├── README.md
└── transactions.json  # Created automatically when transactions are saved
```

##  How to Run

### 1. Install Python

Install Python if it is not already installed.

### 2. Download or Clone the Project

Download this repository from GitHub and extract it, or clone it using Git.

### 3. Open the Project

Open the project folder in VS Code.

### 4. Run the Application

Open the terminal in the project folder and execute:

```bash
python app.py
```

The Personal Finance Tracker window should open.

##  How to Use

1. Enter a transaction description, such as Salary or Food.
2. Enter the amount.
3. Click **Add Income** or **Add Expense**.
4. View the updated financial summary.
5. Check your transaction history in the table.
6. Select a transaction and click **Delete Selected Transaction** to remove it.

Transactions are stored locally in `transactions.json`.

##  What I Learned

Through this project, I practised:

- Creating graphical interfaces with Tkinter.
- Using Python functions.
- Working with lists and dictionaries.
- Handling user input.
- Converting text into numbers.
- Using conditional statements.
- Calculating totals with `sum()`.
- Reading and writing JSON files.
- Handling exceptions.
- Displaying tabular data with `ttk.Treeview`.
- Updating GUI elements dynamically.

##  Future Improvements

- Add transaction dates.
- Search and filter transactions.
- Add monthly expense reports.
- Display spending charts.
- Export transaction records to CSV.
- Improve the interface design.

##  Author

Obaid

##  License

This project is available for learning and personal use.
