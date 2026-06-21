import os
import tkinter as tk
import customtkinter as ctk
import Login_module
from PIL import Image

def get_profile_restriction(username, profile_index):
    try:
        with open("members_profiles.csv", "r") as file:
            header = [h.strip() for h in file.readline().split(",")]
            
            target_column_name = f"restrict{profile_index}"
            restrict_col_idx = header.index(target_column_name)

            for line in file:
                row = [item.strip() for item in line.strip().split(",")]
                if row[0] == username:
                    return row[restrict_col_idx]
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return "None"




RATINGS = {
"G":2,
"PG":2,
"M":3,
"MA15":4,
"MA15+":4,
"R18":5,
"R18+":5,
"None":5
}






class Watchlist(ctk.CTkToplevel):
    def __init__(self, master, tv_data, mv_data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Watchlist")
        self.geometry("1280x900")
        self.label = ctk.CTkLabel(self, text="Watchlist", fg_color="#6D268B", width=150, height=25)
        self.label.grid(column=1, row=1, padx=10, pady=10)

        self.tv_data = tv_data
        self.mv_data = mv_data

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=1200, height=750)
        self.scroll_frame.grid(column=1, row=2, columnspan=5, padx=40, pady=20, sticky="nsew")
        
        self.load_watchlist()

    def load_watchlist(self):
        try:
            profilename = getattr(self.master, "active_profile_name", "DefaultProfile")
            filename = f"watch_lists/{profilename}.txt"

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        title = line.strip()
                        if title:
                            catalog = {**self.tv_data, **self.mv_data}
                            showinfo = catalog.get(title, {"Genre": "Unknown", "Rating": "G"})

                            viewbtn = ctk.CTkButton(self.scroll_frame, text=f"> {title}", font=("Comic Sans MS", 14), anchor="w", fg_color="#325EE2", command=lambda n=title, d=showinfo: self.master.openstream(n,d))
                            viewbtn.pack(pady=5,padx=20, fill="x")
            else:
                empty = ctk.CTkLabel(self.scroll_frame, text="Add some shows to your watchlist!", font=("Comic Sans MS", 16))
                empty.pack(pady=50)
        except Exception as e:
            print(f"Watchlist Error {e}")








class Search(ctk.CTkToplevel):
    def __init__(self, master, tv_data, mv_data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Search")
        self.geometry("640x450")
        self.tv_data = tv_data
        self.mv_data = mv_data
        self._build_ui()
        self.resizable(False,False)

    def _build_ui(self):
        

        user_restrict = getattr(self.master, "current_restrict", "M")
        user_level = RATINGS.get(user_restrict, 5)

        self.disabled_ratings = []
        for rating_string, level_num in RATINGS.items():
            if level_num > user_level:
                self.disabled_ratings.append(rating_string)


        self.label = ctk.CTkLabel(self, text="Search", width=300, height=50, font=("Comic Sans MS", 24))
        self.label.grid(column=1, row=1, padx=10, pady=10)

        self.searchentry=ctk.CTkEntry(self, placeholder_text="Search")
        self.searchentry.grid(column=1, row=2, padx=10, pady=10)

        self.searchbt=ctk.CTkButton(self, text="Search", command=self.search)
        self.searchbt.grid(column=1, row=3, pady=5)

        self.label=ctk.CTkLabel(self, text="")
        self.label.grid(column=1,row=4, pady=2)

        self.searchentry.delete(0, ctk.END)

        self.combo=ctk.CTkComboBox(self, values=["All", "Comedy", "Horror", "Adventure", "Action", "Romance"])
        self.combo.grid(column=2,row=2, padx=10, pady=5)

        if "R18+" in self.disabled_ratings or "R18" in self.disabled_ratings:
            r_state = "disabled"
        else:
            "normal"
        self.Rcheckbox = ctk.CTkCheckBox(self, text="R18+", state=r_state)
        self.Rcheckbox.grid(column=1, row=5, pady=5)

        ma_state = "disabled" if "MA15+" in self.disabled_ratings or "MA15" in self.disabled_ratings else "normal"
        self.MAcheckbox = ctk.CTkCheckBox(self, text="MA15+", state=ma_state)
        self.MAcheckbox.grid(column=1, row=6, pady=5)

        m_state = "disabled" if "M" in self.disabled_ratings else "normal"
        self.Mcheckbox = ctk.CTkCheckBox(self, text="M", state=m_state)
        self.Mcheckbox.grid(column=1, row=7, pady=5)

        self.PGcheckbox = ctk.CTkCheckBox(self, text="PG")
        self.PGcheckbox.grid(column=1, row=8, pady=5)

        self.Gcheckbox = ctk.CTkCheckBox(self, text="G")
        self.Gcheckbox.grid(column=1, row=9, pady=5)

    def search(self):
        query = self.searchentry.get().lower()
        selected_genre = self.combo.get()



        # SEARCH FOR RATING
        allowed = []
        if self.Rcheckbox.get() == 1: allowed.append("R18+")
        if self.MAcheckbox.get() == 1: allowed.append("MA15+")
        if self.Mcheckbox.get() == 1: allowed.append("M")
        if self.PGcheckbox.get() == 1: allowed.append("PG")
        if self.Gcheckbox.get() == 1: allowed.append("G")

        if not allowed:
            allowed = ["R18+", "MA15+", "M", "PG", "G"]

        all_media = {**self.tv_data, **self.mv_data}
        results = []

        for title, details in all_media.items():
            show_rating = details.get("Rating", "G")
            show_genre = details.get("Genre", "Unknown")

            genrematch = (selected_genre == "All" or show_genre == selected_genre)
            
            if query in title.lower() and show_rating in allowed and genrematch:
                if title in self.mv_data:
                    results.append([title, "Movie"])
                else:
                    results.append([title, "TV"])
                
        print(f"Results: {results}")
        full_data = {**self.tv_data, **self.mv_data}
        self.master.open_results(results, full_data)






class Results(ctk.CTkToplevel):
    def __init__(self, master, search_results, media_data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Search Results")
        self.geometry("500x600")
        
        self.title_lbl = ctk.CTkLabel(self, text="Matching Results", font=("Comic Sans MS", 18, "bold"))
        self.title_lbl.pack(pady=10)
        
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=440, height=480)
        self.scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        if search_results:
            for item in search_results:
                show_title = item[0]
                media_type = item[1]

                show_info = media_data.get(show_title, {})

                colour = "#6D268B" if media_type == "Movie" else "#325EE2"

                btn = ctk.CTkButton(self.scroll_frame, text=f"> {show_title}", font=("Comic Sans MS", 14), anchor="w", fg_color=colour, command=lambda n=show_title, d=show_info: self.master.openstream(n, d)
                )
                btn.pack(pady=5, padx=10, fill="x")
        else:
            lbl = ctk.CTkLabel(self.scroll_frame, text="No results", font=("Comic Sans MS", 14))
            lbl.pack(pady=20)






class View(ctk.CTkToplevel): #when you click each show to watch it
    def __init__(self, master, name, info, *args, **kwargs):
        super().__init__(master,*args,**kwargs)
        global profile_for_watch_history
        self.name = name
        self.info = info
        self.title(self.name)
        self.geometry("1280x800")
        self.resizable(False,False)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.save_watch_history()
        self._build_ui()

    def _build_ui(self):
        self.player_frame = ctk.CTkFrame(self, fg_color="black", corner_radius=0)
        self.player_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.player_frame.grid_rowconfigure(0, weight=1)
        self.player_frame.grid_columnconfigure(0, weight=1)

        if "StreamImage" in self.info:
            self.screen_canvas = ctk.CTkLabel(self.player_frame, text="", image=self.info["StreamImage"])
            self.screen_canvas.grid(row=0, column=0, sticky="nsew")
        else:
            self.screen_canvas = ctk.CTkLabel(self.player_frame, text="> Stream Starting", text_color="white", font=("Comic Sans MS", 18))
            self.screen_canvas.grid(row=0, column=0)

        self.sidebar = ctk.CTkFrame(self, fg_color="#2b2b2b", width=320, corner_radius=8)
        self.sidebar.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.sidebar.pack_propagate(False)

        self.side_title = ctk.CTkLabel(self.sidebar, text=self.name, text_color="white", font=("Comic Sans MS", 20, "bold"), wraplength=280)
        self.side_title.pack(pady=20, padx=15, anchor="w")

        meta_string = f"Genre: {self.info.get('Genre', 'Unknown')}\nRating: {self.info.get('Rating', 'G')}"
        self.side_meta = ctk.CTkLabel(self.sidebar, text=meta_string, text_color="#718CDD", font=("Comic Sans MS", 13), justify="left")
        self.side_meta.pack(pady=5, padx=15, anchor="w")

        self.side_desc = ctk.CTkLabel(self.sidebar, text=self.info.get("Description", "No description written yet."), text_color="#cccccc", font=("Comic Sans MS", 13), wraplength=280, justify="left"
        )
        self.side_desc.pack(pady=20, padx=15, anchor="w")

        self.add_watchlist_btn = ctk.CTkButton(self.sidebar, text="+ Add to Watchlist", fg_color="#6D268B", font=("Comic Sans MS", 13), command=self.save_watchlist)
        self.add_watchlist_btn.pack(side="bottom", fill="x", padx=15, pady=20)

    

    def save_watchlist(self):
        try:
            root = self.master
            profilename = getattr(root, "active_profile_name", "DefaultProfile")

            filename = f"watch_lists/{profilename}.txt"
            title = self.name

            with open(filename, "a") as file:
                file.write(f"{title}\n")
            
            print(f"Successful, '{title}', {filename}")
            self.add_watchlist_btn.configure(text="Successfully Added", fg_color="#1AA956", state="disabled")
        except Exception as e:
            print(f"Error - saving watchlist: {e}")
    def save_watch_history(self):
        filename = f"watch_history/{profile_for_watch_history}_history.txt"
        title = self.name
        with open(filename, "a") as file:
                file.write(f"Watched: {title}\n")







class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("You're Watching")
        self.geometry("2560x1800")
        self.toplevel_window = None
        self.toplevel_window2 = None
        self.login_window = None
        self.results_window = None
        self.toplevel_window3 = None
        self.withdraw()
        self.login = Login_module.Login_screen(self)

        self.current_username = "MrDunne"
        self.active_profile_index = 2

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=0, sticky="nsew")

        self._build_ui(self.scroll_frame)

    def _build_ui(self, target_frame):

        global x, Arestriction
        x = 0















        tvs = { #TV Shows
            "Lucky Star" : {
                "Image":ctk.CTkImage(Image.open("luckystar.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Comedy",
                "Description":"Having fun at school, doing homework together, cooking and eating, playing video games, watching anime. All these little things make up the daily life of anime and chocolate lover Izumi Konata and her friends.",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Bocchi the Rock!" : {
                "Image":ctk.CTkImage(Image.open("btr.jpg"), size=(150,225)),
                "Rating":"PG",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Doki Doki Literature Club!" : {
                "Image":ctk.CTkImage(Image.open("ddlc.jpg"), size=(150,225)),
                "Rating":"MA15+",
                "Genre":"Horror",
                "Description":"Just Monika.",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Toradora" : {
                "Image":ctk.CTkImage(Image.open("toradora.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Romance",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "My Deer Friend Nokotan" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Azumanga Daioh" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Roshidere" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"PG",
                "Genre":"Romance",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "K-On!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Girls' Last Tour" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Adventure",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Onimai" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "Nichijou" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "K-On!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "K-On!!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "K-On!!!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "K-On!!!!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                }
        }

        tvbuttons = []

        y = 0












        mvs = { #Movies
            "!Lucky Star" : {
                "Image":ctk.CTkImage(Image.open("luckystar.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Bocchi the Rock!" : {
                "Image":ctk.CTkImage(Image.open("btr.jpg"), size=(150,225)),
                "Rating":"PG",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Doki Doki Literature Club!" : {
                "Image":ctk.CTkImage(Image.open("ddlc.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Horror",
                "Description":"Just Monika.",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Toradora" : {
                "Image":ctk.CTkImage(Image.open("toradora.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Romance",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!My Deer Friend Nokotan" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Azumanga Daioh" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Roshidere" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"PG",
                "Genre":"Romance",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!K-On!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Girls' Last Tour" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Adventure",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Onimai" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"M",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!Nichijou" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!K-On!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!K-On!!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!K-On!!!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                },
            "!K-On!!!!!" : {
                "Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),
                "Rating":"G",
                "Genre":"Comedy",
                "Description":"Placeholder",
                "StreamImage":ctk.CTkImage(Image.open("ddlc.jpg"), size=(800,450))
                }
        }













        current_restrict = get_profile_restriction(self.current_username, int(self.active_profile_index)-1)

        tvs = self.filterM(dict(tvs), current_restrict)
        mvs = self.filterM(dict(mvs), current_restrict)

        tvname = list(tvs.keys())
        tvimages = [details["Image"] for details in tvs.values()]

        mvbuttons = []

        self.label = ctk.CTkLabel(target_frame, text="You're Watching", fg_color="#325EE2", text_color="white", width=200, height=50, font=("Comic Sans MS", 24))
        self.label.grid(padx=0, pady=10, column=0, row=0, columnspan=2)

        self.btn = ctk.CTkButton(target_frame, text="Search", command=self._opensearch, font=("Comic Sans MS", 14))
        self.btn.grid(column=3, row=1, columnspan=2)

        self.btn = ctk.CTkButton(target_frame, text="Watchlist", command=self._openwatchlist, font=("Comic Sans MS", 14))
        self.btn.grid(column=6,row=1)

        self.label = ctk.CTkLabel(target_frame, text="Featured TV Shows", fg_color="#718CDD", width=150, height=30, font=("Comic Sans MS", 12))
        self.label.grid(padx=0, pady=10, column=0, row=1, columnspan=2)

        tvname = list(tvs.keys())
        tvimages = [details["Image"] for details in tvs.values()]
        
        for i in range(x, 6+x):
            self.label = ctk.CTkLabel(target_frame, text="", image=tvimages[i])
            self.label.grid(padx=40, pady=10, column=i+1, row=2)
            
            show_name = tvname[i]
            show_data = tvs[show_name]
            
            tvbuttons.append(ctk.CTkButton(target_frame, text=show_name, command=lambda n=show_name, d=show_data: self.winfo_toplevel().openstream(n, d)))
            tvbuttons[i].grid(padx=10, pady=0, column=i+1, row=3)

        self.label = ctk.CTkLabel(target_frame, text="Featured Movies", fg_color="#718CDD", width=150, height=30, font=("Comic Sans MS", 12))
        self.label.grid(padx=0, pady=10, column=0, row=4, columnspan=2)

        mvname = list(mvs.keys())
        mvimages = [details["Image"] for details in tvs.values()]

        for i in range(x, 6+x):
            self.label=ctk.CTkLabel(target_frame, text="", image=mvimages[i])
            self.label.grid(padx=40, pady=10, column=i+1, row=6)
            movie_name = mvname[i]
            movie_data = mvs[movie_name]
            
            mvbuttons.append(ctk.CTkButton(target_frame, text=movie_name, command=lambda n=movie_name, d=movie_data: self.openstream(n, d)))
            mvbuttons[i]
            mvbuttons[i].grid(padx=10, pady=0, column=i+1, row=7)
            i+=1

        self.all_tvs = tvs
        self.all_mvs = mvs

    def _openwatchlist(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Watchlist(self, tv_data=self.all_tvs, mv_data=self.all_mvs)
        else:
            self.toplevel_window.focus()

    def _opensearch(self):
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_window2 = Search(self, tv_data=self.all_tvs, mv_data=self.all_mvs)
        else:
            self.toplevel_window2.focus()

    def open_results(self, results, full_data):
        if self.results_window is None or not self.results_window.winfo_exists():
            self.results_window = Results(self, search_results=results, media_data=full_data)
        else:
            self.results_window.destroy()
            self.results_window = Results(self, search_results=results, media_data=full_data)

    def openstream(self, name, info):
        if self.toplevel_window3 is None or not self.toplevel_window3.winfo_exists():
            self.toplevel_window3 = View(self, name=name, info=info)
        else:
            self.toplevel_window3.destroy()
            self.toplevel_window3 = View(self, name=name, info=info)
        self.toplevel_window3.focus()

    def filterM(self, raw_media, max_rating):
        max_level = RATINGS.get(max_rating, 5)
        filteredD = {}

        for name, details in raw_media.items():
            show_level = RATINGS.get(details["Rating"],1)
            if show_level <= max_level:
                filteredD[name] = details

        return filteredD
    
    def dologin(self, authu, sprofileidx, profile_name): # for login module to transfer over to here
        self.current_username = authu
        self.active_profile_index = sprofileidx
        self.active_profile_name = profile_name
        global profile_for_watch_history
        profile_for_watch_history = profile_name

        print(self.active_profile_name)
        
        global Arestriction
        Arestriction = get_profile_restriction(self.current_username,self.active_profile_index)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=0, sticky="nsew")

        self._build_ui(self.scroll_frame)
        self.deiconify()





if __name__ == "__main__":
    app = App()
    app.mainloop()
