import os
import tkinter as tk
import customtkinter as ctk
import Login_module
from PIL import Image

class Watchlist(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Watchlist")
        self.geometry("1280x900")
        self.label = ctk.CTkLabel(self, text="Watchlist", fg_color="#6D268B", width=150, height=25)
        self.label.grid(column=1, row=1, padx=10, pady=10)

class Search(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Search")
        self.geometry("640x450")
        self._build_ui()
        self.resizable(False,False)

    def _build_ui(self):
        self.label = ctk.CTkLabel(self, text="Search", width=300, height=50, font=("Comic Sans MS", 24))
        self.label.grid(column=1, row=1, padx=10, pady=10)

        self.searchentry=ctk.CTkEntry(self, placeholder_text="Search")
        self.searchentry.grid(column=1, row=2, padx=10, pady=10)

        self.searchbt=ctk.CTkButton(self, text="Search")
        self.searchbt.grid(column=1, row=3, pady=5)

        self.label=ctk.CTkLabel(self, text="")
        self.label.grid(column=1,row=4, pady=2)

        self.searchentry.delete(0, ctk.END)

        self.combo=ctk.CTkComboBox(self, values=["Comedy", "Horror", "Adventure", "Action", "Romance"])
        self.combo.grid(column=2,row=2, padx=10, pady=5)

        self.Rcheckbox=ctk.CTkCheckBox(self, text="R18+")
        self.Rcheckbox.grid(column=1,row=5, pady=5)

        self.MAcheckbox=ctk.CTkCheckBox(self, text="MA15+")
        self.MAcheckbox.grid(column=1,row=6, pady=5)

        self.Mcheckbox=ctk.CTkCheckBox(self, text="M")
        self.Mcheckbox.grid(column=1,row=7, pady=5)

        self.PGcheckbox=ctk.CTkCheckBox(self, text="PG")
        self.PGcheckbox.grid(column=1,row=8, pady=5)

        self.Gcheckbox=ctk.CTkCheckBox(self, text="G")
        self.Gcheckbox.grid(column=1,row=9, pady=5)

    def search():
        #for name in tvname:
        pass

class View(ctk.CTkToplevel): #when you click each show to watch it
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        title = str("")
        self.title(title)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("You're Watching")
        self.geometry("2560x1800")
        self.toplevel_window = None
        self.toplevel_window2 = None
        self.login_window = None
        self.login = Login_module.Login_screen()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=0, sticky="nsew")

        self._build_ui(self.scroll_frame)

    def _build_ui(self, target_frame):
        global x
        x = 0

        tvs = {
            "Lucky Star" : {"Image":ctk.CTkImage(Image.open("luckystar.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Bocchi the Rock!" : {"Image":ctk.CTkImage(Image.open("btr.jpg"), size=(150,225)),"Rating":"PG","Genre":"Comedy"},
            "Doki Doki Literature Club!" : {"Image":ctk.CTkImage(Image.open("ddlc.jpg"), size=(150,225)),"Rating":"M","Genre":"Horror"},
            "Toradora" : {"Image":ctk.CTkImage(Image.open("toradora.jpg"), size=(150,225)),"Rating":"M","Genre":"Romance"},
            "My Deer Friend Nokotan" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Azumanga Daioh" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Roshidere" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"PG","Genre":"Romance"},
            "K-On!" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Girls' Last Tour" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Adventure"},
            "Onimai" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"}
        }

        tvbuttons = []

        y = 0
        mvs = {
            "Lucky Star" : {"Image":ctk.CTkImage(Image.open("luckystar.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Bocchi the Rock!" : {"Image":ctk.CTkImage(Image.open("btr.jpg"), size=(150,225)),"Rating":"PG","Genre":"Comedy"},
            "Doki Doki Literature Club!" : {"Image":ctk.CTkImage(Image.open("ddlc.jpg"), size=(150,225)),"Rating":"M","Genre":"Horror"},
            "Toradora" : {"Image":ctk.CTkImage(Image.open("toradora.jpg"), size=(150,225)),"Rating":"M","Genre":"Romance"},
            "My Deer Friend Nokotan" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Azumanga Daioh" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Roshidere" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"PG","Genre":"Romance"},
            "K-On!" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"},
            "Girls' Last Tour" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Adventure"},
            "Onimai" : {"Image":ctk.CTkImage(Image.open("shikanokonokonokokoshitantan.jpg"), size=(150,225)),"Rating":"M","Genre":"Comedy"}
        }

        mvbuttons = []

        #for i in range(x, 5+x):
        #    self.label = ctk.CTkLabel(self, text="", image=tvs[i])
        #    self.label.grid(padx=10, pady=20, column=i+1, row=2)
        #    self.btn = ctk.CTkButton(self, text=tvname[i])
        #    self.btn.grid(padx=10, pady=0, column=i+1, row=3)
        #    i+=1

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
            self.label=ctk.CTkLabel(target_frame, text="", image=tvimages[i])
            self.label.grid(padx=40, pady=10, column=i+1, row=2)
            tvbuttons.append(ctk.CTkButton(target_frame, text=tvname[i]))
            tvbuttons[i]
            tvbuttons[i].grid(padx=10, pady=0, column=i+1, row=3)
            i+=1

        self.label = ctk.CTkLabel(target_frame, text="Featured Movies", fg_color="#718CDD", width=150, height=30, font=("Comic Sans MS", 12))
        self.label.grid(padx=0, pady=10, column=0, row=4, columnspan=2)

        mvname = list(mvs.keys())
        mvimages = [details["Image"] for details in tvs.values()]

        for i in range(x, 6+x):
            self.label=ctk.CTkLabel(target_frame, text="", image=mvimages[i])
            self.label.grid(padx=40, pady=10, column=i+1, row=6)
            mvbuttons.append(ctk.CTkButton(target_frame, text=mvname[i]))
            mvbuttons[i]
            mvbuttons[i].grid(padx=10, pady=0, column=i+1, row=7)
            i+=1


    def _openwatchlist(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Watchlist(self)
        else:
            self.toplevel_window.focus()

    def _opensearch(self):
        if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
            self.toplevel_window2 = Search(self)
        else:
            self.toplevel_window2.focus()

    def _openstream(self):
        if self.toplevel_window3 is None or not self.toplevel_window3.winfo_exists():
            self.toplevel_window3 = View(self)
            pass
        else:
            self.toplevel_window3.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
