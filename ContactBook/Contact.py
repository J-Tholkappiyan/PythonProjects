import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        phone TEXT,
                        email TEXT,
                        address TEXT)''')  # Removed 'company' field
    conn.commit()
    conn.close()


def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()
    
    if not name:
        messagebox.showerror("Error", "Name is required!")
        return
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Phone must be exactly 10 digits!")
        return
    if not email.endswith("@gmail.com"):
        messagebox.showerror("Error", "Email must be a valid @gmail.com address!")
        return
    
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                   (name, phone, email, address))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()
    view_contacts()


def update_contact():
    selected_item = contact_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a contact to update.")
        return
    
    item = contact_list.item(selected_item)
    contact_id = item["values"][0]
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()
    
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?", 
                   (name, phone, email, address, contact_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Contact updated successfully!")
    clear_fields()
    view_contacts()


def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    
    contact_list.delete(*contact_list.get_children())
    for row in rows:
        contact_list.insert("", tk.END, values=row)


def search_contact():
    search_term = search_var.get()
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + search_term + '%',))
    rows = cursor.fetchall()
    conn.close()
    
    contact_list.delete(*contact_list.get_children())
    for row in rows:
        contact_list.insert("", tk.END, values=row)


def delete_contact():
    selected_item = contact_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return
    
    item = contact_list.item(selected_item)
    contact_id = item["values"][0]
    
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contacts()


def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")
    search_var.set("")


root = tk.Tk()
root.title("Contact Management System")
root.geometry("750x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, padx=10, pady=10, bg="#ffffff", relief=tk.RIDGE, borderwidth=2)
frame.pack(pady=10, padx=10, fill="both", expand=True)

title = tk.Label(frame, text="Contact Management System", font=("Arial", 16, "bold"), bg="#ffffff")
title.grid(row=0, column=0, columnspan=3, pady=10)

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

labels = ["Name:", "Phone:", "Email:", "Address:"]
vars = [name_var, phone_var, email_var, address_var]

for i in range(4):
    tk.Label(frame, text=labels[i], bg="#ffffff").grid(row=i+1, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=vars[i], width=40).grid(row=i+1, column=1, pady=5)

tk.Label(frame, text="Search Name:", bg="#ffffff").grid(row=5, column=0, sticky="w", pady=5)
search_entry = tk.Entry(frame, textvariable=search_var, width=30)
search_entry.grid(row=5, column=1, pady=5)
tk.Button(frame, text="Search", command=search_contact, bg="#2196F3", fg="white", width=20).grid(row=5, column=2, pady=5, padx=5)

tk.Button(frame, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=20).grid(row=6, column=0, pady=10)
tk.Button(frame, text="Update Contact", command=update_contact, bg="#FFC107", fg="black", width=20).grid(row=6, column=1, pady=10)
tk.Button(frame, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white", width=20).grid(row=7, column=1, pady=10)
tk.Button(frame, text="Clear Fields", command=clear_fields, bg="#9E9E9E", fg="white", width=20).grid(row=7, column=0, pady=10)

columns = ("ID", "Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, width=150, anchor="center")
contact_list.grid(row=8, column=0, columnspan=3, pady=10, sticky="nsew")

frame.grid_rowconfigure(8, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

init_db()
view_contacts()
root.mainloop()
