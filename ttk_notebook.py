from tkinter import *
from tkinter import ttk

# Create the main Tkinter window
tktop = Tk()
tktop.title("Notebook Example")

# Add a label at the top
tabletop = Label(tktop, text="Abad Tak Yahi Jung Jaari Rahegi")
tabletop.pack()

# Create a Notebook widget
notebook = ttk.Notebook(tktop)

# Create two frames to add to the notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

# Add frames to the notebook with titles
notebook.add(frame1, text="Frame One")
notebook.add(frame2, text="Frame Two")
notebook.pack(expand=True, fill='both')

# Add a dummy button in Frame 1
dummy_button = Button(frame1, text="Dummy Button")
dummy_button.pack()

# Add a label in Frame 1
label = Label(frame1, text="Inzaar")
label.pack()

# Add a Quit button to the main window
button_quit = Button(tktop, text="Quit", command=tktop.quit)
button_quit.pack()

# Start the Tkinter event loop
tktop.mainloop()
