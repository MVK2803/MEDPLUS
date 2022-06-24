def cartview(finalbill,finalnameretail,finaldetails):
    def Payment(finalbill,finalnameretail,finaldetails):
        import csv
        print()
        f1=open("BILL.csv","w",newline='')
        writer=csv.writer(f1)
        writer.writerow(["MEDPLUS.COM","","","","","","TAX INVOICE"])
        writer.writerow(["SOLD BY","","","","","","BILLING LOCATION\PINCODE"])
        print("+","-"*101,"+")
        print("|","MEDPLUS.COM"," "*77,"TAX INVOICE","|")
        print("|","SOLD BY:"," "*66,"BILLING LOCATION\PINCODE:","|")
        x=str(finalnameretail[2])
        y=str(finaldetails[2])
        for i in range(2):
            print("|",finalnameretail[i]," "*(99-len(finalnameretail[i])-len(finaldetails[i])),finaldetails[i],"|")
            writer.writerow([str(finalnameretail[i]),"","","","","",str(finaldetails[i])])
        print("|",x," "*(99-len(x)-len(y)),y,"|")
        writer.writerow([x,"","","","","",y])
        print("+","-"*101,"+")
        print()
        print("  +","-"*98,"+")
        writer.writerow(["SL.NO","DESCRIPTION","UNIT PRICE","TAX","QUANTITY","NET RATE","TOTAL AMOUNT"])
        print("  |","SL.NO"," |","DESCRIPTION"," "*14,"|","UNIT PRICE"," |","TAX"," "*1," |","QUANTITY|","NET RATE"," "*3,"|","TOTAL AMOUNT","|")
        print("  +","-"*98,"+")
        totalbillamnt=0
        total1=0
        for i in finalbill:
            totalbillamnt+=i[6]
            total1+=i[5]
            a=str(i[0])
            b=str(i[1])
            c=str(i[2])
            d=str(i[3])
            e=str(i[4])
            f=str(i[5])[:7]
            g=str(i[6])[:7]
            writer.writerow([a,b,c,d,e,f,g])
            print("  |",i[0]," "*(5-len(a)),"|",i[1]," "*(25-len(b)),"|",i[2]," "*(10-len(c)),"|",i[3]," "*(5-len(d)),"|",i[4]," "*(5-len(e)+1),"|",f," "*(10-len(f)+1),"|",g," "*(12-len(g)-1),"|") 
        print("  +","-"*98,"+")
        if finaldetails[4]=="Platinum":
            disct=15
        elif finaldetails[4]=="Gold":
            disct=10
        elif finaldetails[4]=="Silver":
            disct=5
        else:
            disct=0
        print("+","-"*101,"+")
        print("|","TYPE OF MEMBERSHIP"," "*(80-len(finaldetails[4])),finaldetails[4]," |")
        print("|","% OF DISCOUNT"," "*(85-len(str(disct))),disct," |")
        print("|","NET RATE"," "*(90-len(str(total1))),total1," |")
        print("|","TOTAL TAX AMOUNT"," "*(82-len(str((totalbillamnt-total1))[:6])),str(totalbillamnt-total1)[:6]," |")
        print("|","TOTAL BILL AMOUNT"," "*75,str(totalbillamnt)[:6]," |")
        print("+","-"*101,"+")
        print("|","TOTAL AMOUNT PAYABLE"," "*72,str(totalbillamnt*(100-disct)/100)[:6]," |")
        print("+","-"*101,"+")
        print("NOW IT'S TIME FOR PAYMENT!!!!")
        print("a.CASH ON DELIVERY")
        print("b.PAYMENT THROUGH OUR ONLINE PARTNER's APP")
        print("c.NET BANKING")
        writer.writerow(["MEMBERSHIP TYPE","","","","","",finaldetails[4]])
        writer.writerow(["% OF DISCOUNT","","","","","",disct])
        writer.writerow(["NET RATE","","","","","",total1])
        writer.writerow(["TOTAL TAX AMOUNT","","","","","",str(totalbillamnt-total1)[:6]])
        writer.writerow(["TOTAL BILL AMOUNT","","","","","",str(totalbillamnt)[:6]])
        writer.writerow(["TOTAL AMOUNT PAYABLE","","","","","",str(totalbillamnt*(100-disct)/100)[:6]])
        ch=input("ENTER YOUR CHOICE TO PROCEED: ")
        if ch in 'Aa':
            print("THANK YOU FOR CHOOSING CASH ON DELIVERY OPTION\nPLEASE HAND OVER THE EXACT CHANGE TO OUR SERVICE EXCECUTIVE\nTHANK YOU")
        elif ch in 'Bb':
            def qr():
                def screenshot():
                    import pyautogui, time
                    time.sleep(6)
                    screenshot = pyautogui.screenshot()
                    screenshot.save("QRCODE.png")
                    master.destroy()

                import tkinter
                from PIL import Image
                from PIL import ImageTk
                master = tkinter.Tk()
                width = 200
                height = 200
                img1 = Image.open("TEST.png")
                img1 = img1.resize((width,height), Image.ANTIALIAS)
                photoImg1 =  ImageTk.PhotoImage(img1)
                a=tkinter.Button(master,image=photoImg1,width=200).grid(row=0,column=1)
                b=tkinter.Button(master,text="TAKE SCREENSHOT",command=screenshot).grid(row=0,column=2)
                master.mainloop()
            print("AS PER THE DETAILS GIVEN AT THE TIME OF REGISTRATION YOU HAVE OPTED FOR",finaldetails[3])
            ch2=input("TO CONTINUE WITH THIS PLEASE PRESS THE ENTER KEY,ELSE ENTER ANY OTHER KEY ")
            if ch2 =="":
                print("THANK YOU FOR CHOOSING",finaldetails[3])
            else:
                print("NOW YOU CAN CHOOSE OUR PREFERRED PARTNER.THIS IS ONLY A TEMPORARY CHANGE.")
                print("1.Google Pay\n2.Tez App\n3.Paytm")
                chi=int(input("ENTER YOUR CHOICE: "))
                if chi==1:
                    x="Google Pay"
                    print("THANK YOU FOR CHOOSING",x)
                elif chi==2:
                    x="Tez App"
                    print("THANK YOU FOR CHOOSING",x)
                elif chi==3:
                    x="Paytm"
                    print("THANK YOU FOR CHOOSING",x)
            qr()
            print("OUR SERVICE EXCECUTIVE WILL HELP YOU TO COMPLETE THE TRANSACTION AT THE TIME OF DELIVERY")
        elif ch in "cC":
            def otp(cost,end):        
                import time
                c=1
                t1=0
                import random,math
                string="0123456789qwertyuioplkjhgfdsazxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM"
                OTP=""
                length=len(string)
                for i in range(6):
                        OTP+=string[math.floor(random.random()*length)]
                y=OTP
                print("YOUR OTP FOR THE TRANSACTION OF",cost,"INR is",y,"\t THIS SHOULD NOT BE REVEALED TO ANY ONE.THIS WILL BE VALID FOR ONLY 3 ATTEMPTS")
                print(y)
                while c<=3:
                        to=time.perf_counter()
                        ot=input("ENTER OTP: ")
                        if ot==y:
                            t1+=time.perf_counter()-to
                            if(t1-to)>30:
                                    print("SORRY YOUR SEESION HAS TIMED OUT.PLEASE TRY AGAIN LATER.")
                                    break
                            else:
                                    print("SUCCESSFULLY TRANSFERRED")
                                    import tkinter as tk
                                    master = tk.Tk()
                                    msgtext = "AN AMOUNT OF"+cost+"INR HAS BEEN DEBITED FROM YOUR CARD ENDING IN ****"+end+"\nTHANK YOU FOR SHOPPPING WITH MEDPLUS.COM"
                                    msg = tk.Message(master, text = msgtext)
                                    msg.config(font=('times', 24))
                                    msg.pack()
                                    tk.mainloop()
                                    break
                        else:
                            t1+=time.perf_counter()-to
                            c+=1
                            if c<4:
                                print("ATTEMPT UNSUCCESSFULL,TRY AGAIN")
                            
                else:
                        print("THREE ATTEMPTS UNSUCCESSFUL TRY AGAIN LATER")

            import csv
            with open("CARD.csv","r") as f:
                csv_reader=csv.reader(f,delimiter=",")
                next(csv_reader)
                x=list(csv_reader)
            username=input("ENTER USERNAME: ")
            for i in x:
                if i[1]=="" and i[0]==username :
                    name=i[0]
                    cardnumber=input("ENTER A CARD NUMBER: ")
                    cvv=input("ENTER CVV OF YOUR CARD: ")
                    year=input("ENTER YEAR OF EXPIR: ")
                    month=input("ENTER MONTH OF EXPIRY: ")
                    x.remove(i)
                    x.append([name,cardnumber,cvv,year,month])
                    c=cardnumber[-4:]
                    otp(c) 
                    with open("carddetails.csv","w",newline='')as f:
                            heading=["Username","CardNumber","CVV","Yaer of Expiry","Month Of Expiry"]
                            csv_writer=csv.writer(f)
                            csv_writer.writerow(heading)
                            csv_writer.writerows(x)
                    break

                elif i[0]==username and i[1]!="":
                    card=input("ENTER A CARD NUMBER: ")
                    cvv=input("ENTER CVV OF YOUR CARD: ")
                    year=input("ENTER YEAR OF EXPIRY: ")
                    month=input("ENTER MONTH OF EXPIRY: ")
                    if int(i[1])==int(card) and int(i[2])==int(cvv) and int(i[3])==int(year) and int(i[4])==int(month):
                        end=i[1][-4:]
                        cost=str(totalbillamnt*(100-disct)/100)[:6]
                        otp(cost,end)
                        break
                    else:
                        print("INVALID CREDENTIALS")
            else:
                print("OOPS WE WERE UNABLE TO FIND THE CARD IN OUR DATABASE.")
                ch=input( "TO REGISTER A NEW CARD PRESS THE ENTER KEY: ")
                if ch=="":
                    name=input("ENTER YOUR NEW USERNAME:")
                    cardnumber=input("ENTER YOUR CARD NUMBER: ")
                    cvv=input("ENTER CVV NUMBER: ")
                    year=input("ENTER YEAR OF EXPIRY: ")
                    month=input("ENTER MONTH OF EXPIRY: ")
                    x.remove(i)
                    x.append([name,cardnumber,cvv,year,month])
                    end=cardnumber[-4:]
                    cost=str(totalbillamnt*(100-disct)/100)[:6]
                    otp(cost,end) 
                    with open("CARD.csv","w",newline='')as f:
                            heading=["Username","CardNumber","CVV","Yaer of Expiry","Month Of Expiry"]
                            csv_writer=csv.writer(f)
                            csv_writer.writerow(heading)
                            csv_writer.writerows(x)
        f1.close()
        with open ("BILL.csv","r") as f1:
            reader=csv.reader(f1,delimiter=",")
            reader=list(reader)
        def print1():
            import os
            os.startfile("BILL.csv","print")
            window.destroy()
        def exit1():
            window.destroy
        import tkinter
        import csv
        window=tkinter.Tk()
        window.title("BILL")
        for i in range (len(reader)):
            tkinter.Label(window,text=str(reader[i][0])).grid(row=i,column=1)
            tkinter.Label(window,text=str(reader[i][1])).grid(row=i,column=2)
            tkinter.Label(window,text=str(reader[i][2])).grid(row=i,column=3)
            tkinter.Label(window,text=str(reader[i][3])).grid(row=i,column=4)
            tkinter.Label(window,text=str(reader[i][4])).grid(row=i,column=5)
            tkinter.Label(window,text=str(reader[i][5])).grid(row=i,column=6)
            tkinter.Label(window,text=str(reader[i][6])).grid(row=i,column=7)
        f1.close()
        button1=tkinter.Button(window,text="EXIT",command=exit1)
        button1.grid(row=len(reader)+3,column=1)
        button2=tkinter.Button(window,text="PRINT",command=print1)
        button2.grid(row=len(reader)+3,column=4)
        print("THANK YOU FOR CHOOSING MEDPLUS.COM")
        import tkinter as tk
        master = tk.Tk()
        msgtext = "DEAR "+finaldetails[0]+" YOUR MEDICINES WILL BE DELIVERED IN 3 DAYS BY OUR DELIVERY AGENT\nFOR AN FURTHER ASSISTANCE PLEASE MAIL US AT\nmedpluscustomer@gmail.com"
        msg = tk.Message(master, text = msgtext)
        msg.config(font=('times', 12))
        msg.pack()
        tk.mainloop()
        
    print("+","-"*45,"+")
    print("|","SL.NO"," |","DESCRIPTION"," "*14, "|","QUANTITY|")
    print("+","-"*45,"+")
    for i in finalbill:
                a=str(i[0])
                b=str(i[1])
                c=str(i[4])
                print("|",a," "*(5-len(a)),"|",b," "*(25-len(b)),"|",c," "*(6-len(c)),"|")
    print("+","-"*45,"+")
    print("1.PROCEED TO PAYMENT\n2.EDIT MY CART")
    ch=input("ENTER YOUR CHOICE: ")
    if ch=="1":
        Payment(finalbill,finalnameretail,finaldetails)
    elif ch=="2":
        opt=input("PLEASE ENTER THE SERIAL NUMBER OF THE ITEM YOU WANT TO MAKE CHANGE TO: ")
        if int(opt)<=len(finalbill):
            print("1.REMOVE THIS ITEM FROM THE LIST\n2.MAKE A CHANGE IN THE QUANTITY")
            ch=input("ENTER YOUR CHOICE: ")
            if ch=="1":
                for i in finalbill:
                    if i[0]==int(opt):
                        finalbill.remove(i)
                        for i in range(len(finalbill)):
                            finalbill[i][0]=i+1
                        print("THE ITEM HAS BEEN REMOVED FROM YOUR CART")
                        print("+","-"*45,"+")
                        print("|","SL.NO"," |","DESCRIPTION"," "*14, "|","QUANTITY|")
                        print("+","-"*45,"+")
                        for i in finalbill:
                                    a=str(i[0])
                                    b=str(i[1])
                                    c=str(i[4])
                                    print("|",a," "*(5-len(a)),"|",b," "*(25-len(b)),"|",c," "*(6-len(c)),"|")
                        print("+","-"*45,"+")
            elif ch=="2":
                for i in finalbill:
                    if i[0]==int(opt):
                        newqty=int(input("PLEASE ENTER THE NEW QUANTITY: "))
                        i[5]+=(i[2]*(newqty-i[4]))
                        i[6]=i[5]*((100+i[3])/100)
                        i[4]=newqty
                        print("THE QUANTITY HAS BEEN CHANGED")
                        print("+","-"*45,"+")
                        print("|","SL.NO"," |","DESCRIPTION"," "*14, "|","QUANTITY|")
                        print("+","-"*45,"+")
                        for i in finalbill:
                                    a=str(i[0])
                                    b=str(i[1])
                                    c=str(i[4])
                                    print("|",a," "*(5-len(a)),"|",b," "*(25-len(b)),"|",c," "*(6-len(c)),"|")
                        print("+","-"*45,"+")
            ch1=input("TO PROCEED TO PAYMENT PRESS THE ENTER KEY: ")
            if ch1=="":
               Payment(finalbill,finalnameretail,finaldetails)
    else:
        import sys;sys.exit()
                        
                

def shopping(finalnameretail,finaldetails):
    print("HAI",finaldetails[0],"WELCOME TO MEDPLUS.COM") 
    chentry=input("LET'S BEGIN SHOPPING!!!,TO CONTINUE SHOPPING PRESS THE ENTER KEY:")
    if chentry=="":
        import csv
        with open("medicines.csv","r")as x:
            reader=csv.reader(x,delimiter=",")
            next(reader)
            meddet=list(reader)
        medname=[]
        medrate=[]
        meditax=[]
        for i in meddet:
            medname.append(i[0])
            medrate.append(float(i[3]))
            meditax.append(i[4])
        print("1.HAVE A PRESCRIPTION\n2.NO PRESRIPTION")
        ch_1=input("ENTER YOUR CHOICE: ")
        medamnt=[]
        medtax=[]
        billname=[]
        billqty=[]
        billrate=[]
        if ch_1=="1":
            nos=int(input("ENTER NUMBER OF MEDICINES: "))
            for i in range(nos):
                name=input("ENTER THE NAME OF THE MEDICINE: ")
                qty=int(input("ENTER THE QUANTITY REQUIRED: "))
                c=0
                for j in medname:
                    c+=1
                    if name==j:
                        medamnt.append(medrate[c-1])
                        medtax.append(int(meditax[c-1]))
                        billname.append(name)
                        billqty.append(qty)
                        billrate.append(medrate[c-1]*float(qty))
                        break
                else:
                      print("OOPS!!!NOT FOUND")
        elif ch_1=="2":
            import csv
            with open("medicines.csv","r") as f:
                reader=csv.reader(f,delimiter=",")
                next(reader)
                reader=list(reader)
            group=[]
            for i in reader:
                group.append([i[0],i[6]])
            dic1={}
            l=len(group)
            for i in range(l):
                while group[i][1] not in dic1:
                    temp=group[i][1]
                    tup=()
                    for j in group:
                        if j[1]==temp:
                            tup+=(j[0],)
                    dic1[temp]=tup
            grp=["A.","B.","C.","D."]
            c1=0
            for i in dic1:
                print("+","-"*27,"+")
                c=1
                print("|",grp[c1]," |",i," "*(20-len(i)),"|")
                print("+","-"*27,"+")
                c1+=1
                for j in dic1[i]:
                    print("|",c,".","|",j," "*(20-len(j)),"|")
                    c+=1
                print("+","-"*27,"+")
            n=int(input("ENTER THE NUMBER OF MEDICINES YOU WOULD LIKE TO CHOOSE: "))
            for i in range(n):
                    GRP1=input("ENTER THE TYPE OF MEDICINE A/B/C/D: ")
                    GRP2=int(input("ENTER THE SERIAL NUMBER OF MEDICINE: "))
                    if GRP1=="A":
                        x="Alopathy"
                    elif GRP1=="B":
                        x="Ayurvedic"
                    elif GRP1=="C":
                        x="Beauty"
                    else:
                        x="Health Suppliment"
                    name=dic1[x][(GRP2-1)]

                    qty=int(input("ENTER THE QUANTITY YOU WOULD LIKE TO PURCHASE: "))
                    c=0
                    for j in medname:
                                c+=1
                                if name==j:
                                    medamnt.append(medrate[c-1])
                                    medtax.append(int(meditax[c-1]))
                                    billname.append(name)
                                    billqty.append(qty)
                                    billrate.append(medrate[c-1]*float(qty))
                                    break
                    else:
                            print("NOT FOUND")
        finalbill=[]
        for i in range(len(billname)):
            temptax=medtax[i]/100
            totalitem=billrate[i]+(billrate[i]*temptax)
            tempbill=[i+1,billname[i],medamnt[i],medtax[i],billqty[i],billrate[i],totalitem]
            finalbill.append(tempbill)
        cartview(finalbill,finalnameretail,finaldetails)
                
        
    else:
        print("THANK YOU FOR VISITING MEDPLUS.COM")

def storelocator(finalname,finaldetails):
    import csv
    import math
    with open("MEDSTORE.csv","r")as x:
        y=csv.reader(x,delimiter=",")
        next(y)
        ylist=list(y)
    NAME=[]
    ID=[]
    LOCATION=[]
    PINCODE=[]
    for i in ylist:
        if len(i)>0:
            NAME.append(i[0])
            ID.append(i[1])
            LOCATION.append(i[2])
            PINCODE.append(i[3])
    with open("CUSTOMER.csv","r")as y:
        reader=csv.reader(y,delimiter=",")
        next(reader)
        x=list(reader)
    PIN=[]
    NAMED=[]
    for i in x:
        NAMED.append(i[2])
        PIN.append(i[3])
    tempdiff=[]
    for i in range (len(NAMED)):
            if  finalname!="" and finalname==NAMED[i]:
                pin=int(PIN[i])
                for j in range(len(PINCODE)):
                    x=int(math.fabs(pin-int(PINCODE[j])))   
                    tempdiff.append(x)
                break
    if len(tempdiff)>0:
        minpin=min(tempdiff)
        for i in range(len(tempdiff)):
            if tempdiff[i]==minpin:
                finalnameretail=[NAME[i],LOCATION[i],PINCODE[i]]
                shopping(finalnameretail,finaldetails)
                break

    else:
        print("OOPS!!!ENTRY NOT FOUND")
    return x
def registration():
    def okay():
        import csv
        with open("CUSTOMER.csv","r")as x1:
            reader=csv.reader(x1,delimiter=",")
            result=list(reader)
        templist=[y.get(),z.get(),x.get(),int(a.get()),member[u.get()][0],f.get(),payments[v.get()][0]]
        result.append(templist)
        finalname=x.get()
        finaldetails=[x.get(),f.get(),int(a.get()),payments[v.get()][0],member[u.get()][0]]  
        with open("CUSTOMER.csv","w",newline='')as x2:
            csv_records=csv.writer(x2)
            csv_records.writerows(result)
        storename=storelocator(finalname,finaldetails)
        window.destroy()
    import tkinter
    window=tkinter.Tk()
    window.title("REGISTRATION")
    tkinter.Label(window,text="ENTER NAME").grid(row=0)
    x=tkinter.Entry(window)
    x.grid(row=0,column=1)
    tkinter.Label(window,text="ENTER USERNAME").grid(row=1)
    y=tkinter.Entry(window)
    y.grid(row=1,column=1)
    tkinter.Label(window,text="ENTER PASSWORD").grid(row=2)
    z=tkinter.Entry(window,show="*")
    z.grid(row=2,column=1)
    tkinter.Label(window,text="ENTER LOCATION OF DELIVERY").grid(row=3)
    f=tkinter.Entry(window)
    f.grid(row=3,column=1)
    tkinter.Label(window,text="ENTER PINCODE").grid(row=4)
    a=tkinter.Entry(window)
    a.grid(row=4,column=1)
    finalname=x.get()
    u = tkinter.IntVar()
    u.set(0)  
    member = [("Gold",1),("Platinum",2),("Silver",3),("Not intereted now",4)]
    tkinter.Label(window, text="""CHOOSE THE TYPE OF MEMBERSHIP YOU WANT""").grid(row=5)
    c1=0
    for val, membership in enumerate(member):
        c1+=1
        tkinter.Radiobutton(window, 
                      text=membership[0],
                       
                      variable=u,
                      value=val).grid(row=5,column=c1)
    v = tkinter.IntVar()
    v.set(0)  
    payments = [("Paytm",1),("Tez App",2),("Google Pay",3)]
    def ShowChoice():
        x=v.get()
        print(payments[x][0])

    tkinter.Label(window, 
             text="""CHOOSE ANY ONE AF OUR ONLINE PAYMENT PARTNER""").grid(row=6)
    c=0
    for val, payment in enumerate(payments):
        c+=1
        tkinter.Radiobutton(window, 
                      text=payment[0],
                       
                      variable=v,
                      value=val).grid(row=6,column=c)
    bt=tkinter.Button(window,text="SUBMIT",command=okay)
    bt.grid(columnspan=8)

    window.mainloop()
       




def nameerror():
        import tkinter
        error=tkinter.Tk()
        error.title("ERROR")
        tkinter.Message(error,text="INVALID CREDENTIALS\nPLEASE TRY AGAIN LATER!!!").grid(row=0)

def password():
    import csv
    with open("CUSTOMER.csv","r")as x3:
        reader=csv.reader(x3,delimiter=",")
        next(reader)
        s=list(reader)
    user=[]
    password=[]
    name=[]
    location=[]
    mempincode=[]
    Type=[]
    onlinepay=[]
    for i in s:
        user.append(i[0])
        password.append(int(i[1]))
        name.append(i[2])
        mempincode.append(i[3])
        Type.append(i[4])
        location.append(i[5])
        onlinepay.append(i[6])
            
    def check():
                username=x.get()
                passcode=int(y.get())
                window.destroy()
                for i in range(0,len(user),1):
                    if user[i]==username and password[i]==passcode:
                        finalname=name[i]
                        finalloaction=location[i]
                        fianlpin=mempincode[i]
                        finalonlinepay=onlinepay[i]
                        finaltype=Type[i]
                        finaldetails=[finalname,finalloaction,fianlpin,finalonlinepay,finaltype]
                        finalname=name[i]
                        storename=storelocator(finalname,finaldetails)
                        break
                else:
                     finalname=""
                     nameerror()
                
    import tkinter
    window=tkinter.Tk()
    window.title("SIGNIN")
    tkinter.Label(window,text="ENTER USERNAME").grid(row=0)
    x=tkinter.Entry(window)
    x.grid(row=0,column=1)
    tkinter.Label(window,text="ENTER PASSWORD").grid(row=1)
    y=tkinter.Entry(window,show="*")
    y.grid(row=1,column=1)
    tkinter.Checkbutton(window,text="Keep Me Logged In").grid(columnspan=2)
    bt=tkinter.Button(window,text="SUBMIT",command=check)
    bt.grid(columnspan=3)
    window.mainloop()
def ShowChoice():
    num=u.get()
    root.destroy()
    if num==0:
        password()
    else:
        registration()
import tkinter
root=tkinter.Tk()
root.title("WELCOME")
u = tkinter.IntVar()
u.set(0)  
users = [("EXISTING USER",1),("NEW USER",2)]
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
