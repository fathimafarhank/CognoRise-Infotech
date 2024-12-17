import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif text == "AC":
        entry.delete(0, tk.END)
    elif text == "DEL":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])  # Remove the last character
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")
root.configure(bg="white")  # Set the background color to white

# Entry widget for display
entry = tk.Entry(root, font=("Arial", 24), justify=tk.RIGHT, bd=5, bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ["AC", "DEL", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Button colors and styles
btn_font = ("Arial", 16)
btn_color = {"default": "lightgray", "orange": "#ffa500", "bg": "white", "fg": "black"}

# Create and place buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "":
            continue
        color = btn_color["orange"] if text in {"/", "*", "-", "+", "="} else btn_color["default"]
        btn = tk.Button(
            root,
            text=text,
            font=btn_font,
            bg=color,
            fg=btn_color["fg"],
            width=5,
            height=2,
            relief=tk.RAISED
        )
        btn.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", on_click)

# Adjust grid weights for responsiveness
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i + 1, weight=1)

# Run the main loop
root.mainloop()
