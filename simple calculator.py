import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for button_text in buttons:
    b = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 14),
                  command=lambda bt=button_text: click(bt))
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
