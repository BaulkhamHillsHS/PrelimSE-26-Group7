import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("nice")
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.combobox_var = customtkinter.StringVar(value="option 2")
        self.combobox = customtkinter.CTkComboBox(self, values=["option 1", "option 2"],
                                            command=self.combobox_callback, variable=self.combobox_var)
        self.combobox_var.set("option 2")
        self.combobox.grid(row=0, column=0)
    def combobox_callback(self, choice):
        if choice == "option 1":
            print("AH")
        elif choice == "option 2":
            print("yeah")
        if choice == None:
            print("nice")
app = App()
app.mainloop()