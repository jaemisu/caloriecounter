from tkinter import *
import tkinter.messagebox
import os
#functions

def registerall():
    global test1
    test1 = 0
    if txtfld.get().isnumeric():
        test1 = test1 + 1
        tkinter.messagebox.showinfo("WARNING", '"Food Name" is a text only input')
    if txtfld2.get().isalpha():
        test1 = test1 + 1
        tkinter.messagebox.showinfo("WARNING", '"Calories" is a numerical only input')
    if txtfld3.get().isalpha():
        test1 = test1 + 1
        tkinter.messagebox.showinfo("WARNING", '"Time eaten" is a timecode only input')
    while test1 >= 1:
        break
    
    else:
        tx1 = '\nFood: ' + txtfld.get()
        tx2 = '\nCalories: ' + txtfld2.get()
        tx3 = '\nTime/Date: ' + txtfld3.get() + '\n'
        file = open('calories.txt','a+')
        file.write(tx1)
        file.write(tx2)
        file.write(tx3)
        file.close()
        os.system("start " + 'calories.txt')

#window setup
window = Tk()
window.title("Daily Caloric Intake Calendar")
window.configure(width=400, height=450)
window.configure(bg='gray15')

#center window
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

lbl=Label(window, text="Daily Caloric Intake Tracker", fg='orange', font=("Helvetica", 20), bg=('gray15'))
lbl.place(x=30, y=30)
lbl2=Label(window, text="By Jaemisu", fg='orange', font=("Helvetica", 12), bg=('gray15'))
lbl2.place(x=32, y=65)
lbl3=Label(window, text="_____________________________________", fg='orange', font=("Helvetica", 12), bg=('gray15'))
lbl3.place(x=32, y=95)

txtfld=Entry(window, text="Food Name", bd=2)
txtfld.place(x=35, y=155)
lbl4=Label(window, text="Name of Food", fg='orange', font=("Helvetica", 12), bg=('gray15'))
lbl4.place(x=32, y=125)

txtfld2=Entry(window, text="Calories", bd=2)
txtfld2.place(x=35, y=215)
lbl5=Label(window, text="Total Calories", fg='orange', font=("Helvetica", 12), bg=('gray15'))
lbl5.place(x=32, y=185)

txtfld3=Entry(window, text="Time Eaten", bd=2)
txtfld3.place(x=35, y=275)
lbl6=Label(window, text="HH:MM // MM/DD/YY", fg='orange', font=("Helvetica", 12), bg=('gray15'))
lbl6.place(x=32, y=245)

btn=Button(window, text="Enter", fg='black', font=("Helvetica", 20), bg=('gray'), command = registerall)
btn.place(x=30, y=350)
btn.configure(width=5, height=1)



window.mainloop()