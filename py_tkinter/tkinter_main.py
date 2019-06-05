#! /usr/bin/python3

import tkinter as tk

def main():
    root = tk.Tk()
    l = tk.Label(root, width=20)
    l["text"] = "Lable"
    l.pack()
    root.mainloop()

if __name__ == "__main__":
    main()