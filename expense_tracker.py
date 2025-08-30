import tkinter as tk
from tkinter import ttk, messagebox

expenses = []

def add_expense(category):
    desc = desc_entry.get().strip()
    amount = amount_entry.get().strip()
    if not desc or not amount:
        messagebox.showwarning("Missing Info", "Please enter both description and amount.")
        return
    try:
        amount = float(amount)
        full_desc = f"{category} {desc}"
        expenses.append((full_desc, amount))
        update_list()
        desc_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number.")

def update_list():
    listbox.delete(0, tk.END)
    total = 0
    for desc, amount in expenses:
        listbox.insert(tk.END, f"{desc} — ${amount:.2f}")
        total += amount
    total_label.config(text=f"Total Spent: ${total:.2f}")

def clear_expenses():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all expenses?"):
        expenses.clear()
        update_list()

# Main window
root = tk.Tk()
root.title("💰 Vladimir's Expense Tracker")
root.geometry("600x600")
root.minsize(500, 500)
root.configure(bg="#f0f4f8")

# Grid configuration
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# Description input
tk.Label(root, text="Description", font=("Helvetica", 12), bg="#f0f4f8").grid(row=0, column=0, padx=10, pady=10, sticky="e")
desc_entry = ttk.Entry(root, font=("Helvetica", 12))
desc_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

# Amount input
tk.Label(root, text="Amount", font=("Helvetica", 12), bg="#f0f4f8").grid(row=1, column=0, padx=10, pady=10, sticky="e")
amount_entry = ttk.Entry(root, font=("Helvetica", 12))
amount_entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")

# Category buttons
tk.Label(root, text="Choose Category", font=("Helvetica", 12), bg="#f0f4f8").grid(row=2, column=0, columnspan=2, pady=(10, 0))
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.grid(row=3, column=0, columnspan=2, pady=5)

categories = [
    ("🍔 Food", "#FFB74D"),
    ("🛍️ Shopping", "#BA68C8"),
    ("🚗 Transport", "#4FC3F7"),
    ("🎉 Entertainment", "#81C784"),
    ("🧾 Other", "#E57373")
]

for i, (cat, color) in enumerate(categories):
    btn = tk.Button(btn_frame, text=cat, font=("Helvetica", 11, "bold"), bg=color, fg="white",
                    command=lambda c=cat: add_expense(c))
    btn.grid(row=0, column=i, padx=5, ipadx=10)

# Expense list
listbox = tk.Listbox(root, font=("Courier", 11), height=10)
listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Make listbox expand with window
root.rowconfigure(4, weight=1)

# Total label
total_label = tk.Label(root, text="Total Spent: $0.00", font=("Helvetica", 14, "bold"), bg="#f0f4f8", fg="#333")
total_label.grid(row=5, column=0, columnspan=2, pady=10)

# Clear button
tk.Button(root, text="🗑️ Clear All", font=("Helvetica", 11, "bold"), bg="#f44336", fg="white",
          command=clear_expenses).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()