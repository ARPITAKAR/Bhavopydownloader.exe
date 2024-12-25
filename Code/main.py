from datetime import datetime, timedelta
import os, zipfile, io, requests
from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, filedialog
import tkinter as tk
from PIL import ImageTk, Image

def importdata():
    folder = filedialog.askdirectory(title='Folder Location', initialdir='/')
    sdt = s_date.get()
    edt = e_date.get()
    sdate = datetime.strptime(sdt, '%d/%m/%y')
    edate = datetime.strptime(edt, '%d/%m/%y')
    tupdate = f'\nBhavCopy downloading from {sdate.date()} to {edate.date()}\n'
    msg.insert(tk.END, str(tupdate))
    delta = edate - sdate  # as timedelta
    frame1.update()
    tupdate = ""
    for i in range(delta.days + 1):
        date = sdate + timedelta(days=i)
        day = "%02d" % date.day
        month = date.strftime("%b").upper()
        year = date.year
        filename = f"cm{day}{month}{year}bhav.csv"
        file_path = f'{folder}/{filename}'
        if not os.path.exists(file_path):
            try:
                url = f'https://www1.nseindia.com/content/historic' \
                      f'al/EQUITIES/{year}/{month}/{filename}.zip'
                r = requests.get(url, stream=True)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(folder)
                tupdate = f'{file_path} File downloaded\n'
            except:
                # tupdate = f'{filename} Network Failure....................\n'
                pass
        else:
            tupdate = f'{file_path} File exist\n'
        msg.insert(tk.END, str(tupdate))
        frame1.update()
        msg.see(tk.END)
    msg.insert(tk.END, "Task Compleated...........")

win= Tk()
win.title("BhavCopy Downloader.....")
width = 650
height = 400
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
win.geometry(alignstr)
win.resizable(width=True, height=True)

stl = ttk.Style()
stl.configure('My.TButton', foreground='#000000',background='#cee2f7',activeforeground='black')
stl.configure('My.TFrame', background='#0b194f')

tab = ttk.Notebook(win)
frame1 = ttk.Frame(tab, style='My.TFrame')
frame1.pack(fill='both', expand=True)
frame2 = ttk.Frame(tab, style='My.TFrame')
frame2.pack(fill='both', expand=True)
tab.add(frame1, text='Download')
tab.add(frame2, text='About Me')
tab.pack(expand=True,fill='both')

sd=Label(frame1, anchor = "center", text = "Start Date", bg = "#cee2f7").place(x=10,y=10,width=80,height=25)
s_date = DateEntry(frame1, date_pattern='dd/mm/yy', justify='center', size = 20, background="magenta3", foreground="white", bd=2)
s_date.place(x=100,y=10,width=110,height=25)
ed=Label(frame1, anchor = "center", text = "End Date", bg = "#cee2f7").place(x=220,y=10,width=80,height=25)
e_date = DateEntry(frame1, date_pattern='dd/mm/yy', justify='center', size = 20, background="magenta3", foreground="white")
e_date.place(x=310,y=10,width=110,height=25)
tk.Button(frame1, text="Dwnload", width=15, command=importdata,  foreground='#000000',background='#cee2f7',activebackground="#6859ef",activeforeground="white").place(x=500,y=10,width=110,height=25)

txt = StringVar()
md = "Welcome..........."
msg = Text(frame1, bg="#69aef2",fg="#333333", font='Times 15 bold')
scrollbar = Scrollbar(msg)
msg.configure(yscrollcommand=scrollbar.set)
msg.insert(tk.END, "Welcome.........")
scrollbar.config(command=msg.yview,troughcolor="#8e8bf2")
msg.place(x=10, y=50, width=width-20, height=315)
scrollbar.place(x=width-20, y=0, height=315, anchor='ne',width=15)

abt = StringVar()
abttxt = "\nAbout Me:-\n   Subhajt Bhattacharya \n   Academically Embellished from IITB\n" \
         "   Custom Indecator Maker in TradingView\n   Software Developer in Python\n" \
         "   Also Working On Javascript Google Sheet\n\n\n\n" \
         "About BhavCopy Downloader:- \n   "\
         "BhavCopy Downloader is a FREE data downloader for Indian Stock\n   Exchanges" \
         " NSE. The data is directly downloaded from NSE servers."
Abtme = Label(frame2, bg="#69aef2",fg="#333333",anchor = "nw", justify = "left", textvariable=abt, font='Times 16 bold').place(x=10, y=10, width=width-20, height=height-45)
abt.set(abttxt)
img = Image.open("2.jpeg")
img = img.resize((180, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(frame2, image=img)
panel.image = img
panel.place(x=width-15, y=15, height=200, anchor='ne',width=180)
win.mainloop()

# pyinstaller --onefile -w --hiddenimport=babel.numbers .\test.py