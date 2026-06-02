import customtkinter as ctk
import csv
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self, *args):
        super().__init__()
        self.geometry("650x680")
        #create the UI and show it on screen
        self._build_ui()
        self.title("Login")
    def _build_ui(self):
        #giving different weights to different columns
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=20)
        #giving different weights to different rows
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1,2), weight=8)
        self.grid_rowconfigure((3), weight=2)
        #Login Label
        self.label = ctk.CTkLabel(self, width= 80, height= 20, text="Login", bg_color= "transparent")
        self.label.grid(row=0, column=0, sticky= "nsw", padx=10, pady=10, columnspan=2)
        #Username
        self.username_label = ctk.CTkLabel(self, width=20, height=10, text="Username", bg_color="green", fg_color="blue")
        self.username_label.grid(row=1, column=0, sticky="e")
        self.username_label.grid_columnconfigure((0), weight=1)
        self.username_text = ctk.CTkTextbox(self, width= 80, height= 20, fg_color="blue", corner_radius= 0)
        self.username_text.grid(row=1, column=1, sticky= "ew", pady=10, padx=10)
        self.username_text.grid_columnconfigure((1), weight=10)
        #password
        self.password_label = ctk.CTkLabel(self, width=20, height=10, text="Password", bg_color="green", fg_color="blue")
        self.password_label.grid(row=2, column=0, sticky="e")
        self.password_text = ctk.CTkTextbox(self, width= 80, height= 20, fg_color="blue", corner_radius= 0)
        self.password_text.grid(row=2, column=1, sticky= "ew", pady=10, padx=10)
        #login button
        self.login_button = ctk.CTkButton(self, width= 20, height=10 , text="submit", command=self.login_submission)
        self.login_button.grid(row=3, column=0, sticky= "nsew", pady=10, padx=10, columnspan=2)
    def login_submission(self):
        print("Login counted")
        self.save_to_file()
    def save_to_file(self):
        with open('subscribed_members.csv', "w") as file:
            file_writer = csv.writer(file, delimiter=",", quotechar="|")
            file_writer.writerow(["good"])

if __name__ == "__main__":
    app = App()
    app.mainloop()