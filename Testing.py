import csv
import customtkinter as ctk
import os
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class account_credentials():
    def __init__(self, username, password):
        #establish name and password of the account
        self.username = username
        self._password = password
    def get_profiles(self):
        #create a list for the progfiles to go to
        profile_list = []
        file = csv.reader(open('members_profiles.csv', "r"), delimiter=",")
        #make it so that it doesn't read the header row for the file
        next(file)
        #look at each profile
        for row in file:
            #Check to find the profiles of the person logged in
            if self.username == row[0] and self._password == row[1]:
                #read through each profile when you found the correct username and group
                for column in row[2:-5]:
                    #Only add when there are profiles and stop adding when it gets to the 5 profile
                    if column != "None":
                        profile_list.append(column)
        if profile_list == []:
            print("Empty")
        return profile_list

account = account_credentials("MrDunne", "Baulko11!!").get_profiles()
file = csv.reader(open('members_profiles.csv', "r"))
lines = list(file)
print(len(lines))
a_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a_list = "\n".join(str(a_list))
print(a_list)

class Login_screen(ctk.CTk):
    def __init__(self, *args):
        super().__init__()
        self.geometry("450x480")
        #create the UI and show it on screen
        self._build_ui()
        self.title("Login")
        #create username and password instances
        self._profile_page = None
        self.__secret = "Lolapoloo"
        self.viewable = self.__secret
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
        self.login_button = ctk.CTkButton(self, width= 20, height=10 , text="submit",  command=lambda: self.login_submission("h"))
        self.login_button.grid(row=3, column=0, sticky= "nsew", pady=10, padx=10, columnspan=2)
    def login_submission(self, another):
        #Get username that was typed in
        self.username = self.username_text.get("0.0", "end")
        #Get username that was typed in
        self.password = self.password_text.get("0.0", "end")
        print(f"{self.username}, {self.password}")
        if another == "b":
            print("okay now we're getting somewhere")
        else:
            print("reak")
        #Check if the login details are correct
        verification = self.verify_login(self.username.strip(), self.password.strip())
        if verification == True:
            if self._profile_page == None or not self._profile_page.winfo_exists():
                print("Good Job")
                #open up profile page when you log in, as long as it doesn't already exist
            else:
                print("Bad!")
    def verify_login(self, username, password):
        #read the file with member info
        file = csv.reader(open('subscribed_members.csv', "r"), delimiter=",")
        #make it so that it doesn't read the header row for the file
        next(file)
        for row in file:
            if username == row[0] and password == row[1]:
                #if the data is correct make it return true and also create an instance of the account in the code
                self.account = account_credentials(username, password)
                return True
        return False

print(Login_screen().viewable)
    
if __name__ == "__main__":
    app = Login_screen()
    app.mainloop()