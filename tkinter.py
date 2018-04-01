from tkinter import *
## import everything from tkinter
root = Tk()
## initialize tkinter

label1 = Label(root,text="Label 1")

label1.grid(row=0,column=0)

entrySpace = Entry(root)
entrySpace.grid(row=0,column=1)

root.mainloop()
## initialize Tk window until user closes window


#Button1 = Button(None,text = "Click Me!",fg="Blue", bg="Yellow")
#Button1.pack()
#Button2 = Button(None,text = "Hello!",fg="Red")
#Button2.pack(fill=X)
#Button3 = Button(None,text = "You There!",fg="Green")
#Button3.pack(side=RIGHT, fill=Y)
#Button4 = Button(None,text = "Yes!",fg="Orange")
#Button4.pack()
## Button(Layout,Text,Text Color)

#label1 = Label(root,text="Label 1")
#label2 = Label(root,text="Label 2")
#label3 = Label(root,text="Label 3")
#label1.grid(row=0,column=0)
#label2.grid(row=0,column=1)
#label3.grid(row=1,column=0)
