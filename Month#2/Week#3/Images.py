import os
from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.geometry("300x400")
root.title("Meme Viewer")
root.iconbitmap("icon.ico")
i = 0

memes = []

for img in os.listdir("./Memes/"):
    memes.append(ImageTk.PhotoImage(Image.open(os.path.join("./Memes", img))))

label = Label(image=memes[0])
label.grid(row=0, column=0, columnspan=3)
status = Label(root, text="Image 1 of " + str(len(memes)),
               bd=1, relief=SUNKEN, anchor=E)


def previousphoto():
    global i, label, previous, nextbutton, status

    if i == 5:
        nextbutton.grid_forget()
        nextbutton = Button(root, text=">>", width=10, command=nextphoto)
        nextbutton.grid(row=1, column=2)
    if i != 0:
        i -= 1
        status.grid_forget()
        status = Label(root, text="Image " + str(i + 1) + " of " +
                       str(len(memes)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
        label.grid_forget()
        label = Label(image=memes[i])
        label.grid(row=0, column=0, columnspan=3)
    if i == 0:
        previous.grid_forget()
        previous = Button(root, text="<<", width=10,
                          command=previousphoto, state=DISABLED)
        previous.grid(row=1, column=0)


def nextphoto():
    global i, label, nextbutton, previous, status

    if i == 0:
        previous.grid_forget()
        previous = Button(root, text="<<", width=10, command=previousphoto)
        previous.grid(row=1, column=0)
    if i != 5:
        i += 1
        status.grid_forget()
        status = Label(root, text="Image " + str(i + 1) + " of " +
                       str(len(memes)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
        label.grid_forget()
        label = Label(image=memes[i])
        label.grid(row=0, column=0, columnspan=3)
    if i == 5:
        nextbutton.grid_forget()
        nextbutton = Button(root, text=">>", width=10,
                            command=previousphoto, state=DISABLED)
        nextbutton.grid(row=1, column=2)


previous = Button(root, text="<<", width=10,
                  command=previousphoto, state=DISABLED)
previous.grid(row=1, column=0)
nextbutton = Button(root, text=">>", width=10, command=nextphoto)
nextbutton.grid(row=1, column=2, pady=10)
quitter = Button(root, text="Exit", width=10, command=root.quit)
quitter.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
