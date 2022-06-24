def image():
    import tkinter
    from PIL import Image
    from PIL import ImageTk
    master = tkinter.Tk()
    width = 400
    height = 400
    img1 = Image.open("ALLSELLERS.png")
    img2 = Image.open("COMPETITIONS.png")
    img3 = Image.open("PIEPERSONAL.png")
    img4 = Image.open("GROWTHPERSONAL.png")
    img5 = Image.open("MARKETPULSE.png")
    img6 = Image.open("NEIGHBOURS.png")
    img1 = img1.resize((width,height), Image.ANTIALIAS)
    img2 = img2.resize((width,height), Image.ANTIALIAS)
    img3 = img3.resize((width,height), Image.ANTIALIAS)
    img4 = img4.resize((width,height), Image.ANTIALIAS)
    img5 = img5.resize((width,height), Image.ANTIALIAS)
    img6 = img6.resize((width,height), Image.ANTIALIAS)
    photoImg1 =  ImageTk.PhotoImage(img1)
    photoImg2 =  ImageTk.PhotoImage(img2)
    photoImg3 =  ImageTk.PhotoImage(img3)
    photoImg4 =  ImageTk.PhotoImage(img4)
    photoImg5 =  ImageTk.PhotoImage(img5)
    photoImg6 =  ImageTk.PhotoImage(img6)
    a= tkinter.Button(master,image=photoImg1,width=400).grid(row=0,column=1)
    b=tkinter.Button(master,image=photoImg2,width=400).grid(row=0,column=2)
    c=tkinter.Button(master,image=photoImg3,width=400).grid(row=0,column=3)
    d=tkinter.Button(master,image=photoImg4,width=400).grid(row=1,column=1)
    e=tkinter.Button(master,image=photoImg5,width=400).grid(row=1,column=2)
    f=tkinter.Button(master,image=photoImg6,width=400).grid(row=1,column=3)
    master.mainloop()
    print("THANK YOU FOR CHOOSING MEDPLUS.COM")
    import tkinter as tk
    master = tk.Tk()
    msgtext = "DEAR SELLER THANK YOU FOR CHOOSING MEDPLUS\nFOR AN FURTHER ASSISTANCE PLEASE MAIL US AT\nmedplusseller@gmail.com"
    msg = tk.Message(master, text = msgtext)
    msg.config(font=('times', 12))
    msg.pack()
    tk.mainloop()
        
    
def reportseller(user):
    def marketpulse():
        orders=[]
        sales=[]
        import csv
        with open("MEDSTORE.csv","r") as f:
            csv_reader=csv.reader(f,delimiter=",")
            next(csv_reader)
            x=list(csv_reader)
        import math
        from datetime import date
        today=date.today()
        p=today.month
        listmonth=[("JANUARY",1),("FEBRUARY",2),("MARCH",3),("APRIL",4),("MAY",5),("JUNE",6),("JULY",7),("AUGUST",8),("SEPTEMBER",9),("OCTCOBER",10),("NOVEMBER",11),("DECEMBER",12)]
        for i in range(len(listmonth)):
                       if listmonth[i][1]==p-1:
                           monthname=[listmonth[i-2][0],listmonth[i-1][0],listmonth[i][0]]
                           break
        salesa=[int(i[6]) for i in x if len(i)>0]
        salesb=[int(i[7]) for i in x if len(i)>0]
        salesc=[int(i[8]) for i in x if len(i)>0]
        ordersa=[int(i[9]) for i in x if len(i)>0]
        ordersb=[int(i[10]) for i in x if len(i)>0]
        ordersc=[int(i[11]) for i in x if len(i)>0]
        avg1=0
        avg2=0
        avg3=0
        avg4=0
        avg5=0
        avg6=0
        for i in salesa:
            avg1+=i
        for i in salesb:
            avg2+=i
        for i in salesc:
            avg3+=i
        for i in ordersa:
            avg4+=i
        for i in ordersb:
            avg5+=i
        for i in ordersc:
            avg6+=i
        sales=[avg1,avg2,avg3]
        orders=[avg4,avg5,avg6]
        import matplotlib.pyplot as plt 
        x = monthname
        y = sales
        a=monthname
        b=orders
        plt.plot(x, y,label="SALES")
        plt.plot(a,b,label="ORDERS")
        plt.xlabel('MONTH')
        plt.ylabel('SALES')
        plt.title('MARKET PULSE')
        plt.legend()
        plt.savefig("MARKETPULSE.png")
        plt.show()
    def projected(user):
        import math
        import csv
        l=[]
        with open("MEDSTORE.csv","r") as f:
            csv_reader=csv.reader(f,delimiter=",")
            next(csv_reader)
            for i in csv_reader:
                if len(i)>0:
                    if i[1]==user:
                        l.extend([int(i[6]),int(i[7]),int(i[8])])
                        name=i[0]
            a=sum(l)/len(l)
            md=[]
            for i in l:
                md.append(i-a)
            mda=sum(md)/len(md)
            projected=l[-1]+mda
            print("DEAR ",name,"YOUR PROJECTED SALES FOR THE NEXT MONTH IS",math.ceil(projected))
    def personal(user):
        import csv
        import math
        with open("MEDSTORE.csv","r") as f:
                    csv_reader=csv.reader(f)
                    next(csv_reader)
                    x=list(csv_reader)
        salespersonal=[]
        orderspersonal=[]
        for i in x:
            if len(i)>0:
                if i[1]==user:
                    salespersonal.extend([int(i[8]),int(i[7]),int(i[6])])
                    orderspersonal.extend([int(i[11]),int(i[10]),int(i[9])])
        from datetime import date
        today=date.today()
        p=today.month
        listmonth=[("JANUARY",1),("FEBRUARY",2),("MARCH",3),("APRIL",4),("MAY",5),("JUNE",6),("JULY",7),("AUGUST",8),("SEPTEMBER",9),("OCTCOBER",10),("NOVEMBER",11),("DECEMBER",12)]
        for i in range(len(listmonth)):
                   if listmonth[i][1]==p-1:
                       monthname=[listmonth[i-2][0],listmonth[i-1][0],listmonth[i][0]]
                       break
        print("1.SEE MY GROWTH\n2.SEE MY MONTHLY SALES DISTRIBUTION")
        while True:
            opt=input("ENTER YOUR CHOICE: ")
            if opt=="1":
                import matplotlib.pyplot as plt 
                x = monthname
                y = salespersonal
                a=monthname
                b=orderspersonal
                plt.plot(x, y,label="SALES")
                plt.plot(a,b,label="ORDERS")
                plt.xlabel('MONTH') 
                plt.ylabel('SALES') 
                plt.title('PERSONAL SALES')
                plt.legend()
                plt.savefig("GROWTHPERSONAL.png")
                plt.show()
            elif opt=="2":
                total=0
                for i in salespersonal:
                    total+=i
                mod=[]
                for i in salespersonal:
                    mod.append(math.ceil((i/total)*100))

                #TO GET SALES IN PERCENTAGE
                import matplotlib.pyplot as plotter
                figureObject, axesObject = plotter.subplots()
                axesObject.pie(mod,labels=monthname,autopct='%1.2f',startangle=90,explode=(0,0,0.3))
                frame=True
                axesObject.axis('equal')
                plotter.savefig("PIEPERSONAL.png")
                plotter.show()
            else:
                break
    def graphall(user):
        import csv
        with open("MEDSTORE.csv","r") as f:
            csv_reader=csv.reader(f)
            next(csv_reader)
            x=list(csv_reader)
        name=[]
        sales=[]
        for i in x:
            if len(i)>0:
                if i[0]!="":
                    name.append(i[0])
                    sales.append(int(i[6]))
        import matplotlib.pyplot as plt
        left=[]
        number=[]
        c=2
        m=1
        for i in range(len(sales)):
            left.append(c)
            c+=2
        height = sales
        tick_label = name
        plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'green','blue'],label="SELLERS") 
        plt.xlabel('SELLERS')
        plt.ylabel('SALES')
        plt.xticks(rotation=-90)
        plt.title('SALES GRAPH OF ALL REGISTERED SELLERS')
        plt.legend()
        plt.savefig("ALLSELLERS.png")
        plt.show()
    def neighbours(user):
        import csv
        import math
        with open("MEDSTORE.csv","r") as f:
                csv_reader=csv.reader(f)
                next(csv_reader)
                x=list(csv_reader)
        neighbourname=[]
        neighboursales=[]
        for i in x:
            if len(i)>0:
                if i[1]==user:
                    pinsearch=i[3]
                    for j in x:
                        if len(j)>0:
                            if math.fabs(int(j[3])-int(pinsearch))<2000 :
                                if j[1]==i[1]:
                                    neighbourname.append("YOUR STORE")
                                    neighboursales.append(int(j[6]))
                                else:
                                    neighbourname.append(j[0])
                                    neighboursales.append(int(j[6]))
                        
        print("1.VIEW ALL MY NEIGHBOURS\n2.GRAPHICALLY VIEW MY NEIGHBOURS")
        ch=input("ENTER YOUR CHOICE: ")
        if len(neighboursales)>1:
            if ch=="1":
                print("+","-"*25,"+")
                print("|","SL.NO","  |","NEIGHBOUR"," "*6,"|")
                print("+","-"*25,"+")
                c=0
                for i in range (len(neighbourname)):
                    if neighbourname[i]!="YOUR STORE":
                        print("|",c+1,".","   ","|",neighbourname[i]," "*(14-len(neighbourname[i])),"|")
                        c+=1
                print("+","-"*25,"+")
            elif ch=="2":
                import matplotlib.pyplot as plt 
                left=[]
                c=2
                for i in range(len(neighboursales)):
                    left.append(c)
                    c+=2
                height = neighboursales
                tick_label =neighbourname
                plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'green','blue'],label="NEIGHBOURS") 
                plt.xlabel('MY NEIGHBOURS')
                plt.ylabel('SALES')
                plt.title('SALES GRAPH OF ALL NEIGHBOURING SELLERS')
                plt.legend()
                plt.xticks(rotation=90)
                plt.savefig("NEIGHBOURS.png")
                plt.show()
        else:
            print("Oops!!You have no neighbours")
    def competitions(user):
        import math
        import csv
        print("1.SET LIMIT\n2.PROCEED WITH DEFAULT LIMIT")
        cha=input("ENTER YOUR CHOICE: ")
        if cha=="1":
            lim=int(input("ENTER YOUR LIMIT: "))
        else:
            lim=10000
        with open("MEDSTORE.csv","r") as f:
                csv_reader=csv.reader(f)
                next(csv_reader)
                x=list(csv_reader)
        compname=[]
        compsales=[]
        for i in x:
            if len(i)>0:
                if i[1]==user:
                    salesearch=i[6]
                    for j in x:
                        if len(j)>0:
                            if math.fabs(int(j[6])-int(salesearch))<lim:
                                if j[1]==i[1]:
                                    compname.append("YOUR STORE")
                                    compsales.append(int(j[6]))
                                else:
                                    compname.append(j[0])
                                    compsales.append(int(j[6]))
        print("1.VIEW ALL MY NEIGHBOURS\n2.GRAPHICALLY VIEW MY COMPETITIONS")
        ch=input("ENTER YOUR CHOICE: ")
        if len(compsales)>1:
            if ch=="1":
                print("+","-"*25,"+")
                print("|","SL.NO","  |","COMPETITION"," "*4,"|")
                print("+","-"*25,"+")
                c=0
                for i in range (len(compname)):
                    if compname[i]!="YOUR STORE":
                        print("|",c+1,".","   ","|",compname[i]," "*(14-len(compname[i])),"|")
                        c+=1
                print("+","-"*25,"+")
            elif ch=="2":
                import matplotlib.pyplot as plt 
                left=[]
                c=2
                for i in range(len(compsales)):
                    left.append(c)
                    c+=2
                height = compsales
                tick_label =compname
                plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'green','blue'],label="COMPETITIONS") 
                plt.xlabel('MY COMPETITIONS')
                plt.xticks(rotation=60)
                plt.ylabel('SALES')
                plt.title('SALES GRAPH OF ALL COMPETITORS') 
                plt.legend()
                plt.savefig("COMPETITIONS.png")
                plt.show()
        else:
            print("CONGRATS!!!YOU HAVE NO COMPETITIONS")
    def ranking(user):
        import csv
        with open("MEDSTORE.csv","r") as f:
                csv_reader=csv.reader(f)
                next(csv_reader)
                x=list(csv_reader)
        name=[]
        sales=[]
        for i in x:
            if len(i)>0:
                if i[1]==user:
                    namesearch=i[0]
                name.append(i[0])
                sales.append(int(i[6]))  
        list1=sales
        list2=name
        l=len(list1)
        for i in range(0,l):
            for j in range(l-i-1):
                if list1[j]>list1[j+1]:
                    list1[j+1],list1[j]=list1[j],list1[j+1]
                    list2[j+1],list2[j]=list2[j],list2[j+1]
        list1.reverse()
        list2.reverse()
        print("+","-"*60,"+")
        print("|","RANK  ","  |","SELLER"," "*44,"|")
        print("+","-"*60,"+")
        for i in range(len(list1)):
            print("|",i+1," "*(6-len(str(i+1))),"|",list2[i]," "*(50-len(list2[i])),"|")
            if list2[i]==namesearch:
                position=i+1
        print("+","-"*60,"+")
        print("CONGRATS YOU ARE IN THE",position,"th","position")

    print("WELCOME TO THE REPORT SECTION OF ALL REGISTERD SELLERS")
    while True:
        print("1.VIEW ALL SELLERS\n2.VIEW MY NEIGHBOURS\n3.VIEW MY COMPETITIONS\n4.SEE RANKING AND VIEW MY RANK\n5.VIEW PERSONAL PROFILE\n6.VIEW PROJECTED SALES FOR THE NEXT MONTH\n7.VIEW MARKET PULSE")
        ch=input("ENTER YOUR CHOICE: ")
        if ch=="1":
            graphall(user)
        elif ch=="2":
            neighbours(user)
        elif ch=="3":
            competitions(user)
        elif ch=="4":
            ranking(user)
        elif ch=="5":
            personal(user)
        elif ch=="6":
            projected(user)
        elif ch=="7":
            marketpulse()
        else:
            print("INVALID OPTION")
            print("DO YOU WANT TO CONTINUE IN REPORTS SECTION")
            print("1.YES\n2.NO")
            ch=input("ENTER YOUR OPTION: ")
            if ch=="1":
                continue
            elif ch=="2":
                break
                import sys;sys.exit()
def view(user):
    import csv
    with open("MEDSTORE.csv","r") as f:
        csv_reader=csv.reader(f)
        next(csv_reader)
        x=list(csv_reader)
    for i in range(len(x)):
        if len(x[i])>0:
            if x[i][1]==user:
               print("+","-"*133,"+")
               print("|NAME OF MEDICAL STORE"," "*4,"|","SELLER ID"," "*1,"|","LOCATION","  "*2,"|","NAME OF OWNER"," "*1,"|","GST NUMBER","|","PREVIOUS MONTH SALES","|","PREVIOUS MONTH ORDERS","|")
               print("+","-"*133,"+")
               print("|",x[i][0]," "*(24-len(x[i][0])),"|",x[i][1]," "*(10-len(x[i][1])),"|",x[i][2]," "*(12-len(x[i][2])),"|",x[i][4]," "*(14-len(x[i][4])),"|",x[i][5]," "*(9-len(x[i][5])),"|",x[i][6]," "*(19-len(x[i][6])),"|",x[i][9]," "*(20-len(x[i][9])),"|")
               print("+","-"*133,"+")
               print("YOU CAN EDIT THE DETAILS")
               print("1.EDIT DETAILS\n2.EXIT")
               ch=input("PLEASE ENTER YOUR CHOICE: ")
               if ch=="1":
                   print("1.STORE DETAILS\n2.FINANCIAL DETAILS")
                   ch1=input("ENTER YOUR OPTION: ")
                   if ch1=="1":
                       print("1.NAME OF THE RETAIL STORE\n2.NAME OF OWNER\n3.LOCATION AND PINCODE")
                       ch2=input("ENETER YOUR CHOICE:")
                       if ch2=="1":
                           oldname=input("ENETER THE OLD NAME OF THE RETAILS STORE AS PER REGISTERED")
                           newname=input("ENETER THE NEW NAME OF THE RETAILS STORE TO BE REGISTERED")
                           if x[i][0]==oldname:
                                x[i][0]=newname
                           else:
                               print("YOUR DETAILS COULD NOT BE VERIFIED")
                       elif ch2=="2":
                           oldname=input("ENETER THE OLD NAME OF THE OWNER AS PER REGISTERED")
                           newname=input("ENETER THE NEW NAME OF THE OWNER STORE TO BE REGISTERED")
                           if x[i][4]==oldname:
                                x[i][4]=newname
                           else:
                               print("YOUR DETAILS COULD NOT BE VERIFIED")
                       elif ch2=="3":
                           oldloc=input("ENETER THE OLD LOCATION STORE AS PER REGISTERED")
                           newloc=input("ENETER THE NEW LOCATION THE RETAILS STORE TO BE REGISTERED")
                           newpin=input("ENETER THE NEW PINCODE OF THE AREA")
                           if x[i][2]==oldloc:
                                x[i][2]=newloc
                                x[i][3]=newpin 
                           else:
                               print("YOUR DETAILS COULD NOT BE VERIFIED")
                       else:
                             print("INVALID OPTION")
                    
                   
                   elif ch1=="2":
                        print("1.GST NUMBER\n2.SALES")
                        ch2=input("ENTER YOUR CHOICE: ")
                        if ch2=="1":
                           oldgst=input("ENETER THE OLD GST REGISTERED")
                           newgst=input("ENETER THE NEW GST RETAILS STORE TO BE REGISTERED")
                           if x[i][5]==oldgst:
                                x[i][5]=newgst
                           else:
                               print("YOUR DETAILS COULD NOT BE VERIFIED")
                        elif ch2=="2":
                           newsales=input("ENETER THE NEW SALES OF THE RETAILS STORE TO BE REGISTERED")
                           x[i][6]=newsales
                   h=["NAME OF RETAIL STORE","ID","LOCATION","PINCODE","NAME OF OWNER","GST NO","PREVIOUS SALE"] 
                   with open("MEDSTORE.csv","w",newline=''  ) as f:
                        csv_writer=csv.writer(f)
                        csv_writer.writerow(h)
                        csv_writer.writerows(x)
                        import sys;sys.exit()
                   print("+","-"*133,"+")
                   print("|NAME OF MEDICAL STORE"," "*4,"|","SELLER ID"," "*1,"|","LOCATION","  "*2,"|","NAME OF OWNER"," "*1,"|","GST NUMBER","|","PREVIOUS MONTH SALES","|","PREVIOUS MONTH ORDERS","|")
                   print("+","-"*133,"+")
                   print("|",x[i][0]," "*(24-len(x[i][0])),"|",x[i][1]," "*(10-len(x[i][1])),"|",x[i][2]," "*(12-len(x[i][2])),"|",x[i][4]," "*(14-len(x[i][4])),"|",x[i][5]," "*(9-len(x[i][5])),"|",x[i][6]," "*(19-len(x[i][6])),"|",x[i][9]," "*(20-len(x[i][9])),"|")
                   print("+","-"*133,"+")
               elif ch=="2":
                       import sys;sys.exit()
    else:
        print("INVALID DETAILS")
        import sys;sys.exit()
def newseller():
    import csv
    print("HAI SELLER TO VIEW YOUR REPORTS PLEASE REGISTER")
    ch=input("PRESS THE ENTER THE ENTER KEY TO REGISTER AS A SELLER: ")
    if ch=="":
        def okay():
            import csv
            templist=[a.get(),b.get(),c.get(),int(d.get()),e.get(),f.get(),int(g.get()),int(h.get()),int(i.get()),int(j.get()),int(k.get()),int(l.get())]
            if int(g.get()) >10000 and int(h.get())>10000 and int(i.get())>10000:
                with open("MEDSTORE.csv","a") as f1:
                    csv_writer=csv.writer(f1)
                    csv_writer.writerow(templist)
                    user=b.get()
            else:
                print("SORRY YOUR STORE DOES NOT SATISFY ALL THE NECESSARY CONDITIONS TO REGISTER")
                print("PLEASE REFER TO THE DISCLAIMER")
                import sys;sys.exit()
            window.destroy()
            print("1.VIEW MY PROFILE\n2.REPORTS")
            ch=input("ENTER YOUR OPTION: ")
            if ch=="1":
                view(user)
            elif ch=="2":
                reportseller(user)
                image()
        import tkinter
        window=tkinter.Tk()
        window.title("REGISTRATION")
        tkinter.Label(window,text="ENTER THE NAME OF YOUR RETAIL STORE").grid(row=0)
        a=tkinter.Entry(window)
        a.grid(row=0,column=1)
        tkinter.Label(window,text="ENTER A USER ID FOR YOUR RETAIL SHOP").grid(row=1)
        b=tkinter.Entry(window)
        b.grid(row=1,column=1)
        tkinter.Label(window,text="ENTER THE LOCATION OF YOUR RETAIL STORE").grid(row=2)
        c=tkinter.Entry(window)
        c.grid(row=2,column=1)
        tkinter.Label(window,text="ENTER THE PINCODE OF YOUR STORE").grid(row=3)
        d=tkinter.Entry(window)
        d.grid(row=3,column=1)
        tkinter.Label(window,text="ENTER THE NAME OF THE RETAIL STORE OWNER").grid(row=4)
        e=tkinter.Entry(window)
        e.grid(row=4,column=1)
        tkinter.Label(window,text="ENTER THE GST ID OF YOUR STORE").grid(row=5)
        f=tkinter.Entry(window)
        f.grid(row=5,column=1)
        tkinter.Label(window,text="ENTER THE PREVIOUS MONTH SALES").grid(row=6)
        g=tkinter.Entry(window)
        g.grid(row=6,column=1)
        tkinter.Label(window,text="ENTER THE SECOND PREVIOUS MONTH SALES").grid(row=7)
        h=tkinter.Entry(window)
        h.grid(row=7,column=1)
        tkinter.Label(window,text="ENTER THE THIRD PREVIOUS MONTH SALES").grid(row=8)
        i=tkinter.Entry(window)
        i.grid(row=8,column=1)
        tkinter.Label(window,text="ENTER THE NUMBER OF ORDERS RECEIVED IN THE LAST MONTH").grid(row=9)
        j=tkinter.Entry(window)
        j.grid(row=9,column=1)
        tkinter.Label(window,text="ENTER THE NUMBER OF ORDERS RECEIVED IN THE SECOND LAST MONTH").grid(row=10)
        k=tkinter.Entry(window)
        k.grid(row=10,column=1)
        tkinter.Label(window,text="ENTER THE NUMBER OF ORDERS RECEIVED IN THE THIRD LAST MONTH").grid(row=11)
        l=tkinter.Entry(window)
        l.grid(row=11,column=1)
        bt=tkinter.Button(window,text="SUBMIT",command=okay)
        bt.grid(row=12)
        u=b.get()
        print(u)
        return u
def ShowChoice():
    num=u.get()
    root.destroy()
    if num==0:
        def close():
            user=a.get()
            window.destroy()
            print("1.VIEW MY PROFILE\n2.REPORTS")
            ch=input("ENTER YOUR OPTION")
            if ch=="1":
                view(user)
            elif ch=="2":
                reportseller(user)
                image()
            else:
                import sys;sys.exit()
        import tkinter
        window=tkinter.Tk()
        window.title("SIGNIN")
        tkinter.Label(window,text="ENTER YOUR USER ID").grid(row=0)
        a=tkinter.Entry(window)
        a.grid(row=0,column=1)
        bt=tkinter.Button(window,text="SUBMIT",command=close)
        bt.grid(row=1)
    elif num==1:
        user=newseller()
    elif num==2:
        def TERMS():
            import os;os.startfile("TERMS AND CONDITIONS.txt")
            print("THANK YOU FOR VISITING MEDPLUS")
            window.destroy()
        import tkinter
        import tkinter
        window=tkinter.Tk()
        window.title("TERMS AND CONDITION")
        tkinter.Label(window,text="DEAR SELLER YOU CAN VIEW OUR TERMS AND CONDITIONS BY CLICKING PROCEED").grid(row=0)
        bt=tkinter.Button(window,text=">>>PROCEED",command=TERMS)
        bt.grid(row=1)
import tkinter
root=tkinter.Tk()
root.title("WELCOME")
u = tkinter.IntVar()
u.set(0)  
users = [("EXISTING USER",1),("NEW USER",2),("VIEW THE TERMS AND CONDITIONS",3)]
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
