import customtkinter as ctk
import csv
import os
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class Login_screen(ctk.CTkToplevel):
    def __init__(self, *args):
        super().__init__()
        self.geometry("450x480")
        #create the UI and show it on screen
        self._build_ui()
        self.title("Login")
        #create username and password instances
        self._profile_page = None
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
        self.login_button = ctk.CTkButton(self, width= 20, height=10 , text="submit",  command= self.login_submission)
        self.login_button.grid(row=3, column=0, sticky= "nsew", pady=10, padx=10, columnspan=2)
    def login_submission(self):
        #Get username that was typed in
        self.username = self.username_text.get("0.0", "end")
        #Get username that was typed in
        self.password = self.password_text.get("0.0", "end")
        print(f"{self.username}, {self.password}")
        #Check if the login details are correct
        verification = self.verify_login(self.username.strip(), self.password.strip())
        if verification == True:
            if self._profile_page == None or not self._profile_page.winfo_exists():
                print("Good Job")
                #open up profile page when you log in, as long as it doesn't already exist
                self._profile_page = Profile_Page(self)
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
#A class for the profile page having it inherit from the login page to know what account to use
class Profile_Page(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("450x480")
        #Take username and password found in login and get rid of white space
        self.username = parent.username.strip()
        self.password = parent.password.strip()
        #also carry over the instance of the account_credential class
        self.account = parent.account
        self.title(f"{self.username}'s profiles")
        self._build_ui()
    def _build_ui(self):
        #set up rows and columns
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0,weight=3)
        self.columnconfigure(1, weight=5)
        #create a list of profiles from csv file
        self.profiles = self.account.profiles
        #create a combobox with the profiles as options
        self.profile_box = ctk.CTkComboBox(self, values=self.profiles, command=self.describe_profile)
        #put the combobox in position
        self.profile_box.grid(row=0, column=0,)
        #Create a label to show the specifications of the profile and set details to be empty when no profile is chosen
        self.description = "No profile chosen yet"
        self.description_label = ctk.CTkLabel(self, text=self.description, fg_color="blue",width=150, height=100,corner_radius=10)
        #place the description down
        self.description_label.grid(row=0,column=1,sticky='ew', padx=20)
        #Button to choose profile
        self.submit_button = ctk.CTkButton(self, text="Choose profile", command=self._submit_profile)
        self.submit_button.grid(row=1, column=1, columnspan=2)
    def describe_profile(self, choice):
        #get the allowed content of the profile
        self.allowed_content = self.account.get_profile_description(choice)
        self.description = f"You have chosen profile: {choice} \n Allowed content up to: {self.allowed_content}"
        print(self.description)
        #remake the label to update this
        self.description_label = ctk.CTkLabel(self, text=self.description, fg_color="blue",width=150, height=100,corner_radius=10)
        #place the textbox down
        self.description_label.grid(row=0,column=1, sticky="ew", padx=20)
    def _submit_profile(self):
        print(f"You've chosen {self.profiles}")
class Subscription_page(ctk.CTkFrame):
    def __init__(self):
        super().__init__()
class account_credentials():
    def __init__(self, username, password):
        #establish name and password of the account
        self.username = username
        self._password = password
        #establish variables for quick access from other classes of different attributes of users
        self.profiles = self.get_profiles()
        self.email = self.get_profile_description("email")
        self.subscription = self.get_profile_description("subscription")
        self.payment_info = self.get_profile_description("payment")
    def get_profiles(self):
        #create a list for the profiles to go to
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
        return profile_list
    def get_profile_feature(self, feature):
        attribute = None
        file = csv.reader(open('subscribed_members.csv', "r"), delimiter=",")
        #make it so that it doesn't read the header row for the file
        next(file)
        for row in file:
            #Find the row in the csv file of the person logged in
            if self.username == row[0] and self._password == row[1]:
                #dependent on what feature was specified get it from the user, email is column 2, subscription is column 3 and payment info is column 4
                if feature == "email":
                #get the email which is in the second column
                    attribute = row[2]
                elif feature == "subscription":
                #get the subscription which is in the third column
                    attribute = row[3]
                elif feature == "payment":
                #get the subscription which is in the fourth column
                    attribute = row[4]
                return attribute
    def get_profile_description(self, profile):
        file = csv.reader(open('members_profiles.csv', "r"), delimiter=",")
        #make it so that it doesn't read the header row for the file
        next(file)
        for row in file:
            #find the specific user
            if self.username == row[0] and self._password == row[1]:
                for number, column in enumerate(row):
                    #find the specific profile chosen by the user
                    if profile == column:
                        #get the specific content rating (which is always down the row from the profile)
                        allowed_content = row[number + 5]
                        return allowed_content
