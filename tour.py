import sqlite3 as sq
try:
    conn=sq.connect("tours.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tours(
    To_place text,
    From_place text,
    Interval text,
    Amount text,
    Tour_code text PRIMARY KEY);""")

    from tkinter import *
    import tkinter.messagebox

    def res():
        if(v.get()==2):
            w.destroy()
            def show():
                list1.delete(0,END)
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM tours")
                a=cursor.fetchall() #fetches whole data from the db
                for i in a:
                    list1.insert(END,i)
                if list1.size()==0:
                    tkinter.messagebox.showinfo("Underflow","Oops!! Nothing to show")
            def search():
                t=str(e1.get())
                f=str(e2.get())
                dt=str(e3.get())
                a=str(e4.get())
                c=str(e5.get())
                if(t=="" and f=="" and dt=="" and a=="" and c==""):
                    tkinter.messagebox.showinfo("Error","None of the fields are filled")
                else:
                    m=[]
                    if(t!=""):
                        f1="To_place=? and"
                        m.append(t)
                    else:
                        f1=""
                    if(f!=""):
                        f2="From_place=? and"
                        m.append(f)
                    else:
                        f2=""
                    if(dt!=""):
                        f3="Interval=? and"
                        m.append(dt)
                    else:
                        f3=""
                    if(a!=""):
                        f4="Amount=? and"
                        m.append(a)
                    else:
                        f4=""
                    if(c!=""):
                        f5="Tour_code=?"
                        m.append(c)
                    else:
                        f5="Tour_code!=?"
                        m.append(c)
                    cursor=conn.cursor()
                    cursor.execute(f"""SELECT * FROM tours WHERE {f1} {f2} {f3} {f4} {f5}""",m)
                    rows=cursor.fetchall()
                    if(rows==[]):
                        tkinter.messagebox.showinfo("Alert","No record found")
                    else:
                        list1.delete(0,END)
                        for i in rows:
                            list1.insert(END,i)
            def close():
                answer=tkinter.messagebox.askquestion("Exit","Are you sure you want to exit ?")
                if answer=="yes":
                    w1.destroy()
                else:
                    pass
            def set(m):
                i=list1.curselection()
                if(len(i)==0):
                    pass
                else:
                    b=i[0]
                    j1,j2,j3,j4,j5=list1.get(b)
                    e1.delete(0,END)
                    e1.insert(END,j1)
                    e2.delete(0,END)
                    e2.insert(END,j2)
                    e3.delete(0,END)
                    e3.insert(END,j3) 
                    e4.delete(0,END)
                    e4.insert(END,j4)
                    e5.delete(0,END)
                    e5.insert(END,j5)
            def clear1():
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)

            w1=Tk()
            w1.title("TOURS AND TRAVELS (USER MODULE)")
            w1.configure(background="light green")
            l1 = Label(w1, text="TO" ,bg='yellow' ,font=("Comic Sans MS",20))
            l1.grid(row=0, column=0)

            l2 = Label(w1, text="FROM" ,bg='yellow' ,font=("Comic Sans MS",20))
            l2.grid(row=0, column=3)

            l3 = Label(w1, text="INTERVAL",bg='yellow' ,font=("Comic Sans MS",20))
            l3.grid(row=1, column=0)

            l4 = Label(w1, text="AMOUNT",bg='yellow' ,font=("Comic Sans MS",20))
            l4.grid(row=1, column=3)

            l5=Label(w1,text="TOUR CODE",bg='yellow' ,font=("Comic Sans MS",20))
            l5.grid(row=2, column=0)

            l6=Label(w1,text="====To\tFrom\tInterval\tAmount\tTour code====",bg='yellow',font=("Comic Sans MS",16))
            l6.grid(row=4,column=0)

            from_text = StringVar()
            e1 = Entry(w1, textvariable=from_text,bg="pink",font=("Calibri",20))
            e1.grid(row=0, column=1)

            to_text = StringVar()
            e2 = Entry(w1, textvariable=to_text,bg="pink",font=("Calibri",20))
            e2.grid(row=0, column=4)

            traveldt_text = StringVar()
            e3 = Entry(w1, textvariable=traveldt_text,bg="pink",font=("Calibri",20))
            e3.grid(row=1, column=1)

            amount_text = StringVar()
            e4= Entry(w1, textvariable=amount_text,bg="pink",font=("Calibri",20))
            e4.grid(row=1, column=4)

            tourcode_id=StringVar()
            e5=Entry(w1, textvariable=tourcode_id,bg="pink",font=("Calibri",20))
            e5.grid(row=2, column=1)

            list1 = Listbox(w1, height=7, width=35,bg="light blue",fg="red",font=("Calibri",20))
            list1.bind('<<ListboxSelect>>', set)
            list1.grid(row=5, column=0, rowspan=6, columnspan=1)

            sb1 = Scrollbar(w1)
            sb1.grid(row=3, column=1, rowspan=6)
            list1.config(yscrollcommand=sb1.set)
            sb1.config(command=list1.yview)
            b1 = Button(w1, text="SHOW DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=show)
            b1.grid(row=4, column=3)

            b4 = Button(w1, text="SEARCH DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=search)
            b4.grid(row=5, column=3)

            b6 = Button(w1, text="CLOSE",width=16,bg="black",fg="white",font=("Calibri",20),command=close)
            b6.grid(row=6, column=3)
            w1.mainloop()
        elif(v.get()==1):
            def check():
                p=e.get()
                if(p=="Hello"):
                    window1.destroy()
                    w.destroy()
                    window=Tk()
                    def set(m):
                        i=list1.curselection()
                        if(len(i)==0):
                            pass
                        else:
                            b=i[0]
                            j1,j2,j3,j4,j5=list1.get(b)
                            e1.delete(0,END)
                            e1.insert(END,j1)
                            e2.delete(0,END)
                            e2.insert(END,j2)
                            e3.delete(0,END)
                            e3.insert(END,j3)
                            e4.delete(0,END)
                            e4.insert(END,j4)
                            e5.delete(0,END)
                            e5.insert(END,j5)
                    def clear1():
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)

                    def show():
                        list1.delete(0,END)
                        cursor=conn.cursor()
                        cursor.execute("SELECT * FROM tours")
                        a=cursor.fetchall() #fetches whole data from the db
                        for i in a:
                            list1.insert(END,i)
                        if list1.size()==0:
                            tkinter.messagebox.showinfo("Underflow","Oops!! Nothing to show")
                    def add():
                        t=str(e1.get())
                        f=str(e2.get())
                        dt=str(e3.get())
                        a=str(e4.get())
                        c=str(e5.get())
                        if(t=="" or f=="" or dt=="" or a=="" or c==""):
                            tkinter.messagebox.showinfo("Error","All fields not filled")
                        else:
                            cursor=conn.cursor()
                            cursor.execute("SELECT * FROM tours WHERE Tour_code=?",[c])
                            a1=cursor.fetchone()
                            if(a1==None):
                                k=[t,f,dt,a,c]
                                cursor=conn.cursor()
                                cursor.execute("INSERT INTO tours VALUES(?,?,?,?,?);",k)
                                conn.commit()
                                show()
                                tkinter.messagebox.showinfo("Alert","Data Added")
                                clear1()
                            else:
                                tkinter.messagebox.showinfo("Error", "Tour_code cannot be same")
                    def update():
                        upd=list1.curselection()
                        if upd==():
                            show()
                            tkinter.messagebox.showinfo("Alert","Entry not selected")
                        else:
                            upd=list1.get(upd[0])
                            cd=upd[4]
                            tkinter.messagebox.showinfo("Alert","Updation would be done in accordance with Tour_code")
                            t=str(e1.get())
                            f=str(e2.get())
                            dt=str(e3.get())
                            a=str(e4.get())
                            c=str(e5.get())
                            if(t=="" or f=="" or dt=="" or a=="" or c==""):
                                tkinter.messagebox.showinfo("Error","All fields not filled")
                            else:
                                cursor=conn.cursor()
                                cursor.execute("SELECT Tour_code FROM tours WHERE Tour_code=?",[cd])
                                rows=cursor.fetchone()
                            if(rows==None):
                                tkinter.messagebox.showinfo("Alert","Given Tour_code do not exist")
                            else:
                                if(c==cd):
                                    cursor.execute("""UPDATE tours SET To_place=?,From_place=?,Interval=?,Amount=?,Tour_code=? WHERE Tour_code=?""",[t,f,dt,a,c,cd])
                                    conn.commit()
                                    show()
                                    tkinter.messagebox.showinfo("Alert", "Data Updated")
                                    clear1()
                                else:
                                    cursor.execute("SELECT * FROM tours WHERE Tour_code=?",[c])
                                    a1=cursor.fetchone()
                                    if(a1==None):
                                        cursor=conn.cursor()
                                        cursor.execute("""UPDATE tours SET To_place=?,From_place=?,Interval=?,Amount=?,Tour_code=? WHERE Tour_code=?""",[t,f,dt,a,c,cd])
                                        conn.commit()
                                        show()
                                        tkinter.messagebox.showinfo("Alert", "Data Updated")
                                        clear1()
                                    else:
                                        tkinter.messagebox.showinfo("Alert","Tour code already exists for some other entry")
                    def search():
                        t=str(e1.get())
                        f=str(e2.get())
                        dt=str(e3.get())
                        a=str(e4.get())
                        c=str(e5.get())
                        if(t=="" and f=="" and dt=="" and a=="" and c==""):
                            tkinter.messagebox.showinfo("Error","None of the fields are filled")
                        else:
                            m=[]
                            if(t!=""):
                                f1="To_place=? and"
                                m.append(t)
                            else:
                                f1=""
                            if(f!=""):
                                f2="From_place=? and"
                                m.append(f)
                            else:
                                f2=""
                            if(dt!=""):
                                f3="Interval=? and"
                                m.append(dt)
                            else:
                                f3=""
                            if(a!=""):
                                f4="Amount=? and"
                                m.append(a)
                            else:
                                f4=""
                                if(c!=""):
                                    f5="Tour_code=?"
                                    m.append(c)
                                else:
                                    f5="Tour_code!=?"
                                    m.append(c)
                                    cursor=conn.cursor()
                                    cursor.execute(f"""SELECT * FROM tours WHERE {f1} {f2} {f3} {f4} {f5}""",m)
                                    rows=cursor.fetchall()
                                    if(rows==[]):
                                        tkinter.messagebox.showinfo("Alert","No record found")
                                    else:
                                        list1.delete(0,END)
                                    for i in rows:
                                        list1.insert(END,i)
                    def delete():
                        dele=list1.curselection()
                        if dele==():
                            show()
                            tkinter.messagebox.showinfo("Alert","Select item from list box that you wish to delete")
                        else:
                            r=dele[::-1]
                            for x in r:
                                delete=list1.get(x)
                                code=delete[4]
                                cursor=conn.cursor()
                                cursor.execute("DELETE FROM tours WHERE Tour_code=?",[code])
                                conn.commit()
                                show()
                                tkinter.messagebox.showinfo("Alert","Data deleted")
                                clear1()
                    def close():
                        answer=tkinter.messagebox.askquestion("Exit","Are you sure you want to exit ?")
                        if answer=="yes":
                            window.destroy()
                        else:
                            pass

                    window.title("TOURS AND TRAVELS (ADMIN MODULE)")
                    window.configure(background="light green")

                    l1 = Label(window, text="TO" ,bg='yellow' ,font=("Comic Sans MS",20))
                    l1.grid(row=0, column=0)

                    l2 = Label(window, text="FROM" ,bg='yellow' ,font=("Comic Sans MS",20))
                    l2.grid(row=0, column=3)

                    l3 = Label(window, text="INTERVAL",bg='yellow' ,font=("Comic Sans MS",20))
                    l3.grid(row=1, column=0)

                    l4 = Label(window, text="AMOUNT",bg='yellow' ,font=("Comic Sans MS",20))
                    l4.grid(row=1, column=3)

                    l5=Label(window,text="TOUR CODE",bg='yellow' ,font=("Comic Sans MS",20))
                    l5.grid(row=2, column=0)

                    l6=Label(window,text="====To\tFrom\tInterval\tAmount\tTour code====",bg='yellow' ,font=("Comic Sans MS",16))
                    l6.grid(row=4,column=0)

                    from_text = StringVar()
                    e1 = Entry(window, textvariable=from_text,bg="pink",font=("Calibri",20))
                    e1.grid(row=0, column=1)

                    to_text = StringVar()
                    e2 = Entry(window, textvariable=to_text,bg="pink",font=("Calibri",20))
                    e2.grid(row=0, column=4)

                    traveldt_text = StringVar()
                    e3 = Entry(window, textvariable=traveldt_text,bg="pink",font=("Calibri",20))
                    e3.grid(row=1, column=1)

                    amount_text = StringVar()
                    e4= Entry(window, textvariable=amount_text,bg="pink",font=("Calibri",20))
                    e4.grid(row=1, column=4)

                    tourcode_id=StringVar()
                    e5=Entry(window, textvariable=tourcode_id,bg="pink",font=("Calibri",20))
                    e5.grid(row=2, column=1)

                    list1 = Listbox(window, height=7, width=35,bg="light blue",fg="red",font=("Calibri",20),selectmode=MULTIPLE)
                    list1.bind('<<ListboxSelect>>', set)
                    list1.grid(row=4, column=0, rowspan=6, columnspan=1)

                    sb1 = Scrollbar(window)
                    sb1.grid(row=3, column=1, rowspan=6)
                    list1.config(yscrollcommand=sb1.set)
                    sb1.config(command=list1.yview)

                    b1 = Button(window, text="SHOW DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=show)
                    b1.grid(row=4, column=3)

                    b2 = Button(window, text="ADD DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=add) # no bracket with function
                    b2.grid(row=5, column=4)

                    b3 = Button(window, text="UPDATE DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=update)
                    b3.grid(row=6, column=3)

                    b4 = Button(window, text="SEARCH DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=search)
                    b4.grid(row=7, column=4)

                    b5 = Button(window, text="DELETE DATA",width=16,bg="black",fg="white",font=("Calibri",20),command=delete)
                    b5.grid(row=8, column=3)

                    b6 = Button(window, text="CLOSE",width=16,bg="black",fg="white",font=("Calibri",20),command=close)
                    b6.grid(row=9, column=4)

                    window.mainloop()
                    conn.commit()
                else:
                    tkinter.messagebox.showinfo("Status", "Wrong password")
            window1=Tk()
            window1.geometry("430x120+300+400")
            window1.configure(background="light green")
            window1.title("TOURS AND TRAVELS ADMIN LOGIN")
            l1=Label(window1,text="Enter password:",bg='yellow' ,font=("Comic Sans MS",15))
            l1.grid(row=0,column=0)
            s=StringVar()
            e=Entry(window1,textvariable=s,bg="pink",font=("Calibri",15),width=10)
            e.grid(row=1,column=1)
            b=Button(window1,text="Login as admin",command=check,bg="teal",fg="white",font=("Calibri",18))
            b.grid(row=2,column=2)
            window1.mainloop()
        else:
            tkinter.messagebox.showinfo("Alert","Select one")
    w=Tk()
    w.geometry("380x200") #width x height(small x)
    w.title("TOURS AND TRAVELS")
    w.configure(background="light green")
    l1=Label(w,text="Login page",bg='yellow' ,font=("Comic Sans MS",20))
    l1.grid(row=0,column=2)
    l2=Label(w,text="Select one:",bg='pink' ,font=("Comic Sans MS",15))
    l2.grid(row=1,column=2)
    v=IntVar()
    l3=Label(w,text="",padx=10,bg="light green")
    l3.grid(row=2,column=0)
    r1=Radiobutton(w,text="Admin",value=1,variable=v,bg='light blue' ,font=("Comic Sans MS",15))
    r1.grid(row=2,column=1)
    r2=Radiobutton(w,text="User",value=2,variable=v,bg='light blue' ,font=("Comic Sans MS",15))
    r2.grid(row=2,column=3)
    l4=Label(w,text="",padx=10,bg="light green")
    l4.grid(row=3,column=2)
    b=Button(w,text="Submit choice",command=res,fg="white",bg='teal' ,font=("Comic Sans MS",15))
    b.grid(row=4,column=2)
    w.mainloop()
    conn.commit()
except:
    tkinter.messagebox.showerror("Error","Some error occured")
finally:
    conn.commit()
    conn.close()