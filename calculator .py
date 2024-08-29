from tkinter import*
root = Tk()
root.geometry('300x380')
root.title('calculator by satyam')
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "c":
            scvalue.set(" ")
            screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue=StringVar()
scvalue.set(" ")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill= X,ipadx=8,pady=10,padx=10)
f= Frame(root,bg="light blue")
b= Button(f,text="9",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)


b= Button(f,text="8",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)


b= Button(f,text="7",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)
f.pack()


f= Frame(root,bg="light blue")
b= Button(f,text="6",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)


b= Button(f,text="5",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)



b= Button(f,text="4",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)
f.pack()


f= Frame(root,bg="light blue")
b= Button(f,text="3",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b= Button(f,text="2",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b= Button(f,text="1",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)
f.pack()

f= Frame(root,bg="light blue")
b= Button(f,text="+",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b= Button(f,text="=",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

b= Button(f,text="c",padx=0.2,pady=0.2,font="lucida 30 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT)

f.pack()

root.mainloop()
