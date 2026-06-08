import customtkinter
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.name = App.title
        self.label = customtkinter.CTkLabel(self, text=self.name)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("nice")
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)


        self.my_frame = MyFrame(self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()