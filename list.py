import tkinter as tk
import math

# This is a function to update the entry widget with the selected number or operation.
def update_entry(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Here is a function to clear the entry widget.
def clear_entry():
    entry.delete(0, tk.END)

# Here is a function to calculate the factorial of a entered number.
def factorial():
    try:
        result = math.factorial(int(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate the square root of a number
def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create a main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#262626")

# Create entry widget
entry = tk.Entry(root, font=('Times New Roman', 20), justify="right", bg="#262626", fg="#E6E6E6", insertbackground="#E6E6E6")
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

# Define button labels
button_labels = [
    ('7', '8', '9', '/', 'C'),
    ('4', '5', '6', '*', 'π'),
    ('1', '2', '3', '-', 'e'),
    ('.', '0', '^', '+', '√'),
    ('(', ')', '!', '=', 'log')
]

# Create buttons
for i in range(5):
    for j in range(5):
        label = button_labels[i][j]
        if label == '=':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=calculate, bg="#b300b3").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif label == 'C':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=clear_entry, bg="#e6e600").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif label == 'π' or label == 'e':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=lambda value=label: update_entry(value), bg="#e6e600").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif label == '√':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=square_root, bg="#e6e600").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif label == '!':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=factorial, bg="#e6e600").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif label == '^':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=lambda value='**': update_entry(value), bg="#e6e600").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        elif label == 'log':
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=lambda value='log(': update_entry(value), bg="#e6e600").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        else:
            tk.Button(root, text=label, font=('Times New Roman', 16), padx=20, pady=20, command=lambda value=label: update_entry(value), bg="#d9d9d9").grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

# Configure grid row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Run the main event loop
root.mainloop()