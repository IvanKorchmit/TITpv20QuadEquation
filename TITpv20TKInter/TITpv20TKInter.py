from tkinter import *
n=0
def vajutamine(event):
    global n
    n+=1
    nupp.config(text="Vajutatud: "+str(n))

aken=Tk()
aken.title("Grafi4eskyy Interface")
aken.iconbitmap()
aken.iconbitmap('caco.ico')
aken.geometry('400x600')
nupp=Button(aken,text="Vajuta \nsiia",height=4,width=15,bg="blue",fg="green", font="Arial 36")   #.pack(side=TOP) command=vajutamine()
nupp.pack(side=TOP)     # grid(), place()
nupp.bind('<Button-3>',vajutamine)
aken.mainloop() 