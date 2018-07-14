import tkinter as tk
import sqlite3 as sql
import turtle
import time

db = sql.connect('sqlhospitaldbms.db')
cur = db.cursor()
def create_db():
    sq = """create table if not exists patient(
          id  integer  primary key autoincrement not null,
          name  varchar(50) not null,
          section varchar(50) not null,
          email varchar(50) not null,
          doc integer not null
          ) """
    cur.execute(sq)


def create_db1():
    sq = """create table if not exists password(
          username  varchar(50)  primary key,
          password  varchar(50) not null
          

          ) """
    cur.execute(sq)


def create_db2():
    sq = """create table if not exists doctor(
          doc  integer  primary key autoincrement not null,
          name varchar(50) not null,
          specialization varchar(50) not null,
          email varchar(50) not null,
          pat int not null
          ) """
    cur.execute(sq)


def add_data():
    qo="None"
    def rset():
        q.set('')
        s.set('')

    def admit():
        global qo
        try:
            name1=name.get()
            section1=qo
            email1=email.get()
            z=[]
            z.append(section1)
            sqc="select * from doctor where specialization=? and pat<1"
            d=cur.execute(sqc,z)
            row=d.fetchone()
            print(row)
            docid=row[0]
                
            f=row[4]
            t=[]
            t.append(f+1)
            t.append(docid)
            sqr="update doctor set pat=? where doc=?"
            cur.execute(sqr,t)
            v = [name1,section1,email1,docid]
            sqq = "insert into patient(name,section,email,doc) values(?,?,?,?)"
            cur.execute(sqq, v)
            db.commit()
        except:
            root45=tk.Tk()
            lhu=tk.Label(root45,text="SORRY,DOCTOR IS NOT AVAILABLE!!!")
            lhu.pack()
            root45.mainloop()
    def heart():
        global qo
        qo="CARDIOLOGY"
    def lung():
        global qo
        qo="DENTIST"
    def ent():
        global qo
        qo="ENT"
    def icu():
        global qo
        qo="ICU"
    def cs():
        global qo
        qo="CHILD SPECIALIST"
    def gy():
        global qo
        qo="GYNAECOLOGY"
    def sg():
        global qo
        qo="SURGERY"
       
    def now():
        root5=tk.Tk()
        rt=tk.Button(root5,text="CARDIOLOGY",command=heart)
        rt.pack()
        rt2=tk.Button(root5,text="DENTIST",command=lung)
        rt2.pack()
        rt2=tk.Button(root5,text="ENT",command=ent)
        rt2.pack()
        rt2=tk.Button(root5,text="ICU",command=icu)
        rt2.pack()
        rt2=tk.Button(root5,text="CHILD SPECIALIST",command=cs)
        rt2.pack()
        rt2=tk.Button(root5,text="GYNAECOLOGY",command=gy)
        rt2.pack()
        rt2=tk.Button(root5,text="SURGERY",command=sg)
        rt2.pack()
        root5.mainloop()
    root3=tk.Tk()
    root3.geometry('800x800')
    root3.title('ADMIT PATIENT')
    root3.configure(background='cyan')
    f4=tk.Frame(root3,bg='cyan')
    lab=tk.Label(f4,text="ADMIT PATIENT",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    f4.pack()

    canvas1 = tk.Canvas(root3, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    
    p=tk.StringVar(root3)
    p.set('')
    q=tk.StringVar(root3)
    q.set('')
    r=tk.StringVar(root3)
    r.set('')
    s=tk.StringVar(root3)
    s.set('')
    w=tk.StringVar(root3)
    w.set('')
    f1=tk.Frame(root3,bg='cyan')
    name=tk.Entry(f1,textvariable=q)
    name.pack(side='right')
    az=tk.Label(f1,text="NAME",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    az.pack(side='right')
    f1.pack()
    f2=tk.Frame(root3,bg='cyan')
    ay=tk.Button(f2,text="SECTION",bg='cyan',command=now,font='TimesNewRoman 25',fg='yellow')
    ay.pack(side='right')
    f2.pack()
    f3=tk.Frame(root3,bg='cyan')
    email=tk.Entry(f3,textvariable=s)
    email.pack(side='right')
    at=tk.Label(f3,text="EMAIL",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    at.pack(side='right')
    f3.pack()
    f32=tk.Frame(root3,bg='cyan')
    but=tk.Button(f32,text="ADMIT",command=admit,font="TimesNewRoman 25 ",bg='yellow')
    but.pack(side='right')
    but3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    but3.pack(side='right')
    f32.pack()
    but4=tk.Button(root3,text="BACK",command=root3.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but4.pack()
    thout=tk.Label(root3,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thout.pack()
    root3.mainloop()
def add_data2():
    qw="None"
    def rset():
        q.set('')
        s.set('')

    def admit():
        global qw
        name1=name.get()
        section1=qw
        email1=email.get()
        pat=0
        v = [name1,section1,email1,pat]
        sqq = "insert into doctor(name,specialization,email,pat) values(?,?,?,?)"
        cur.execute(sqq, v)
        db.commit()   
    def heart():
        global qw
        qw="CARDIOLOGY"
    def lung():
        global qw
        qw="DENTIST"
    def ent():
        global qw
        qw="ENT"
    def icu():
        global qw
        qw="ICU"
    def cs():
        global qw
        qw="CHILD SPECIALIST"
    def gy():
        global qw
        qw="GYNAECOLOGY"
    def sg():
        global qw
        qw="SURGERY"
    def then():
        root5=tk.Tk()
        rt=tk.Button(root5,text="CARDIOLOGY",command=heart)
        rt.pack()
        rt2=tk.Button(root5,text="DENTIST",command=lung)
        rt2.pack()
        rt2=tk.Button(root5,text="ENT",command=ent)
        rt2.pack()
        rt2=tk.Button(root5,text="ICU",command=icu)
        rt2.pack()
        rt2=tk.Button(root5,text="CHILD SPECIALIST",command=cs)
        rt2.pack()
        rt2=tk.Button(root5,text="GYNAECOLOGY",command=gy)
        rt2.pack()
        rt2=tk.Button(root5,text="SURGERY",command=sg)
        rt2.pack()
        root5.mainloop()
    root3=tk.Tk()
    root3.geometry('800x800')
    root3.title('ADD DOCTOR')
    root3.configure(background='cyan')
    lab=tk.Label(root3,text="ADD DOCTOR",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    
    canvas1 = tk.Canvas(root3, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    
    
    p=tk.StringVar(root3)
    p.set('')
    q=tk.StringVar(root3)
    q.set('')
    r=tk.StringVar(root3)
    r.set('')
    s=tk.StringVar(root3)
    s.set('')
    w=tk.StringVar(root3)
    w.set('')
    f1=tk.Frame(root3,bg='cyan')
    name=tk.Entry(f1,textvariable=q)
    name.pack(side='right')
    at=tk.Label(f1,text="NAME",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    at.pack(side='right')
    f1.pack()
    f2=tk.Frame(root3,bg='cyan')
    
    ata=tk.Button(f2,text="SPECIALIZATION",command=then,bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ata.pack(side='right')
    f2.pack()
    f3=tk.Frame(root3,bg='cyan')
    email=tk.Entry(f3,textvariable=s)
    email.pack(side='right')
    atd=tk.Label(f3,text="EMAIL",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    atd.pack(side='right')
    f3.pack()
    f32=tk.Frame(root3,bg='cyan')
    but=tk.Button(f32,text="ADD",command=admit,font="TimesNewRoman 25 ",bg='yellow')
    but.pack(side='right')
    but3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    but3.pack(side='right')
    f32.pack()
    but4=tk.Button(root3,text="BACK",command=root3.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but4.pack()
    thout=tk.Label(root3,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thout.pack()
    root3.mainloop()

def add_data1():
    print("SIGNUP")
    try:
        username = (input("enter username"))
        password = (input("enter password"))
        name = (input("enter name"))
        v = []
    except:
        print("type mismatch")

    v.append(username)
    v.append(password)
    v.append(name)
    try:
        sq = "insert into password values(?,?,?)"
        d = cur.execute(sq, v)
        row = d.fetchone()
        db.commit()
        print("WELCOME ", name)
        main()
    except:
        db.rollback()
        print("Username already exists, try a different username")
        add_data1()


def dis():
    
    root2=tk.Tk()
    root2.geometry('800x800')
    root2.title('DISPLAY ALL PATIENTS')
    
    root2.configure(background='cyan')
    canvas1 = tk.Canvas(root2, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    lab=tk.Label(root2,text="PATIENT LIST",bg="white",font="TimesNewRoman 30 bold italic",fg="red")
    lab.pack()
    lab1=tk.Label(root2,text="===========================================================================================",width='700',height='1',bg='yellow')
    lab1.pack()
    lab2=tk.Label(root2,text="ID                  NAME                    SECTION                       EMAIL                  DOCID",bg='yellow',font="TimesNewRoman 10 bold",width='700',height='1')
    lab2.pack()
    lab3=tk.Label(root2,text="===========================================================================================",width='700',bg='yellow',font="TimesNewRoman 10 bold",height='1')
    lab3.pack()
    s=tk.StringVar()
    sq = "select * from patient"
    result = cur.execute(sq)
    d = result.fetchall()
    
    a=[]
    for j in range (len(d)):
        row=d[j]
        s=tk.StringVar()
        s.set(row[0])
        u=tk.StringVar()
        u.set(row[1])
        v=tk.StringVar()
        v.set(row[2])
        w=tk.StringVar()
        w.set(row[3])
        z=tk.StringVar()
        z.set(row[4])
        
        fr=tk.Frame(root2)
        
        lb=tk.Label(fr,textvariable=s,width='12',font='25',bg='yellow')
        lb.pack(side='left')
        lb1=tk.Label(fr,textvariable=u,width='14',font='25',bg='yellow')
        lb1.pack(side='left')
        lb2=tk.Label(fr,textvariable=v,width='14',font='25',bg='yellow')
        lb2.pack(side='left')
        lb3=tk.Label(fr,textvariable=w,width='14',font='25',bg='yellow')
        lb3.pack(side='left')
        lb4=tk.Label(fr,textvariable=z,width='14',font='25',bg='yellow')
        lb4.pack(side='left')
        fr.pack()
        
    root2.mainloop()    
    
def dis2():
    
    root2=tk.Tk()
    root2.geometry('800x800')
    root2.title('DISPLAY ALL DOCTORS')
    root2.configure(background='cyan')
    top=tk.Frame(root2,bg='cyan')
    scroll=tk.Scrollbar(top)
    canvas1 = tk.Canvas(root2, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    lab=tk.Label(root2,text="DOCTOR LIST",bg="white",font="TimesNewRoman 30 bold italic",fg="red")
    lab.pack()
    lab1=tk.Label(root2,text="===========================================================================================",width='700',height='1',bg='yellow')
    lab1.pack()
    lab2=tk.Label(root2,text="                     ID                        NAME                SPECIALIZATION              EMAIL          NO. OF PATIENTS ASSIGNED",bg='yellow',font="TimesNewRoman 10 bold",width='700',height='1')
    lab2.pack()
    lab3=tk.Label(root2,text="===========================================================================================",width='700',height='1',bg='yellow')
    lab3.pack()
    
    s=tk.StringVar()
    sq = "select * from doctor"
    result = cur.execute(sq)
    d = result.fetchall()
    
    a=[]
    for j in range(len(d)):
        row=d[j]
        s=tk.StringVar()
        s.set(row[0])
        u=tk.StringVar()
        u.set(row[1])
        v=tk.StringVar()
        v.set(row[2])
        w=tk.StringVar()
        w.set(row[3])
        q=tk.StringVar()
        q.set(row[4])
        
        
        fr=tk.Frame(root2)
        
        lb=tk.Label(fr,textvariable=s,width='14',font='25',bg='yellow')
        lb.pack(side='left')
        lb1=tk.Label(fr,textvariable=u,width='14',font='25',bg='yellow')
        lb1.pack(side='left')
        lb2=tk.Label(fr,textvariable=v,width='14',font='25',bg='yellow')
        lb2.pack(side='left')
        lb3=tk.Label(fr,textvariable=w,width='14',font='25',bg='yellow')
        lb3.pack(side='left')
        lb4=tk.Label(fr,textvariable=q,width='14',font='25',bg='yellow')
        lb4.pack(side='left')
        fr.pack()
    scroll.pack()
    top.pack()    
    root2.mainloop()    

def dis_roll():
    def rset():
        s.set('')

    def show():
        roll = roll1.get()
        roll=int(roll)
        x = [roll]
        sq = "select * from patient where id =?"
        d = cur.execute(sq, x)
        row = d.fetchone()
        if row != None:
            root5=tk.Tk()
            
            root5.geometry('800x800')
            root5.configure(background='cyan')
            canvas1 = tk.Canvas(root5, width = 200, height = 200)
            canvas1.pack()
            tu=turtle.RawTurtle(canvas1)
            tu.speed(0)
            tu.screen.bgcolor('white')
            tu.pensize(20)
            tu.color('red')
            tu.circle(30,280)
            tu.left(100)
            tu.color('pink')
            tu.pensize(22)
            tu.circle(30,300)
            tu.fd(300)
            tu.rt(140)
            tu.fd(300)
            
            s=tk.StringVar(root5)
            s.set(row[0])
            u=tk.StringVar(root5)
            u.set(row[1])
            v=tk.StringVar(root5)
            v.set(row[2])
            w=tk.StringVar(root5)
            w.set(row[3])
            y=tk.StringVar(root5)
            y.set(row[4])
            kl=tk.Label(root5,text="ID",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            kl.pack()
            ab=tk.Label(root5,textvariable=s,width='700',font='25',bg='yellow')
            ab.pack()
            k2=tk.Label(root5,text="NAME",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k2.pack()
            cd=tk.Label(root5,textvariable=u,width='700',font='25',bg='yellow')
            cd.pack()
            k3=tk.Label(root5,text="SECTION",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k3.pack()
            ef=tk.Label(root5,textvariable=v,width='700',font='25',bg='yellow')
            ef.pack()
            k4=tk.Label(root5,text="EMAIL",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k4.pack()
            gh=tk.Label(root5,textvariable=w,width='700',font='25',bg='yellow')
            gh.pack()
            k5=tk.Label(root5,text="DOCTOR ID",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k5.pack()
            ij=tk.Label(root5,textvariable=y,width='700',font='25',bg='yellow')
            ij.pack()
            
            thout=tk.Label(root5,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
            thout.pack()
            root5.mainloop()
    root4=tk.Tk()
    root4.geometry('800x800')
    root4.title('DISPLAY PATIENT DETAILS')
    root4.configure(background='cyan')
    lab=tk.Label(root4,text="PATIENT DETAILS",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    
    canvas1 = tk.Canvas(root4, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    
    s=tk.StringVar(root4)
    s.set('')
    f1=tk.Frame(root4,bg='cyan')
    roll1=tk.Entry(f1,textvariable=s)
    roll1.pack(side='right')
    ate=tk.Label(f1,text="PATIENT ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f1.pack()
    f32=tk.Frame(root4,bg='cyan')
    but=tk.Button(f32,text="SHOW",command=show,font="TimesNewRoman 25 ",bg='yellow')
    but.pack(side='right')
    but3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    but3.pack(side='right')
    f32.pack()
    but4=tk.Button(root4,text="BACK",command=root4.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but4.pack()
    thot=tk.Label(root4,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thot.pack()
    root4.mainloop()
def dis_roll2():
    def rset():
        s.set('')
        

    def show():
        roll = roll1.get()
        roll=int(roll)
        x = [roll]
        sq = "select * from doctor where doc =?"
        d = cur.execute(sq, x)
        row = d.fetchone()
        if row != None:
            root5=tk.Tk()
            
            root5.geometry('800x800')
            root5.configure(background='cyan')
            canvas1 = tk.Canvas(root5, width = 200, height = 200)
            canvas1.pack()
            tu=turtle.RawTurtle(canvas1)
            tu.speed(0)
            tu.screen.bgcolor('white')
            tu.pensize(20)
            tu.color('red')
            tu.circle(30,280)
            tu.left(100)
            tu.color('pink')
            tu.pensize(22)
            tu.circle(30,300)
            tu.fd(300)
            tu.rt(140)
            tu.fd(300)
            
            s=tk.StringVar(root5)
            s.set(row[0])
            u=tk.StringVar(root5)
            u.set(row[1])
            v=tk.StringVar(root5)
            v.set(row[2])
            w=tk.StringVar(root5)
            w.set(row[3])
            y=tk.StringVar(root5)
            y.set(row[4])
            kl=tk.Label(root5,text="ID",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            kl.pack()
            ab=tk.Label(root5,textvariable=s,width='700',font='25',bg='yellow')
            ab.pack()
            k2=tk.Label(root5,text="NAME",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k2.pack()
            cd=tk.Label(root5,textvariable=u,width='700',font='25',bg='yellow')
            cd.pack()
            k3=tk.Label(root5,text="SPECIALIZATION",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k3.pack()
            ef=tk.Label(root5,textvariable=v,width='700',font='25',bg='yellow')
            ef.pack()
            k4=tk.Label(root5,text="EMAIL",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k4.pack()
            gh=tk.Label(root5,textvariable=w,width='700',font='25',bg='yellow')
            gh.pack()
            k5=tk.Label(root5,text="NUMBER OF PATIENTS ASSIGNED",font='TimesNewRoman 25 ',fg='yellow',bg='cyan')
            k5.pack()
            ij=tk.Label(root5,textvariable=y,width='700',font='25',bg='yellow')
            ij.pack()
            thout=tk.Label(root5,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
            thout.pack()
            root5.mainloop()
    root4=tk.Tk()
    root4.geometry('800x800')
    root4.title('DISPLAY DOCTOR DETAILS')
    root4.configure(background='cyan')
    lab=tk.Label(root4,text="DOCTOR DETAILS",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    
    canvas1 = tk.Canvas(root4, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    
    s=tk.StringVar(root4)
    s.set('')
    f4=tk.Frame(root4,bg='cyan')
    roll1=tk.Entry(f4,textvariable=s)
    roll1.pack(side='right')
    ate=tk.Label(f4,text="DOCTOR ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f4.pack()
    f32=tk.Frame(root4,bg='cyan')
    but=tk.Button(f32,text="SHOW",command=show,font="TimesNewRoman 25 ",bg='yellow')
    but.pack(side='right')
    but3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    but3.pack(side='right')
    f32.pack()
    but4=tk.Button(root4,text="BACK",command=root4.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but4.pack()
    thot=tk.Label(root4,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thot.pack()
    root4.mainloop()

    

def dis_roll1():
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("==========================\n")
    print("Already a Member?")
    print("Y/N")
    ch = input()
    if ch.lower() == 'y':
        print("==========LOGIN============")
        usr = (input("enter username"))
        pss = (input("enter password"))
        x = [usr, pss]
        sq = "select * from password where username =? and password=?"
        d = cur.execute(sq, x)
        row = d.fetchone()
        if row != None:
            print("WELCOME ", row[2])
            main()
        else:
            print("Invalid Username and password ")
    else:

        add_data1()


def update():
    def rset():
        s.set('')
        
    
    def updt():
        def rset1():
            q.set('')
            r.set('')

        def updt1():
            n = lab1.get()
            m = lab2.get()
            
            roll=lab.get()
            roll=int(roll)
            x = []
            x.append(n)
            x.append(m)
            x.append(roll)
            sq = "update patient set name=?,email=? where id=?"
            cur.execute(sq, x)
            db.commit()
            
        roll = lab.get()
        v = [roll]
        d = cur.execute("select * from patient where id=?", v)
        row = d.fetchone()

        root8=tk.Tk()
        root8.geometry('800x800')
        root8.configure(background='cyan')
        labu=tk.Label(root8,text="ENTER NEW PATIENT DETAILS",bg="white",font="TimesNewRoman 40 bold italic",fg="red")
        labu.pack()
        canvas1 = tk.Canvas(root8, width = 200, height = 200)
        canvas1.pack()
        tu=turtle.RawTurtle(canvas1)
        tu.speed(0)
        tu.screen.bgcolor('white')
        tu.pensize(20)
        tu.color('red')
        tu.circle(30,280)
        tu.left(100)
        tu.color('pink')
        tu.pensize(22)
        tu.circle(30,300)
        tu.fd(300)
        tu.rt(140)
        tu.fd(300)

        r=tk.StringVar(root8)
        r.set('')
        q=tk.StringVar(root8)
        q.set('')
        fq1=tk.Frame(root8,bg='cyan')
        lab1=tk.Entry(fq1,textvariable=r)
        lab1.pack(side='right')
        q1=tk.Label(fq1,text="NAME",bg='cyan',fg='yellow',font="TimesNewRoman 25 ")
        q1.pack(side='right')
        fq1.pack()
        fq2=tk.Frame(root8,bg='cyan')
        lab2=tk.Entry(fq2,textvariable=q)
        lab2.pack(side='right')
        q12=tk.Label(fq2,text="EMAIL",bg='cyan',fg='yellow',font="TimesNewRoman 25 ")
        q12.pack(side='right')
        fq2.pack()
        we=tk.Frame(root8,bg='cyan')
        lat=tk.Button(we,text="UPDATE",command=updt1,bg='yellow',font="TimesNewRoman 25 ")
        lat.pack()
        we.pack()
        web=tk.Frame(root8,bg='cyan')
        but3=tk.Button(web,text="RESET",command=rset1,font="TimesNewRoman 25 ",bg='yellow')
        but3.pack()
        web.pack()
        but4=tk.Button(root8,text="BACK",command=root8.destroy,font="TimesNewRoman 25 ",bg='yellow')
        but4.pack()
        thout=tk.Label(root8,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
        thout.pack()
        root8.mainloop()
    root7=tk.Tk()
    root7.geometry('800x800')
    root7.title('UPDATE PATIENT DETAILS')
    root7.configure(background='cyan')
    labe=tk.Label(root7,text="UPDATE PATIENT DETAILS",bg="white",font="TimesNewRoman 40 bold italic",fg="red")
    labe.pack()
    
    canvas1 = tk.Canvas(root7, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    s=tk.StringVar(root7)
    s.set('')
    f4=tk.Frame(root7,bg='cyan')
    lab=tk.Entry(f4,textvariable=s)
    lab.pack(side='right')
    ate=tk.Label(f4,text="PATIENT ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f4.pack()
    f32=tk.Frame(root7,bg='cyan')
    la=tk.Button(f32,text="CONTINUE",command=updt,font="TimesNewRoman 25 ",bg='yellow')
    la.pack(side='right')
    bu3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    bu3.pack(side='right')
    f32.pack()
    but44=tk.Button(root7,text="BACK",command=root7.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but44.pack()
    thut=tk.Label(root7,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thut.pack()
    root7.mainloop()
def update2():
    def rset():
        s.set('')
        

    def updt():
        def rset1():
            q.set('')
            r.set('')

        def updt1():
            n = lab1.get()
            m = lab2.get()
            
            roll=lab.get()
            roll=int(roll)
            x = []
            x.append(n)
            x.append(m)
            
            
            x.append(roll)
            sq = "update doctor set name=?,email=? where doc=?"
            cur.execute(sq, x)
            db.commit()
            
        roll = lab.get()
        v = [roll]
        d = cur.execute("select * from doctor where doc=?", v)
        row = d.fetchone()

        root8=tk.Tk()
        root8.geometry('800x800')
        root8.title('UPDATE DOCTOR DETAILS')
        root8.configure(background='cyan')
        labu=tk.Label(root8,text="ENTER NEW DETAILS",bg="white",font="TimesNewRoman 40 bold italic",fg="red")
        labu.pack()
        canvas1 = tk.Canvas(root8, width = 200, height = 200)
        canvas1.pack()
        tu=turtle.RawTurtle(canvas1)
        tu.speed(0)
        tu.screen.bgcolor('white')
        tu.pensize(20)
        tu.color('red')
        tu.circle(30,280)
        tu.left(100)
        tu.color('pink')
        tu.pensize(22)
        tu.circle(30,300)
        tu.fd(300)
        tu.rt(140)
        tu.fd(300)

        s=tk.StringVar(root8)
        s.set('')
        r=tk.StringVar(root8)
        r.set('')
        q=tk.StringVar(root8)
        q.set('')
        p=tk.StringVar(root8)
        p.set('')
        fq1=tk.Frame(root8,bg='cyan')
        lab1=tk.Entry(fq1,textvariable=r)
        lab1.pack(side='right')
        q1=tk.Label(fq1,text="NAME",bg='cyan',fg='yellow',font="TimesNewRoman 25 ")
        q1.pack(side='right')
        fq1.pack()
        fq2=tk.Frame(root8,bg='cyan')
        lab2=tk.Entry(fq2,textvariable=q)
        lab2.pack(side='right')
        q12=tk.Label(fq2,text="EMAIL",bg='cyan',fg='yellow',font="TimesNewRoman 25 ")
        q12.pack(side='right')
        fq2.pack()
        lat=tk.Button(root8,text="UPDATE",command=updt1,font="TimesNewRoman 25 ",bg='yellow')
        lat.pack()
        but3=tk.Button(root8,text="RESET",command=rset1,font="TimesNewRoman 25 ",bg='yellow')
        but3.pack()
        but4=tk.Button(root8,text="BACK",command=root8.destroy,font="TimesNewRoman 25 ",bg='yellow')
        but4.pack()
        thout=tk.Label(root8,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
        thout.pack()
        root8.mainloop()
    root7=tk.Tk()
    root7.geometry('800x800')
    root7.configure(background='cyan')
    labe=tk.Label(root7,text="UPDATE DOCTOR DETAILS",bg="white",font="TimesNewRoman 40 bold italic",fg="red")
    labe.pack()
    
    canvas1 = tk.Canvas(root7, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    s=tk.StringVar(root7)
    s.set('')
    f4=tk.Frame(root7,bg='cyan')
    lab=tk.Entry(f4,textvariable=s)
    lab.pack(side='right')
    ate=tk.Label(f4,text="DOCTOR ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f4.pack()
    f32=tk.Frame(root7,bg='cyan')
    la=tk.Button(f32,text="CONTINUE",command=updt,font="TimesNewRoman 25 ",bg='yellow')
    la.pack(side='right')
    bt3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    bt3.pack(side='right')
    f32.pack()
    ut4=tk.Button(root7,text="BACK",command=root7.destroy,font="TimesNewRoman 25 ",bg='yellow')
    ut4.pack()
    thou=tk.Label(root7,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thou.pack()
    root7.mainloop()

def delete():
    def rset():
        s.set('')
        

    root6=tk.Tk()
    root6.geometry('800x800')
    root6.title('DISCHARGE PATIENT')
    root6.configure(background='cyan')
    lab=tk.Label(root6,text="DISCHARGE PATIENT",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    
    s=tk.StringVar(root6)
    s.set('')
    canvas1 = tk.Canvas(root6, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    f4=tk.Frame(root6,bg='cyan')
    lab=tk.Entry(f4,textvariable=s)
    lab.pack(side='right')
    ate=tk.Label(f4,text="PATIENT ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f4.pack()
    def dele():
        roll = lab.get()
        roll=int(roll)
        v = [roll]
        sqa="select * from patient where id=?"
        d=cur.execute(sqa,v)
        row=d.fetchone()
        x=[]
        x.append(row[4])
        b=row[4]
        sqw="select * from doctor where doc=?"
        d=cur.execute(sqw,x)
        row=d.fetchone()
        y=[]
        e=row[4]
        y.append(e-1)
        y.append(b)
        sqb="update doctor set pat=? where doc=?"
        cur.execute(sqb,y)
        sq = "delete from patient where id=?"
        cur.execute(sq, v)
        db.commit()
    f32=tk.Frame(root6,bg='cyan')    
    la=tk.Button(f32,text="DISCHARGE",command=dele,font="TimesNewRoman 25 ",bg='yellow')
    la.pack(side='right')
    b3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    b3.pack(side='right')
    f32.pack()
    but4=tk.Button(root6,text="BACK",command=root6.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but4.pack()
    thout=tk.Label(root6,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thout.pack()
    root6.mainloop()
def delete2():
    def rset():
        s.set('')

    root6=tk.Tk()
    root6.geometry('800x800')
    root6.title('DELETE DOCTOR')
    root6.configure(background='cyan')
    lab=tk.Label(root6,text="DELETE DOCTOR",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    
    s=tk.StringVar(root6)
    s.set('')
    canvas1 = tk.Canvas(root6, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    f4=tk.Frame(root6,bg='cyan')
    lab=tk.Entry(f4,textvariable=s)
    lab.pack(side='right')
    ate=tk.Label(f4,text="DOCTOR ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f4.pack()
    def dele():
        roll = lab.get()
        roll=int(roll)
        v = [roll]
        sq = "delete from doctor where doc=?"
        cur.execute(sq, v)
        db.commit()
    f32=tk.Frame(root6,bg='cyan')    
    la=tk.Button(f32,text="DELETE",command=dele,font="TimesNewRoman 25 ",bg='yellow')
    la.pack(side='right')
    but3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    but3.pack(side='right')
    f32.pack()
    but4=tk.Button(root6,text="BACK",command=root6.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but4.pack()
    thout=tk.Label(root6,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thout.pack()
    root6.mainloop()
def combine():
    def rset():

        s.set('')

    def go():
                    roll=lb.get()
                    roll=int(roll)
                    v=[roll]
                    sq="select * from patient where id=?"
                    d=cur.execute(sq,v)
                    row=d.fetchone()
                    b=row[4]
                    y=[b]
                    sqa="select * from doctor where doc=?"
                    d=cur.execute(sqa,y)
                    row=d.fetchone()
                           
                    root8=tk.Tk()
                    root8.geometry('800x800')
                    root8.configure(background='cyan')
                    lab=tk.Label(root8,text="DOCTOR DETAILS",bg="white",font="TimesNewRoman 30 bold italic",fg="red")
                    lab.pack()
    
                    canvas1 = tk.Canvas(root8, width = 200, height = 200)
                    canvas1.pack()
                    tu=turtle.RawTurtle(canvas1)
                    tu.speed(0)
                    tu.screen.bgcolor('white')
                    tu.pensize(20)
                    tu.color('red')
                    tu.circle(30,280)
                    tu.left(100)
                    tu.color('pink')
                    tu.pensize(22)
                    tu.circle(30,300)
                    tu.fd(300)
                    tu.rt(140)
                    tu.fd(300)
                    
                    s=tk.StringVar(root8)
                    s.set(row[0])
                    u=tk.StringVar(root8)
                    u.set(row[1])
                    v=tk.StringVar(root8)
                    v.set(row[2])
                    w=tk.StringVar(root8)
                    w.set(row[3])
                    f=tk.StringVar(root8)
                    f.set(row[4])
                    f1=tk.Frame(root8,bg='cyan')
                    ate=tk.Label(f1,text="PATIENT ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
                    ate.pack()
                    lbxq=tk.Label(f1,textvariable=s,font='25',bg='yellow')
                    lbxq.pack()
                    
                    f1.pack()
                    f2=tk.Frame(root8,bg='cyan')
                    ate=tk.Label(f2,text="NAME",bg='cyan',font='TimesNewRoman 25',fg='yellow')
                    ate.pack()
                    lbxo=tk.Label(f2,textvariable=u,font='25',bg='yellow')
                    lbxo.pack()
                    
                    f2.pack()
                    f3=tk.Frame(root8,bg='cyan')
                    
                    ate=tk.Label(f3,text="SPECIALIZATION",bg='cyan',font='TimesNewRoman 25',fg='yellow')
                    ate.pack()
                    lbxp=tk.Label(f3,textvariable=v,font='25',bg='yellow')
                    lbxp.pack()
                    
                    f3.pack()
                    f4=tk.Frame(root8,bg='cyan')
                    ate=tk.Label(f4,text="EMAIL",bg='cyan',font='TimesNewRoman 25',fg='yellow')
                    ate.pack()
                    f4.pack()
                    f5=tk.Frame(root8,bg='cyan')
                    lb4=tk.Label(f5,textvariable=w,font='25',bg='yellow')
                    lb4.pack()
                    ate=tk.Label(f5,text="NO. OF PATIENTS ASSIGNED",bg='cyan',font='TimesNewRoman 25',fg='yellow')
                    ate.pack()
                    lb1=tk.Label(f5,textvariable=f,font='25',bg='yellow')
                    lb1.pack()
                    
                    f5.pack()
                    but4=tk.Button(root8,text="BACK",command=root8.destroy,font="TimesNewRoman 10 ",bg='yellow')
                    but4.pack()
                    thout=tk.Label(root8,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 20 italic bold")
                    thout.pack()
                    root8.mainloop()  
              
    root9=tk.Tk()
    root9.geometry('800x800')
    root9.configure(background='cyan')
    lab=tk.Label(root9,text="SEARCH DOCTOR",bg="white",font="TimesNewRoman 50 bold italic",fg="red")
    lab.pack()
    
    canvas1 = tk.Canvas(root9, width = 200, height = 200)
    canvas1.pack()
    tu=turtle.RawTurtle(canvas1)
    tu.speed(0)
    tu.screen.bgcolor('white')
    tu.pensize(20)
    tu.color('red')
    tu.circle(30,280)
    tu.left(100)
    tu.color('pink')
    tu.pensize(22)
    tu.circle(30,300)
    tu.fd(300)
    tu.rt(140)
    tu.fd(300)
    
    s=tk.StringVar(root9)
    s.set('')
    f4=tk.Frame(root9,bg='cyan')
    lb=tk.Entry(f4,textvariable=s)
    lb.pack(side='right')
    ate=tk.Label(f4,text="PATIENT ID",bg='cyan',font='TimesNewRoman 25',fg='yellow')
    ate.pack(side='right')
    f4.pack()
    f32=tk.Frame(root9,bg='cyan')
    lbt=tk.Button(f32,text="SHOW",command=go,font="TimesNewRoman 25 ",bg='yellow')
    lbt.pack(side='right')
    b3=tk.Button(f32,text="RESET",command=rset,font="TimesNewRoman 25 ",bg='yellow')
    b3.pack(side='right')
    f32.pack()
    but41=tk.Button(root9,text="BACK",command=root9.destroy,font="TimesNewRoman 25 ",bg='yellow')
    but41.pack()
    thout=tk.Label(root9,text='"Always with you NOW THEN FOREVER"',fg='red',bg='cyan',font="Arial 29 italic bold")
    thout.pack()
    root9.mainloop()
def screen_2():
    def end():
        root100=tk.Tk()
        root1.destroy()
        lab=tk.Label(root100,text="THANK YOU , HOPE TO SEE YOU SOON")
        lab.pack()
        root100.mainloop()

    root1=tk.Tk()
    root.destroy()
    
    root1.geometry('500x800')
    root1.title('MENU')
    root1.configure(background='cyan')
    frame3=tk.Frame(root1,bg='cyan',width='1000')
    
    but1=tk.Button(root1,text="DISPLAY ALL PATIENTS",command=dis,font="TimesNewRoman 20 bold",bg='yellow')
    but1.pack()
    but2=tk.Button(root1,text="ADMIT PATIENT",command=add_data,font="TimesNewRoman 20 bold",bg='yellow')
    but2.pack()
    
    but3=tk.Button(root1,text="DISPLAY PATIENT DETAILS",command=dis_roll,font="TimesNewRoman 20 bold",bg='yellow')
    but3.pack()
    but4=tk.Button(root1,text="UPDATE PATIENT DETAILS",command=update,font="TimesNewRoman 20 bold",bg='yellow')
    but4.pack()
    
    but5=tk.Button(root1,text="DISCHARGE PATIENT",command=delete,font="TimesNewRoman 20 bold",bg='yellow')
    but5.pack()
    but7=tk.Button(root1,text="DISPLAY ALL DOCTORS",command=dis2,font="TimesNewRoman 20 bold",bg='yellow')
    but7.pack()
    
    but8=tk.Button(root1,text="ADD DOCTOR DETAILS",command=add_data2,font="TimesNewRoman 20 bold",bg='yellow')
    but8.pack()
    but9=tk.Button(root1,text="DISPLAY DOCTOR DETAILS",command=dis_roll2,font="TimesNewRoman 20 bold",bg='yellow')
    but9.pack()
    
    but10=tk.Button(root1,text="UPDATE DOCTOR DETAILS",command=update2,font="TimesNewRoman 20 bold",bg='yellow')
    but10.pack()
    but11=tk.Button(root1,text="DELETE DOCTOR DETAILS",command=delete2,font="TimesNewRoman 20 bold",bg='yellow')
    but11.pack()
    
    but12=tk.Button(root1,text="SEARCH DOCTOR FOR PATIENT",command=combine,font="TimesNewRoman 20 bold",bg='yellow')
    but12.pack()
    but6=tk.Button(root1,text="EXIT",command=end,font="TimesNewRoman 20 bold",bg='yellow')
    but6.pack()
    
    frame3.pack()
    
    root1.mainloop()

def signup():
     usr=usrname.get()

     pss=psswd.get()
     x = [usr, pss]
     try:   
        sq = "insert into password values(?,?) "
        d = cur.execute(sq, x)
        row = d.fetchone()
        db.commit()
        screen_2()
     except:
        db.rollback()
        root20=tk.Tk()
        luv=tk.Label(root20,text="Username already exists, try a different username")
        luv.pack()
        root20.mainloop()
        print("Username already exists, try a different username")
   
def reset():
    x.set('')
    y.set('')
def login():
    usr=usrname.get()
    pss=psswd.get()
    x = [usr, pss]
    sq = "select * from password where username =? and password=?"
    d = cur.execute(sq, x)
    row = d.fetchone()
    if row != None:
        screen_2()
    else:
        print("Invalid Login Credentials")

create_db1()
create_db()
create_db2()
root0=tk.Tk()
root0.geometry('800x800')
root0.configure(background='white')
but=tk.Label(root0,text="LIFE HOSPITALS",font="TimesNewRoman 45 bold italic",width='700',fg='red',bg='white')
but.pack()
canvas = tk.Canvas(root0, width = 600, height = 500)
canvas.pack()
t=turtle.RawTurtle(canvas)
t.screen.bgcolor('white')
t.pensize(20)
t.color('red')
t.circle(100,280)
t.left(100)
t.color('pink')
t.pensize(30)
t.circle(80,300)
t.fd(500)
t.rt(140)
t.fd(500)
bt=tk.Label(root0,text="WELCOME YOU",font="TimesNewRoman 45 bold italic",width='700',fg='red',bg='white')
bt.pack()
btu=tk.Button(root0,text="CLICK HERE TO CONTINUE",fg='black',command=root0.destroy)
btu.pack()
root0.mainloop()
root=tk.Tk()

root.geometry('800x800')
root.configure(background='cyan')
root.title('LOGIN PAGE')
canvas = tk.Canvas(root, width = 500, height = 350)
canvas.pack()
t=turtle.RawTurtle(canvas)
t.screen.bgcolor('white')
t.pensize(20)
t.speed(0)
t.color('red')
t.circle(65,280)
t.left(100)
t.color('pink')
t.pensize(30)
t.circle(50,300)
t.fd(300)
t.rt(140)
t.fd(300)

fm=tk.Frame(root,bg='cyan')
mssg=tk.Label(fm,bg="white",fg="red",text="LIFE HOSPITALS",width='700',font='TimesNewRoman 35 bold italic')
mssg.pack()
fm.pack()
x=tk.StringVar(root)
x.set('')
y=tk.StringVar(root)
y.set('')
frame1=tk.Frame(root,bg='cyan')
lab1=tk.Label(frame1,bg="cyan",text="USERNAME",font="TimesNewRoman 25 ",fg='yellow')
lab1.pack(side='left')
usrname=tk.Entry(frame1,textvariable=x,bg='white')
usrname.pack(side='left')
frame1.pack()
frame2=tk.Frame(root,bg='cyan')
lab2=tk.Label(frame2,bg="cyan",text="PASSWORD",font="TimesNewRoman 25 ",fg='yellow')
lab2.pack(side='left')
psswd=tk.Entry(frame2,show='*',textvariable=y,bg='white',)
psswd.pack(side='left')
frame2.pack()
frame3=tk.Frame(root)
but1=tk.Button(frame3,text="LOGIN",command=login,font="TimesNewRoman 25 ",bg='yellow')
but1.pack(side='right')
but2=tk.Button(frame3,text="RESET",command=reset,font="TimesNewRoman 25 ",bg='yellow')
but2.pack(side='right')
but3=tk.Button(frame3,text="SIGNUP",command=signup,font="TimesNewRoman 25 ",bg='yellow')
but3.pack(side='right')
frame3.pack()
root.mainloop()
    
