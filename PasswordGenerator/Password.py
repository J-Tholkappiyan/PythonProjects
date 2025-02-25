import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    """Generate a strong password based on user input"""
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Warning", "Password length should be at least 8 Characters.")
            return
        
        characters = string.ascii_letters + string.digits
        if special_var.get():
            characters += string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.config(state=tk.NORMAL, bg="#F9E79F", fg="#154360", font=("Arial", 12, "bold"))  # Updated styles
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

def copy_to_clipboard():
    """Copy the generated password to clipboard"""
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update_idletasks()
        messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("420x300")
root.configure(bg="#2C3E50")  # Background color


title_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)


tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#2C3E50", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, bg="white", fg="black")
length_entry.pack(pady=5)


special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", font=("Arial", 10), variable=special_var, bg="#2C3E50", fg="white", selectcolor="#34495E")
special_checkbox.pack()


generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#1ABC9C", fg="white", activebackground="#16A085", activeforeground="white", padx=10, pady=5, command=generate_password)
generate_button.pack(pady=10)


password_entry = tk.Entry(root, font=("Arial", 12, "bold"), width=30, bg="#F9E79F", fg="#154360", state=tk.DISABLED, justify="center", relief="solid", bd=2)
password_entry.pack(pady=5)


copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", activebackground="#C0392B", activeforeground="white", padx=10, pady=5, command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
