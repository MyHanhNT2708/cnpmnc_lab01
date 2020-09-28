#Nguyễn Thị Mỹ Hạnh - 43.01.104.044

from tkinter import *
 
root=Tk()
root.geometry("450x250")
root.title("Welcome to My App")
root.grid()
 
 
txt = Entry(root,width=20)
txt.pack()
 
def clicked():
 
    res = "Welcome " + txt.get() + " to My App"
    lbl.configure(text= res)
 
btn = Button(root, text="Click Me",bg="light blue", fg="red", command=clicked)
btn.pack()

lbl = Label(root, text="Hello", font=("Arial Bold", 25))
lbl.pack()
 
root.mainloop()