import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result.set(f"{num1} + {num2} = {num1 + num2}")
        elif operation == "-":
            result.set(f"{num1} - {num2} = {num1 - num2}")
        elif operation == "*":
            result.set(f"{num1} * {num2} = {num1 * num2}")
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result.set(f"{num1} / {num2} = {num1 / num2:.2f}")
        else:
            messagebox.showerror("Error", "Invalid Operation")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

def on_key_press(event):
    if event.keysym == "Return":
        calculate()

root = tk.Tk()
root.title("Responsive Calculator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

entry1 = tk.Entry(frame, font=("Arial", 14), width=10)
entry1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

operation_var = tk.StringVar(root)
operation_var.set("+")
operations_menu = tk.OptionMenu(frame, operation_var, "+", "-", "*", "/")
operations_menu.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(frame, font=("Arial", 14), width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

result_frame = tk.Frame(root, bg="#f0f0f0")
result_frame.pack(pady=10)

result = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=result, font=("Arial", 16, "bold"), bg="#f0f0f0")
result_label.grid(row=0, column=0, padx=10, pady=10)

buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=20)

calculate_btn = tk.Button(buttons_frame, text="Calculate", command=calculate, font=("Arial", 14), bg="#4CAF50", fg="white")
calculate_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")

clear_btn = tk.Button(buttons_frame, text="Clear", command=clear, font=("Arial", 14), bg="#f44336", fg="white")
clear_btn.grid(row=0, column=1, padx=5, pady=5, sticky="w")

root.bind("<Return>", on_key_press)

root.mainloop()
