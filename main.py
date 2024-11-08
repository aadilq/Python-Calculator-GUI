import tkinter as tk 

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry field
        self.entry = tk.Entry(master, width=30, justify='right', font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 2)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("=", 4, 0)
        self.create_button("C", 5, 0)
        self.create_button("CE", 5, 1)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)