from tkinter import *

root=Tk()

def send():
    send="You : "+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=='hi'):
        text.insert(END,"\n"+"Bot : hello")
    elif(a.get()=='hello'):
        text.insert(END,"\n"+"Bot : hi")




text= Text(root,bg='white')
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
bsend=Button(root,text='Send',bg='green',width=20,command=send)
bsend.grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('Simple ChatBot')
root.mainloop()