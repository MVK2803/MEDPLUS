def mainprogram():
    master.destroy()
    import tkinter
    root=tkinter.Tk()
    root.title("WELCOME")
    def ShowChoice():
        num=u.get()
        root.destroy()
        if num==0:
            import CUSTOMER
        elif num==1:
            import SELLER
        else:
            import sys;sys.exit()
    u = tkinter.IntVar()
    u.set(0)  
    users = [("I AM A CUSTOMER",1),("I AM A SELLER",2)]
    tkinter.Label(root, 
             text="""Choose your option""").grid(row=0)
    c1=0
    for val, user in enumerate(users):
        c1+=1
        tkinter.Radiobutton(root, 
                      text=user[0],
                       
                      variable=u,
                      value=val).grid(row=c1)
    bt=tkinter.Button(root,text="PROCEED",command=ShowChoice)
    bt.grid(columnspan=3)
import tkinter
from PIL import Image
from PIL import ImageTk
master = tkinter.Tk()
width = 400
height = 400
img1 = Image.open("MEDPLUS.png")
img1 = img1.resize((width,height), Image.ANTIALIAS)
photoImg1 =  ImageTk.PhotoImage(img1)
a= tkinter.Button(master,image=photoImg1,width=400,command=mainprogram).grid(row=0,column=1)
master.mainloop()
