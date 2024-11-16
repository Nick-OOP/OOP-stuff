import tkinter as tk

top = tk.Tk()
top.geometry("580x750")
top.title("Simple Calculator")
top.configure(bg="black")
answer = tk.Text(top, width=35, height=2, bg="black", fg="white", font=("Helvetica", 14), bd=0, highlightthickness=0)
answer.grid(row=1, column=0, columnspan=4, padx=10, pady=0)
answer.tag_configure("right", justify="right")

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.delete(1.0, tk.END)
            answer.insert(1.0, final_answer, "right")
        elif x == "d":
            content = answer.get(1.0, "end-1c")
            if content:
                answer.delete(1.0, tk.END)
                answer.insert(1.0, content[:-1], "right")
        elif x == "c":  # Clear all text
            answer.delete(1.0, tk.END)
        elif x == "%":
            content = answer.get(1.0, "end-1c")
            if "/" in content:
                parts = content.split("/")
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    numerator = float(parts[0])
                    denominator = float(parts[1])
                    percent = (numerator / denominator) * 100
                    answer.delete(1.0, tk.END)
                    answer.insert(1.0, f"{percent}%", "right")
                # else:
                #     answer.insert(1.0, "Error", "right")
            else:
                number = float(content)
                percent = number * 100
                answer.delete(1.0, tk.END)
                answer.insert(1.0, f"{percent}%", "right")
        else:
            answer.insert(tk.INSERT, x, "right")
    except:
        final_answer = "Error"
        answer.insert(tk.INSERT, final_answer, "right")

# I found out how to make this cool button grid and save some lines of code. As a bonus, it lines up all the buttons and makes them scalable with the window.
buttons = [
    ("Delete", "Clear All", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", None, ".", "=")
]

for row, button_row in enumerate(buttons):
    for col, text in enumerate(button_row):
        if text == "Clear All":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("c"), bg="grey", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "Delete":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("d"), bg="grey", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "%":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("%"), bg="grey", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "0":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("0"), bg="#383838", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
        elif text == "/":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("/"), bg="orange", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "*":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("*"), bg="orange", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "-":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("-"), bg="orange", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "+":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("+"), bg="orange", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text == "=":
            button = tk.Button(top, text=text, width=7, height=3, command=lambda: show("="), bg="orange", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)
        elif text is not None:
            button = tk.Button(top, text=text, width=7, height=3, command=lambda x=text: show(x), bg="#383838", fg="white", font=("Helvetica"))
            button.grid(row=row+2, column=col, sticky="nsew", padx=5, pady=5)

for i in range(5):
    top.grid_rowconfigure(i, weight=1)
    for j in range(4):
        top.grid_columnconfigure(j, weight=1)

top.mainloop()
