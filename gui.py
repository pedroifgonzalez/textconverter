import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(False, False)
        self.configure(background='')
        self.pack()
        self.create_buttons()
    
    def create_buttons(self):
        common_options = dict(
            activebackground="pink",
            anchor="w"
        )

        title_button = tk.Button(self, text="AbC", **common_options)
        after_period_capitalize_button = tk.Button(self, text="Ab.C", **common_options)
        uppercase_button = tk.Button(self, text="A", **common_options)
        lowercase_button = tk.Button(self, text="a", **common_options)
        capitalize_button = tk.Button(self, text="Ab", **common_options)

        uppercase_button.pack(fill="x")
        lowercase_button.pack(fill="x")
        capitalize_button.pack(fill="x")
        title_button.pack(fill="x")
        after_period_capitalize_button.pack(fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()