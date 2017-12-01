from tkinter import *

window=Tk()

def kg_converter():
    grams=float(e2_value.get())*1000
    t1.insert(END,grams)

    pounds=float(e2_value.get())*2.20462
    t2.insert(END,pounds)

    ounces=float(e2_value.get())*35.274
    t3.insert(END,ounces)

e1=Label(window,text="Kg")
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=kg_converter)
b1.grid(row=0,column=2)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3)

t1=Text(window,height=1,width=10)
t1.grid(row=1,column=1)

t2=Text(window,height=1,width=10)
t2.grid(row=1,column=2)

t3=Text(window,height=1,width=10)
t3.grid(row=1,column=3)

window.mainloop()
