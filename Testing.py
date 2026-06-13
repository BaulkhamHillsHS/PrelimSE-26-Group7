import customtkinter
import csv

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
print(account)