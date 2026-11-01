import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# -----------------------------
# 1. Create the main window
# -----------------------------

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("850x650")
root.minsize(750, 550)

# Store transactions in a file beside this Python file
FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "transactions.json"
)

transactions = []


# -----------------------------
# 2. Load saved transactions
# -----------------------------

def load_transactions():
    global transactions

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                transactions = json.load(file)

            if not isinstance(transactions, list):
                transactions = []

        except (json.JSONDecodeError, OSError):
            transactions = []
            messagebox.showwarning(
                "Warning",
                "Could not load saved transactions."
            )


# -----------------------------
# 3. Save transactions
# -----------------------------

def save_transactions():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(transactions, file, indent=4)

        return True

    except OSError:
        messagebox.showerror(
            "File Error",
            "Could not save transactions."
        )
        return False


# -----------------------------
# 4. Update financial summary
# -----------------------------

def update_summary():
    total_income = sum(
        item["amount"]
        for item in transactions
        if item["type"] == "Income"
    )

    total_expenses = sum(
        item["amount"]
        for item in transactions
        if item["type"] == "Expense"
    )

    balance = total_income - total_expenses

    income_label.config(
        text=f"Total Income: {total_income:.2f}"
    )

    expense_label.config(
        text=f"Total Expenses: {total_expenses:.2f}"
    )

    balance_label.config(
        text=f"Balance: {balance:.2f}"
    )


# -----------------------------
# 5. Display transaction history
# -----------------------------

def refresh_table():
    # Remove the old rows
    for item in transaction_table.get_children():
        transaction_table.delete(item)

    # Insert all transactions again
    for index, transaction in enumerate(transactions):
        transaction_table.insert(
            "",
            "end",
            iid=str(index),
            values=(
                transaction["description"],
                transaction["type"],
                f'{transaction["amount"]:.2f}'
            )
        )

    update_summary()


# -----------------------------
# 6. Add income or expense
# -----------------------------

def add_transaction(transaction_type):
    description = description_entry.get().strip()
    amount_text = amount_entry.get().strip()

    # Check the description
    if not description:
        messagebox.showwarning(
            "Missing Description",
            "Please enter a description."
        )
        return

    # Convert the amount into a number
    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showwarning(
            "Invalid Amount",
            "Please enter a valid number."
        )
        return

    # Check that the amount is positive
    if amount <= 0:
        messagebox.showwarning(
            "Invalid Amount",
            "The amount must be greater than zero."
        )
        return

    # Create a transaction dictionary
    transaction = {
        "description": description,
        "type": transaction_type,
        "amount": amount
    }

    # Add the transaction to our list
    transactions.append(transaction)

    # Save the updated list
    if not save_transactions():
        transactions.pop()
        return

    # Update the table and financial summary
    refresh_table()

    # Clear the input fields
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        f"{transaction_type} added successfully!"
    )


# -----------------------------
# 7. Delete a selected transaction
# -----------------------------

def delete_transaction():
    selected_items = transaction_table.selection()

    if not selected_items:
        messagebox.showwarning(
            "No Selection",
            "Please select a transaction to delete."
        )
        return

    selected_index = int(selected_items[0])

    # Ask before deleting
    confirm = messagebox.askyesno(
        "Confirm Deletion",
        "Are you sure you want to delete this transaction?"
    )

    if not confirm:
        return

    # Temporarily remove the selected transaction
    deleted_transaction = transactions.pop(selected_index)

    # Save the updated list
    if not save_transactions():
        transactions.insert(
            selected_index,
            deleted_transaction
        )
        return

    refresh_table()

    messagebox.showinfo(
        "Success",
        "Transaction deleted successfully!"
    )


# -----------------------------
# 8. Design the graphical interface
# -----------------------------

heading = tk.Label(
    root,
    text="Personal Finance Tracker",
    font=("Arial", 24, "bold")
)
heading.pack(pady=15)


# Financial summary
summary_frame = tk.Frame(root)
summary_frame.pack(pady=10)

income_label = tk.Label(
    summary_frame,
    text="Total Income: 0.00",
    font=("Arial", 12, "bold")
)
income_label.grid(row=0, column=0, padx=15)

expense_label = tk.Label(
    summary_frame,
    text="Total Expenses: 0.00",
    font=("Arial", 12, "bold")
)
expense_label.grid(row=0, column=1, padx=15)

balance_label = tk.Label(
    summary_frame,
    text="Balance: 0.00",
    font=("Arial", 12, "bold")
)
balance_label.grid(row=0, column=2, padx=15)


# Input section
input_frame = tk.Frame(root)
input_frame.pack(pady=15)

tk.Label(
    input_frame,
    text="Description:"
).grid(row=0, column=0, padx=5, pady=5)

description_entry = tk.Entry(
    input_frame,
    width=25
)
description_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(
    input_frame,
    text="Amount:"
).grid(row=1, column=0, padx=5, pady=5)

amount_entry = tk.Entry(
    input_frame,
    width=25
)
amount_entry.grid(row=1, column=1, padx=5, pady=5)


# Income and expense buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

income_button = tk.Button(
    button_frame,
    text="Add Income",
    width=15,
    command=lambda: add_transaction("Income")
)
income_button.grid(row=0, column=0, padx=10)

expense_button = tk.Button(
    button_frame,
    text="Add Expense",
    width=15,
    command=lambda: add_transaction("Expense")
)
expense_button.grid(row=0, column=1, padx=10)


# Transaction history table
table_frame = tk.Frame(root)
table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)

columns = ("Description", "Type", "Amount")

transaction_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=10
)

transaction_table.heading(
    "Description",
    text="Description"
)

transaction_table.heading(
    "Type",
    text="Type"
)

transaction_table.heading(
    "Amount",
    text="Amount"
)

transaction_table.column(
    "Description",
    width=350
)

transaction_table.column(
    "Type",
    width=150,
    anchor="center"
)

transaction_table.column(
    "Amount",
    width=150,
    anchor="e"
)

# Add a scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=transaction_table.yview
)

transaction_table.configure(
    yscrollcommand=scrollbar.set
)

transaction_table.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Delete button
delete_button = tk.Button(
    root,
    text="Delete Selected Transaction",
    command=delete_transaction
)
delete_button.pack(pady=10)


# -----------------------------
# 9. Start the application
# -----------------------------

load_transactions()
refresh_table()

root.mainloop()