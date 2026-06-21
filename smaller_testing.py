import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("test")
        self.geometry("500x500")
        self.build_ui()
        self.watch_list = None
        self.watch_history = None
    def build_ui(self):
        #I don't know how you will implement this to your movie and tv show classes but if each video/movie is an object you can pass on their name as self.video
        #self.video will then be passed into the self.watch and save buttons so that it can be added to the watch_list or watch history
        self.video = "Movie Name"
        #self.profile would be the profile accessing all of the home page, I think for your main app class you should put profile in the init so that from my login section I can pass the profile chosen when I call the front_page class
        self.profile = "test"
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2,3), weight=1)
        self.button = ctk.CTkButton(self, text="watch", command=lambda:self.watch(self.profile, self.video))
        self.button.grid(row=0,column=0)
        self.button1 = ctk.CTkButton(self, text="Save to watchlist", command=lambda:self.save(self.profile, self.video))
        self.button1.grid(row=1,column=0)
        self.button2 = ctk.CTkButton(self, text="Open watch_history", command=lambda: self.open_watch_history(self.profile))
        self.button2.grid(row=2,column=0)
        self.button3 = ctk.CTkButton(self, text="Open watch_list", command=lambda: self.open_watch_list(self.profile))
        self.button3.grid(row=3,column=0)
    def watch(self, profile, video):
        #having it as a f string would make it so that it just finds the text file based on their name, for the watch_history files it is formatted "name"_history.txt and for all watchlists it is just "name".txt but when you actually implement this you do watch_history//... or watch_list//... as they are in folders
        file = open(f"{profile}_history.txt", "a")
        #for your movie and tv show subclasses you can change it so that this function write "watched movie: " or "watched tv show episode: " instead
        file.write(f"Watched movie: {video}"+"\n")
        file.close
    def save(self, profile, video):
        #get the text 
        file = open(f"{profile}.txt", "r")
        self.videos = file.read()
        print(self.videos)
        #make sure it isn't in the watch list
        #I'm not to sure how to make it so that you can get rid of things from your watch_list, maybe have two separate buttons one for adding and one for getting rid of it from the watch_list
        #this is for checking if it is already in the watchlist if you do two buttons for adding and getting rid of then if they already have it in the watchlist only the getting rid of show button could work and if they don't have it then only the adding button could work
        if video in self.videos:
            print("its already in watch list")
        else:
            file = open(f"{self.profile}.txt", "a")
            file.write(f"{video}"+"\n")
        file.close
    
    def open_watch_list(self, profile):
        if self.watch_list == None or not self.watch_list.winfo_exists():
            self.watch_list = Watchlist(self, profile)
        else:
            self.watch_list.focus()
    def open_watch_history(self, profile):
        if self.watch_history == None or not self.watch_history.winfo_exists():
            self.watch_history = WatchHistory(self, profile)
        else:
            self.watch_history.focus()

class Watchlist(ctk.CTkToplevel):
    def __init__(self, parent, profile):
        super().__init__(parent)
        self.title("watch_list")
        self.geometry("300x300")
        self.profile = profile
        self.build_ui()
    def build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0), weight=1)

        #put in the frame with everything
        self.frame = Watchlist_frame(self, self.profile)
        self.frame.grid(row=0, column=0, sticky="nsew")
#I put everything in scrollable frames so that you can actually navigate everything
class Watchlist_frame(ctk.CTkScrollableFrame):
    def __init__(self, parent, profile):
        super().__init__(parent)
        self.profile = profile
        self.build_ui()
    def build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0), weight=1)
        self.rowconfigure((1), weight=11)
        #get watchlist from text file
        file = open(f"{self.profile}.txt", "r")
        self.watch_listed_shows = file.read()
        #scrollable frame so it is more useable

        #Title label
        self.title_label = ctk.CTkLabel(self, text="Watchlist",font=("Comic Sans MS", 20))
        self.title_label.grid(row=0, column=0)
        self.watchlist_text = ctk.CTkLabel(self, text=self.watch_listed_shows, font=("Comic Sans MS", 12))
        self.watchlist_text.grid(row=1, column=0, sticky="nsew")
class WatchHistory(ctk.CTkToplevel):
    def __init__(self, parent, profile):
        super().__init__(parent)
        self.title("watch history")
        self.geometry("300x300")
        self.profile = profile
        self.build_ui()
    def build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0), weight=1)
        #put in the frame
        self.watch_history_frame = Watch_history_frame(self, self.profile)
        self.watch_history_frame.grid(row=0, column=0, sticky="nsew")
class Watch_history_frame(ctk.CTkScrollableFrame):
    def __init__(self, parent, profile):
        super().__init__(parent)
        self.profile = profile
        self.build_ui()
    def build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0), weight=1)
        self.rowconfigure((1), weight=11)

        #get text from text file
        file = open(f"{self.profile}_history.txt", "r")
        self.shows_watched = file.read()
        
        #Title label
        self.title_label = ctk.CTkLabel(self, text="Watch History",font=("Comic Sans MS", 20))
        self.title_label.grid(row=0, column=0)
        self.watchlist_text = ctk.CTkLabel(self, text=self.shows_watched, font=("Comic Sans MS", 12))
        self.watchlist_text.grid(row=1, column=0, sticky="nsew")
if __name__ == "__main__":
    app = App()
    app.mainloop()
