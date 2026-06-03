import os
import tkinter
import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):

    global tv

    def __init__(root, **kwargs):
        super().__init__(**kwargs)
        root.title("Yuri Watching")
        root.geometry("2560x1800")
        root._build_ui()




    def _build_ui(root):
        
        x = 0
        root._openwatchlist = None
        tvs = []

        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/stfu.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/kessokulastwinter.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigakfc.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/shikanokonokonokokoshitantan.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taiga.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taiga.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))
        tvs.append(ctk.CTkImage(Image.open('/Users/ryanlam/Desktop/i need this/taigashutup.jpg'), size=(200,300)))

        tvname = []

        tvname.append("Lucky Star")
        tvname.append("All of the Above")
        tvname.append("Toradora")
        tvname.append("Toradora")
        tvname.append("Shikanoko Nokonoko Koshitantan")
        tvname.append("Toradora")
        tvname.append("Toradora")
        tvname.append("Toradora")
        tvname.append("Toradora")
        tvname.append("Toradora")

        root.label = ctk.CTkLabel(root, text="You're Watching", fg_color="#325EE2", text_color="white", width=200, height=50, font=("Arial", 24))
        root.label.grid(padx=30, pady=20, column=0, row=0, columnspan=2)

        root.label = ctk.CTkLabel(root, text="Front Page TV Shows", fg_color="#718CDD", width=150, height=25)
        root.label.grid(padx=30, pady=0, column=0, row=1, columnspan=2)

        root.btn = ctk.CTkButton(root, text="Watchlist", command=root._openwatchlist)
        root.btn.grid(column=6,row=1)


        for i in range(x, 5+x):
            root.label = ctk.CTkLabel(root, text="", image=tvs[i])
            root.label.grid(padx=10, pady=20, column=i+1, row=2)
            root.btn = ctk.CTkButton(root, text=tvname[i], command="")
            root.btn.grid(padx=10, pady=0, column=i+1, row=3)
            i+=1

    def _openwatchlist(root):
        if root._openwatchlist is None or not root._openwatchlist.winfo_exists():
            root._openwatchlist = Watchlist(root)
        else:
            root._openwatchlist.focus()

class Watchlist(ctk.CTkToplevel):
    def __init__(root, **kwargs):
        super().__init__(**kwargs)
        root.title("Watchlist")
        root.geometry("2560,1800")
        root.label = ctk.CTkLabel(root, "Watchlist")

if __name__ == "__main__":
    app = App()
    app.mainloop()
