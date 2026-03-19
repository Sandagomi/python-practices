import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Function to update entry
def click(value):
    entry.insert(tk.END, value)

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            action = calculate
        elif btn == "C":
            action = clear
        else:
            action = lambda x=btn: click(x)

        tk.Button(frame, text=btn, font=("Arial", 16),
                  command=action).pack(side="left", expand=True, fill="both")

# Run app
root.mainloop()