from tkinter import *

root=Tk()

root.geometry("655x533")

f1= Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2= Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP, fill="x")


l=Label(f1,text="WAR is Not Done")
l.pack(pady=142)

l=Label(f2,text="Dream Die when you quit not when u fail",
         font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root.mainloop()