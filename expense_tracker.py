import tkinter as tk
from tkinter import messagebox, Scrollbar

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

# Main window setup
root = tk.Tk()
root.title("💰 Vladimir's Expense Tracker")
root.geometry("420x550")
root.configure(bg="#f0f4f8")

LABEL_FONT = ("Helvetica", 12)
ENTRY_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 11, "bold")

# Description input
tk.Label(root, text="Description", font=LABEL_FONT, bg="#f0f4f8").pack(pady=(20, 5))
desc_entry = tk.Entry(root, font=ENTRY_FONT, width=30)
desc_entry.pack(pady=5)

# Amount input
tk.Label(root, text="Amount", font=LABEL_FONT, bg="#f0f4f8").pack(pady=(10, 5))
amount_entry = tk.Entry(root, font=ENTRY_FONT, width=30)
amount_entry.pack(pady=5)

# Category buttons
tk.Label(root, text="Choose Category", font=LABEL_FONT, bg="#f0f4f8").pack(pady=(15, 5))
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack()

categories = [
    ("🍔 Food", "#FFB74D"),
    ("🛍️ Shopping", "#BA68C8"),
    ("🚗 Transport", "#4FC3F7"),
    ("🎉 Entertainment", "#81C784"),
    ("🧾 Other", "#E57373")
]

for cat, color in categories:
    tk.Button(btn_frame, text=cat, font=BUTTON_FONT, bg=color, fg="white",
              command=lambda c=cat: add_expense(c)).pack(side="left", padx=5, pady=5)

# Expense list with scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=45, height=10, font=("Courier", 11), yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Total label
total_label = tk.Label(root, text="Total Spent: $0.00", font=("Helvetica", 14, "bold"), bg="#f0f4f8", fg="#333")
total_label.pack(pady=20)

# Clear button
tk.Button(root, text="🗑️ Clear All", font=BUTTON_FONT, bg="#f44336", fg="white",
          command=clear_expenses).pack(pady=10)

root.mainloop()