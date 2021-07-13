import tkinter as tk
from datetime import datetime as dt
from tkinter import *
import tkinter

trigger = False
selection = 0
hosts_temp = "hosts"
hosts_path = r"/private/etc/hosts"
redirect = "127.0.0.1"
website_list = []

master = tk.Tk()
master.title("Website Blocker")

# Create List
listBox = tkinter.Listbox(master)
listBox.pack()

# Create textbox
entry = tk.Entry(master)
entry.insert(0,"Paste URL")
entry.pack()

#add to list
def list_add():
    website_list.append(entry.get())
    print(website_list)
    listBox.insert(END, entry.get())
    entry.delete(0, END)
#remove items from list
def list_remove():
    if listBox.curselection() == ():
        pass
    else:
        listBox.delete(listBox.curselection())
        indexP = listBox.curselection()
        if indexP != ():
            website_list.remove(website_list[indexP])

def block():
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("non working hours")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    master.after(90000, block)

button_add = tk.Button(master, text="Add Website", command=list_add)
button_add.pack()

button_remove = tk.Button(master, text="Remove Website", command=list_remove)
button_remove.pack()

button_block = tk.Button(master, text="Block", command=block)
button_block.pack()

master.mainloop()
