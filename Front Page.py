import os
import tkinter as tk
import customtkinter as ctk
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
        self.geometry("1280x900")
        self.label = ctk.CTkLabel(self, text="Search", fg_color="#6D268B", width=300, height=50, font=("Comic Sans MS", 24))
        self.label.grid(column=1, row=1, padx=10, pady=10)

class App(ctk.CTk):

    global tv

    def __init__(self):
        super().__init__()
        self.title("Yuri Watching")
        self.geometry("2560x1800")
        self.toplevel_window = None
        self.toplevel_window2 = None
        self._build_ui()

    def _build_ui(self):
        
        x = 0
        tvs = []

        tvs.append(ctk.CTkImage(Image.open('luckystar.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('btr.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('ddlc.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('toradora.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('shikanokonokonokokoshitantan.jpg'), size=(200,300)))
        #tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taiga.jpg'), size=(200,300)))
        #tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taiga.jpg'), size=(200,300)))
        #tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))
        #tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))
        #tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))

        tvname = []

        tvname.append("Lucky Star")
        tvname.append("Bocchi The Rock!")
        tvname.append("DDLC")
        tvname.append("Toradora")
        tvname.append("Shikanoko Nokonoko Koshitantan")
        #tvname.append("Toradora")
        #tvname.append("Toradora")
        #tvname.append("Toradora")
        #tvname.append("Toradora")
        #tvname.append("Toradora")

        self.label = ctk.CTkLabel(self, text="You're Watching", fg_color="#325EE2", text_color="white", width=200, height=50, font=("Comic Sans MS", 24))
        self.label.grid(padx=0, pady=0, column=0, row=0, columnspan=2)

        self.label = ctk.CTkLabel(self, text="Front Page TV Shows", fg_color="#718CDD", width=150, height=25, font=("Comic Sans MS", 12))
        self.label.grid(padx=0, pady=0, column=0, row=1, columnspan=2)

        self.btn = ctk.CTkButton(self, text="Watchlist", command=self._openwatchlist, font=("Comic Sans MS", 14))
        self.btn.grid(column=6,row=1)

        self.btn = ctk.CTkButton(self, text="Search", command=self._opensearch)
        self.btn.grid(column=3, row=1, columnspan=2)

        thingyb = []

        #for i in range(x, 5+x):
        #    self.label = ctk.CTkLabel(self, text="", image=tvs[i])
        #    self.label.grid(padx=10, pady=20, column=i+1, row=2)
        #    self.btn = ctk.CTkButton(self, text=tvname[i])
        #    self.btn.grid(padx=10, pady=0, column=i+1, row=3)
        #    i+=1

        for i in range(x, 6+x):
            self.label=ctk.CTkLabel(self, text="", image=tvs[i])
            self.label.grid(padx=10, pady=20, column=i+1, row=2)
            thingyb.append(ctk.CTkButton(self, text=tvname[i]))
            self.btn.grid(padx=10, pady=0, column=i+1, row=3)
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





# if __name__ == "__main__":
app = App()
app.mainloop()
