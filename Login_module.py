import customtkinter as ctk
import csv
import tkinter as tk
import Front_Page
import Testing
import os
import smtplib
from email.message import EmailMessage
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class Login_screen(ctk.CTkToplevel):
    def __init__(self, *args):
        super().__init__()
        self.geometry("450x480")
        #create the UI and show it on screen
        self._build_ui()
        self.title("Login")
        #have variables of the window and the navigation frame, so that when the pages are created again (going through this class because it is used as the parent) everything an error for it not having a attribute isn't put up
        self.window = self
        self.navigation_frame = None
    def _build_ui(self):
        #giving different weights to different columns
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=20)
        #Creating a row
        self.grid_rowconfigure((0), weight=10)
        self.login_page = Login_Page(self)
        self.login_page.grid(row=0, column=0, sticky="nsew", columnspan=2)
#A class for the login page
class Login_Page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self._profile_page = None
        self.window = parent
        #create ui
        self._build_ui()
    def _build_ui(self):
        #giving different weights to different columns
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=20)
        #giving different weights to different rows
        self.grid_rowconfigure((0,4), weight=1)
        self.grid_rowconfigure((1,2), weight=8)
        self.grid_rowconfigure((3), weight=2)
        #Login Label
        self.label = ctk.CTkLabel(self, width= 80, height= 20, text="Login", fg_color= "transparent", font=("Calibri", 24))
        self.label.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10, columnspan=2)
        #Username
        self.username_label = ctk.CTkLabel(self, width=20, height=10, text="Username", bg_color="green", fg_color="blue")
        self.username_label.grid(row=1, column=0, sticky="e")
        self.username_label.grid_columnconfigure((0), weight=1)
        self.username_text = ctk.CTkEntry(self, fg_color="blue", corner_radius= 0, height= 10, width= 400)
        self.username_text.grid(row=1, column=1, pady=10, padx=10, sticky="ew")
        #password
        self.password_label = ctk.CTkLabel(self, width=20, height=10, text="Password", bg_color="green", fg_color="blue")
        self.password_label.grid(row=2, column=0, sticky="e")
        self.password_text = ctk.CTkEntry(self, width= 80, height= 20, fg_color="blue", corner_radius= 0)
        self.password_text.grid(row=2, column=1, sticky= "ew", pady=10, padx=10)
        #login button
        self.login_button = ctk.CTkButton(self, width= 20, height=10 , text="submit",  command= self.login_submission)
        self.login_button.grid(row=3, column=0, sticky= "nsew", pady=10, padx=10, columnspan=2)
        #button if you forget your username and password
        self.forgotten_button = ctk.CTkButton(self, text="Press if you have forgotten your account details", command=self.send_credentials)
        self.forgotten_button.grid(row=4, column=0, sticky="ew", pady=10, padx=10, columnspan=2)
        #create instance of navigation frame and put it on the screen
        self.navigation_frame = Page_navigation_panel(self.window, "Login", None, self)
        self.navigation_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
    def login_submission(self):
        #Get username that was typed in
        self.username = self.username_text.get()
        #Get username that was typed in
        self.password = self.password_text.get()
        print(f"{self.username}, {self.password}")
        #Check if the login details are correct
        verification = self.verify_login(self.username.strip(), self.password.strip())
        if verification == True:
            if self._profile_page == None:
                #destroy everything in this frame
                for widget in self.winfo_children():
                    widget.destroy()
                print(self.winfo_children())
                #open up profile page when you log in, as long as it doesn't already exist
                self._profile_page = Profile_Page(self, self.account)
                self._profile_page.grid(row=0, column=0, sticky='nsew', columnspan=2, rowspan=5)
                
        else:
            #show warning if you don't put in a valid username/password
            tk.messagebox.showwarning("Invalid username or password", "There doesn't seem to be a user matched with these details")

    def verify_login(self, username, password):
        #read the file with member info
        file = csv.reader(open('subscribed_members.csv', "r"), delimiter=",")
        #make it so that it doesn't read the header row for the file
        next(file)
        for row in file:
            if username == row[0] and password == row[1]:
                #if the data is correct make it return true and also create an instance of the account in the code
                self.account = account_credentials(username, password, None)
                return True
        return False
    def send_credentials(self):
        #destroy everything in this frame
        for widget in self.winfo_children():
            widget.destroy()
        #Go to the Email_send page
        self.email_send = Email_Send(self)
        self.email_send.grid(row=0, column=0, sticky='nsew', columnspan=2, rowspan=5)

#A class for the profile page having it inherit from the login page to know what account to use
class Profile_Page(ctk.CTkFrame):
    def __init__(self, parent, account):
        super().__init__(parent)
        #Carry over the instance of the account_credential class
        self.account = account
        #get username and pass word from the account
        self.username = account.username
        self.password = account._password
        #also have it remember what window it is on (so that when it creates the navigation panel frame it knows what to put it on)
        self.window = parent.window
        #destroy old navigation panel if it exists
        try:
            parent.navigation_frame.destroy()
        except:
            pass
        #create a new navigation panel on the same window
        self.navigation_frame = Page_navigation_panel(self.window, "Profile", self.account, self)
        self._build_ui()
    def _build_ui(self):
        #set up rows and columns
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0,weight=3)
        self.columnconfigure(1, weight=5)
        #create a list of profiles from csv file
        self.profiles = self.account.profiles
        #create a title for this page
        self.profile_title_label = ctk.CTkLabel(self, text=f"{self.username}'s profiles", font=("Calibri", 24), fg_color="transparent")
        self.profile_title_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10, columnspan=2)
        #create a combobox with the profiles as options
        self.profile_box = ctk.CTkComboBox(self, values=self.profiles, state="readonly", command=self.describe_profile)
        #put the combobox in position
        self.profile_box.grid(row=1, column=0,)
        #Create a label to show the specifications of the profile and set details to be empty when no profile is chosen
        self.description = "No profile chosen yet"
        self.description_label = ctk.CTkLabel(self, text=self.description, fg_color="blue",width=150, height=100,corner_radius=10)
        #place the description down
        self.description_label.grid(row=1,column=1,sticky='ew', padx=20)
        #Button to choose profile
        self.submit_button = ctk.CTkButton(self, text="Choose profile", command=self.submit_profile)
        self.submit_button.grid(row=2, column=1)
        #Button to go to subscription page
        self.subscription_page_button = ctk.CTkButton(self, text="Go to subscription page", command=self.open_subscription)
        self.subscription_page_button.grid(row=2,column=0)
        #put in the navigation frame
        self.navigation_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
    def describe_profile(self, choice):
        #get the allowed content of the profile
        self.allowed_content = self.account.get_profile_description(choice)
        self.description = f"You have chosen profile: {choice} \n Allowed content up to: {self.allowed_content}"
        print(self.description)
        #remake the label to update this
        self.description_label = ctk.CTkLabel(self, text=self.description, fg_color="blue",width=150, height=100,corner_radius=10)
        #place the textbox down
        self.description_label.grid(row=1,column=1, sticky="ew", padx=20)
    def submit_profile(self):
        #check if a profile has been chosen
        if self.profile_box.get() == "":
            tk.messagebox.showwarning("Unchosen profile", "You have not chosen a profile yet")
        else:
            self.profile = self.profile_box.get()
            #get rid of the navigation panel as they go to the main page
            self.navigation_frame.destroy()
            #destroy everything in this frame
            for widget in self.winfo_children():
                widget.destroy()
            #create instance of the home page and pass through the account, profile and profile restrictions through
            self.homepage = Testing.Homepage(self.window, self.account, self.profile, self.allowed_content)
            #put it on screen
            self.homepage.grid(row=0,column=0, sticky="nsew")
            
    def open_subscription(self):
         #destroy everything in this frame
        for widget in self.winfo_children():
            widget.destroy()
        #open the subscription page frame and have it be the parent
        self.subscription_page = Subscription_Page(self, self.account)
        self.subscription_page.grid(row=0, column=0, columnspan=2, rowspan=3, sticky="nsew")
class Subscription_Page(ctk.CTkFrame):
    def __init__(self, parent, account):
        super().__init__(parent)
        #get the account from the parent
        self.account = account
        #get the subscription of the account
        self.subscription = self.account.subscription
        #again have it remember what window it is on (so that when it creates the navigation panel frame it knows what to put it on)
        self.window = parent.window
        #destroy old navigation panel if it exists
        try:
            parent.navigation_frame.destroy()
        except:
            pass
        #create a new navigation panel on the same window
        self.navigation_frame = Page_navigation_panel(self.window, "Subscription", self.account, self)
        self._build_ui()
    def _build_ui(self):
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0,weight=3)
        self.columnconfigure(1, weight=5)
        #create a title for the subscription page
        #create a title for this page
        self.profile_title_label = ctk.CTkLabel(self, text=f"Subscription Plans \nExisting plan: {self.subscription} tier", font=("Calibri", 24), fg_color="transparent")
        self.profile_title_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10, columnspan=2)
        #create a combobox with the subscription plans as options
        self.subscription_box = ctk.CTkComboBox(self, values=["Budget", "Basic", "Premium"], state="readonly", command=self.describe_subscription)
        #put the combobox in position
        self.subscription_box.grid(row=1, column=0)
        #Create a label to show the specifications of the profile and set details to be empty when no profile is chosen
        self.subscription_description = "Different plan not chosen yet"
        self.description_label = ctk.CTkLabel(self, text=self.subscription_description, fg_color="blue",width=150, height=100,corner_radius=10)
        #place the description down
        self.description_label.grid(row=1,column=1,sticky='ew', padx=20)
        #Button to choose subscription plan
        self.submit_button = ctk.CTkButton(self, text="Choose plan", command=self.submit_subscription)
        self.submit_button.grid(row=2, column=1, columnspan=2)
        #navigation frame
        self.navigation_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
    def describe_subscription(self, choice):
        #give different descriptions based off of subscription chosen
        print("okay")
        print(choice)
        if choice == "Budget":
            self.subscription_description = "Lowest streaming quality\nFor the You're streaming partakers"
        elif choice == "Basic":
            self.subscription_description = "An okay level of streaming quality and experiences\nFor the You're streaming initiated"
        elif choice == "Premium":
            self.subscription_description = "The highest level of streaming and video quality \nFor the You're streaming enjoyers"
        #update subscriiption description
        self.description_label = ctk.CTkLabel(self, text=self.subscription_description, fg_color="blue",width=150, height=100,corner_radius=10)
        self.description_label.grid(row=1,column=1, sticky="ew", padx=20)
    def submit_subscription(self):
        #get the choice of the subscription
        self.new_subscription = self.subscription_box.get()
        #only proceed if the choice is different to the existing plan
        if self.new_subscription == self.subscription:
            print("You already have that subscription")
        elif self.new_subscription == "Budget":
            print("nice")
        elif self.new_subscription == "Basic":
            print("nicer")
        elif self.new_subscription == "Premium":
            print("nicest")
        #go to Payment subscription page if a plan is chosen and it is different from original plan
        if self.new_subscription == "":
            tk.messagebox.showwarning("Unchosen Plan", "You have not chosen a plan yet")
        elif self.new_subscription == self.subscription:
            tk.messagebox.showwarning("Same Plan", "The plan you have chosen is the same as your existing one, you cannot swap to it")
        elif self.new_subscription != self.subscription:
            #destroy everything in this frame
            for widget in self.winfo_children():
                widget.destroy()
            self.payment_page = Payment_page(self)
            self.payment_page.grid(row=0, column=0, columnspan=2, rowspan=3, sticky="nsew")
class Payment_page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.account = parent.account
        self.subscription = parent.new_subscription
        self.username = self.account.username
        self.password = self.account._password
        #also get the viewable payment info of the user in this class
        self.payment_info = self.account._viewable_payment_info
        #again have it remember what window it is on (so that when it creates the navigation panel frame it knows what to put it on)
        self.window = parent.window
        #destroy old navigation panel
        parent.navigation_frame.destroy()
        #create a new navigation panel on the same window
        self.navigation_frame = Page_navigation_panel(self.window, "Payment", self.account, self)
        self._build_ui()
    def _build_ui(self):
        #create a column
        self.columnconfigure(0, weight=1)
        #create 4 rows
        self.grid_rowconfigure((0,2,3), weight=2)
        self.grid_rowconfigure((1,4), weight=1)
        #Label asking for you to pay to change subscription
        self.label = ctk.CTkLabel(self, width= 80, height= 20, text="Pay To Change Subscription", bg_color= "transparent", font=("Calibri", 24))
        self.label.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
        #Payment info Pin 
        self.bank_prompt_label = ctk.CTkLabel(self, width=20, height=10, text="Type in your Payment information", fg_color="transparent")
        self.bank_prompt_label.grid(row=1, column=0, sticky="ew", pady=10, padx=10)
        self.bank_details_text = ctk.CTkEntry(self, width= 80, height= 20, fg_color="blue", corner_radius= 0)
        self.bank_details_text.grid(row=2, sticky= "ew", pady=10, padx=10)
        #Payment button
        self.payment_button = ctk.CTkButton(self, width= 20, height=10 , text="Pay and Change Subscription", command=self.pay_subscription)
        self.payment_button.grid(row=3, column=0, sticky= "nsew", pady=10, padx=10)
        #navigation frame
        self.navigation_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
    def pay_subscription(self):
        print(f"Your was {self.account.subscription}")
        print(self.payment_info)
        #get the payment info that was typed in
        self.pin = self.bank_details_text.get()
        #also strip it
        self.pin = self.pin.strip()
        #make sure it is correct
        if self.pin == str(self.payment_info):
            #make sure that the subscription being paid for is different to what the account already has
            if self.account.subscription != self.subscription:
                #change the subscription and show it to the user
                self.account.change_subscription(self.subscription)
                print(f"Your subscription is now {self.account.subscription}")
                tk.messagebox.showinfo("Payment succeeded", f"Payment for the {self.account.subscription} plan has gone through")
            else:
                tk.messagebox.showwarning("Same Plan", "You have already paid for that subscription plan")
        elif self.pin == "":
            tk.messagebox.showwarning("Unfilled information", "You have not filled the bank credentials")
        else:
            #notify the user if they did not put the correct bank information 
            tk.messagebox.showwarning("Invalid Bank Information", "That is not your payment details")
#class for a frame that will go at the bottom of the screen allowing navigation to
class Page_navigation_panel(ctk.CTkFrame):
    def __init__(self, parent, page, account, old_frame):
        super().__init__(parent)
        #The pages correspond with what top frame calling the page_navigation which will change what buttons show up and what pages will which can be navigated to
        self.panel = page
        #Having so that it inherits the existing instance of the window opened so that the frame is put on the existing window
        self.window = parent
        #Having so that it inherits the account logged in so that it can pass it on when it makes a new instance of the old page it still gives the account details
        self.account = account
        #be able to call the old page so it can destroy it
        self.old_frame = old_frame
        self._build_ui()
    def _build_ui(self):
        #create 2 columns
        self.grid_columnconfigure((0,1), weight=1)
        #create 1 row
        self.grid_rowconfigure((0), weight=1)
        #Create buttons
        self.choose_buttons()
    def choose_buttons(self):
        if self.panel == "Login":
            #show no buttons if it is the login screen
            pass
        if self.panel == "Profile":
            #make a button to go back to the login page
            self.back_button1 = ctk.CTkButton(self, width= 20, height=10 , text="Go back to Login Page", command=self.back_login)
            self.back_button1.grid(row=1, column=0, sticky= "nsew", columnspan=2, pady=10, padx=10)
        elif self.panel == "Subscription":
            #make a button to go back to the login page
            self.back_button1 = ctk.CTkButton(self, width= 20, height=10 , text="Go back to Login Page", command=self.back_login)
            self.back_button1.grid(row=1, column=0, sticky= "nsew", pady=10, padx=10)
            #make a button to go back to the Profile page
            self.back_button2 = ctk.CTkButton(self, width= 20, height=10 , text="Go back to Profile Page", command=self.back_profile)
            self.back_button2.grid(row=1, column=1, sticky= "nsew", pady=10, padx=10)
        elif self.panel == "Payment":
            #make a button to go back to the login page
            self.back_button1 = ctk.CTkButton(self, width= 20, height=10 , text="Go back to Login Page", command=self.back_login)
            self.back_button1.grid(row=1, column=0, sticky= "nsew", pady=10, padx=10)
            #make a button to go back to the Subscription page
            self.back_button2 = ctk.CTkButton(self, width= 20, height=10 , text="Go back to Subscription Page", command=self.back_subscription)
            self.back_button2.grid(row=1, column=1, sticky= "nsew", pady=10, padx=10)
    def back_login(self):
        #creating a instance of the login_page but have it be so that it's parent is the carried over instance of the window, so when you put it on with grid it will be placed on the grind of the window and not within this frame
        self.login_page = Login_Page(self.window)
        self.login_page.grid(row=0, column=0, sticky="nsew", columnspan=2)
        #destroy the old frame when it is called
        self.get_rid()
    #function for going back to the profile page
    def back_profile(self):
        self.profile_page = Profile_Page(self.window, self.account)
        self.profile_page.grid(row=0, column=0, sticky="nsew", columnspan=2)
        #destroy the old frame when it is called
        self.get_rid()
    #function for going back to the subscription page
    def back_subscription(self):
        self.subscription_page = Subscription_Page(self.window, self.account)
        self.subscription_page.grid(row=0, column=0, sticky="nsew", columnspan=2)
        #destroy the old frame when it is called
        self.get_rid()
    def get_rid(self):
        print(self.old_frame.winfo_children())
         #destroy everything in the frame calling it
        for widget in self.old_frame.winfo_children():
            widget.destroy()
        print(self.old_frame.winfo_children())
class Email_Send(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.window = parent.window
        #destroy old navigation panel
        parent.navigation_frame.destroy()
        #create a new navigation panel on the same window, it use profile as both use the exact same button
        self.navigation_frame = Page_navigation_panel(self.window, "Profile", None, self)
        self._build_ui()
    def _build_ui(self):
        #create a column
        self.columnconfigure(0, weight=1)
        #create 4 rows
        self.grid_rowconfigure((0,2,3), weight=2)
        self.grid_rowconfigure((1,4), weight=1)
        #Label telling you how to get your credentials
        self.label = ctk.CTkLabel(self, width= 80, height= 20, text="Lost user credentials", bg_color= "transparent", font=("Calibri", 24))
        self.label.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
        #Entry box to put in email
        self.email_label = ctk.CTkLabel(self, width=20, height=10, text="Type in your Email address to be sent your username and password \n(through a popup)", fg_color="transparent")
        self.email_label.grid(row=1, column=0, sticky="ew", pady=10, padx=10)
        self.email_text = ctk.CTkEntry(self, width= 80, height= 20, fg_color="blue", corner_radius= 0)
        self.email_text.grid(row=2, sticky= "ew", pady=10, padx=10)
        #email button
        self.email_button = ctk.CTkButton(self, width= 20, height=10 , text="Find username and password", command=self.send_email)
        self.email_button.grid(row=3, column=0, sticky= "nsew", pady=10, padx=10)
        #navigation frame
        self.navigation_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
    def send_email(self):
        #get the email given
        self.email = self.email_text.get()
        #create an instance of the user account
        self.account = account_credentials(None, None, self.email)
        #send and warning if nothing was typed
        if self.email == "":
            tk.messagebox.showwarning("Unfilled email", "You have not filled in your email")
        else:
            #make sure the email is actually tied to an account
            if self.account.username and self.account._password != "None":
                tk.messagebox.showinfo("Found credentials", f"Your Username is {self.account.username}, your Password is {self.account._password}")

                #message = EmailMessage()
              #  message.set_content(f"Your account username is {self.account.username}, your password is {self.account._password}")
               # message['Subject'] = "Lost credentials"
               # message["From"] = "nathan.lay6@education.nsw.gov.au"
                #message['To'] = self.email
                #set up a SMTP connection 
            #message to show them if them if the email they put actually wasn't part of an account
            else:
                tk.messagebox.showwarning("Invalid email", "We are sorry but that email is not tied to an account")
class account_credentials():
    def __init__(self, username, password, email):
        #establish name and password of the account if it is given
        if username != None and password != None:
            self.username = username
            self._password = password
        #if name and password aren't given find account through email
        else:
            self._email = email
            self.username = self.get_username_and_password("username")
            self._password = self.get_username_and_password("password")
        #Try to establish variables for quick access from other classes of different attributes of the account if the credentials are good
        try:
            self.profiles = self.get_profiles()
            self._email = self.__get_profile_feature("email")
            self.subscription = self.__get_profile_feature("subscription")
            self.__payment_info = self.__get_profile_feature("payment")
            #make a variable so that the mangled payment info can be seen by other classes but not acessed (as in it only shows the payment info but doesn't allow you to change it internally)
            self._viewable_payment_info = self.__payment_info
        except:
            #don't do anything
            pass
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
    def __get_profile_feature(self, feature):
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
    def get_username_and_password(self, feature):
        #open file
        file = csv.reader(open('subscribed_members.csv', "r"), delimiter=",")
        #make it so that it doesn't read the header row for the file
        next(file)
        for row in file:
            #Find the row in the csv file of the user via their email
            if self._email == row[2]:
                #give back the attribute based on what was typed to get
                if feature == "username":
                    return row[0]
                elif feature == "password":
                    return row[1]
        #if nothing is found notify caller
        return "None"
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
                        print(f"Yes {column} {number}")
                        #get the specific content rating (which is always down the row from the profile)
                        allowed_content = row[number + 5]
                        return allowed_content
    def change_subscription(self, subscription):
        #open file with subscribed members
        file = csv.reader(open('subscribed_members.csv', "r"))
        #make lists for each row
        lines = list(file)
        #make a variable to hold the number the row which the account is in
        account_row = None
        for number, row in enumerate(lines):
            #find the specific user
            print(self.username)
            print(self._password)
            if self.username == row[0] and self._password == row[1]:
                #remember the account's row
                account_row = number
        #change the fourth item on that row because that is the subscription column, changing to the specified subscription
        lines[account_row][3] = subscription
        #write the newly edited file back row by row
        with open('subscribed_members.csv', "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            for line in lines:
                writer.writerow(line)
        #write the change to the account subscription invoice
        file = open(f"Subscription_invoice\\{self.username}.txt", "a")
        file.write(f"Changed to {subscription} plan"+"\n")
        file.close
        #update the subscription variable
        self.subscription = subscription