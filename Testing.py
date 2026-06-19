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

    def _build_ui(self):
        self.label = ctk.CTkLabel(self, text="Search", width=300, height=50, font=("Comic Sans MS", 24))
        self.label.grid(column=1, row=1, padx=10, pady=10)

        self.search=ctk.CTkEntry(self, placeholder_text="Search")
        self.search.grid(column=1, row=2, padx=10, pady=10)

        self.search.delete(0, ctk.END)

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("You're Watching")
        self.geometry("2560x1800")
        self.toplevel_window = None
        self.toplevel_window2 = None
        self.login_window = None
        #have variables of the window and the navigation frame, so that when the pages are created again (going through this class because it is used as the parent) everything an error for it not having a attribute isn't put up
        self.window = self
        self.navigation_frame = None
        self._build_ui()
    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.login_page = Login_module.Login_Page(self)
        self.login_page.grid(column=0, row=0, sticky="nsew")
        #self.homepage = Homepage(self)
        #self.homepage.grid(row=0, column=0, sticky="nsew")
class Homepage(ctk.CTkScrollableFrame):
        def __init__(self, parent, account, profile, restrictions):
            super().__init__(parent)
            self.toplevel_window = None
            self.toplevel_window2 = None
            self.login_window = None
            #have variables of the window and the navigation frame, so that when the pages are created again (going through this class because it is used as the parent) everything an error for it not having a attribute isn't put up
            self.window = parent.window
            self.navigation_frame = None
            self.account = account
            self.profile = profile
            self.restrictions = restrictions
            print(self.account)
            print(self.profile)
            print(self.restrictions)
            self._build_ui()
        def _build_ui(self):
            global x
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

            thingyb = []

            self.label = ctk.CTkLabel(self, text="You're Watching", fg_color="#325EE2", text_color="white", width=200, height=50, font=("Comic Sans MS", 24))
            self.label.grid(padx=0, pady=10, column=0, row=0, columnspan=2)

            self.btn = ctk.CTkButton(self, text="Search", command=self._opensearch, font=("Comic Sans MS", 14))
            self.btn.grid(column=3, row=1, columnspan=2)

            self.btn = ctk.CTkButton(self, text="Watchlist", command=self._openwatchlist, font=("Comic Sans MS", 14))
            self.btn.grid(column=6,row=1)

            y = 0
            mvs = []

            mvs.append(ctk.CTkImage(Image.open('luckystar.jpg'), size=(150,225)))
            mvs.append(ctk.CTkImage(Image.open('btr.jpg'), size=(150,225)))
            mvs.append(ctk.CTkImage(Image.open('ddlc.jpg'), size=(150,225)))
            mvs.append(ctk.CTkImage(Image.open('toradora.jpg'), size=(150,225)))
            mvs.append(ctk.CTkImage(Image.open('shikanokonokonokokoshitantan.jpg'), size=(150,225)))
            #mvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/toradora.jpg'), size=(150,225)))
            #mvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taiga.jpg'), size=(150,225)))
            #mvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(150,225)))
            #mvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(150,225)))
            #mvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(150,225)))

            mvname = []

            mvname.append("Lucky Star")
            mvname.append("Bocchi The Rock!")
            mvname.append("DDLC")
            mvname.append("Toradora")
            mvname.append("Shikanoko Nokonoko Koshitantan")
            #mvname.append("Toradora")
            #mvname.append("Toradora")
            #mvname.append("Toradora")
            #mvname.append("Toradora")
            #mvname.append("Toradora")

            thingyc = []

            #for i in range(x, 5+x):
            #    self.label = ctk.CTkLabel(self, text="", image=tvs[i])
            #    self.label.grid(padx=10, pady=20, column=i+1, row=2)
            #    self.btn = ctk.CTkButton(self, text=tvname[i])
            #    self.btn.grid(padx=10, pady=0, column=i+1, row=3)
            #    i+=1

            self.label = ctk.CTkLabel(self, text="Featured TV Shows", fg_color="#718CDD", width=150, height=30, font=("Comic Sans MS", 12))
            self.label.grid(padx=0, pady=10, column=0, row=1, columnspan=2)

            for i in range(x, 5+x):
                self.label=ctk.CTkLabel(self, text="", image=tvs[i])
                self.label.grid(padx=40, pady=10, column=i+1, row=2)
                thingyb.append(ctk.CTkButton(self, text=tvname[i]))
                thingyb[i]
                thingyb[i].grid(padx=10, pady=0, column=i+1, row=3)
                i+=1

            self.label = ctk.CTkLabel(self, text="Featured Movies", fg_color="#718CDD", width=150, height=30, font=("Comic Sans MS", 12))
            self.label.grid(padx=0, pady=10, column=0, row=4, columnspan=2)

            for i in range(x, 5+x):
                self.label=ctk.CTkLabel(self, text="", image=mvs[i])
                self.label.grid(padx=40, pady=10, column=i+1, row=6)
                thingyc.append(ctk.CTkButton(self, text=mvname[i]))
                thingyc[i]
                thingyc[i].grid(padx=10, pady=0, column=i+1, row=7)
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
if __name__ == "__main__":
    app = App()
    app.mainloop()
