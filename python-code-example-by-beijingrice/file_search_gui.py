import os
from tkinter import *
import tkinter.filedialog
import sys
tqdm_enabled = False
try:
    from tqdm import tqdm
    tqdm_enabled = True
except ImportError:
    pass
tk = Tk()
tk.title("File Search")
L = Label(tk, text="File Search (GUI Version)")
L.grid(row=0, column=0)
E = Entry(tk)
E.grid(row=1, column=0)
L1 = Label(tk, text="Filename")
L1.grid(row=1, column=1)
T = Text(tk, width=60, height=30)
T.grid(row=2, column=0)


def main():
    T.delete("0.0", "end")
    search_at = tkinter.filedialog.askdirectory(title="Choose search start from")
    filename = E.get()
    text = ""
    found = False
    if not tqdm_enabled:
        for root, dir, file in os.walk(search_at):
            for each in file:
                if filename in each:
                    text = text + "Filename: %s" % (root + "/" + each) + "\n"
                    found = True
    if tqdm_enabled:
        for root, dir, file in tqdm(os.walk(search_at)):
            for each in file:
                if filename in each:
                    text = text + "Filename: %s" % (root + "/" + each) + "\n"
                    found = True
    if found:
        T.insert(INSERT, text)
    if not found:
        T.insert(INSERT, "No files found!")


def _exit():
    tk.destroy()
    sys.exit()


B = Button(tk, text="Start Search", command=main)
B.grid(row=3, column=0)
tk.protocol("WM_DELETE_WINDOW", _exit)
tk.mainloop()
