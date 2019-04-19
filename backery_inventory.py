from Tkinter import *
import sqlite3
from tkMessageBox import *
#() Tuple
#[] List
#[(,,,),(a,b,v)]
root =Tk()
root.title('Bakery Inventory')
global e1,e2
z11=showinfo(title="Info Box",message="Hello owner!Welcome to Bakery Inventory ")
z12=showinfo(title="Info Box",message="Please note that you can only add a single name to an item.It means that no items can have two names as the item name is the primary key and has its unique identity.Thus if you add another item with the same name it will not be accepted and thus it could not be inserted.So be careful on adding the entry box of the item name and ensure whever you add a new item its name name should not be existing previously.THANK YOU ")
z13=showinfo(title="Info Box",message="Please note that you can update and search any item only by its name which you have inserted.So in the entry boxes above Update and Search button only type the name of the item inserted earlier.THANK YOU!")
z11=showinfo(title="Info Box",message="For further queries you can click on HELP button and even if you dont find them solved their you can mail me at abhishektrivedi1997@gmail.com.")
con=sqlite3.Connection("inventory")
cur=con.cursor()
cur.execute("create table if not exists inventory2(iname varchar(10) primary key,ln int, id int )")
def delete():
    con.close()
def insertar():
    a1=a.get()
    b1=float(b.get())
    c1=float(c.get())
    cur.execute("insert into inventory2 values(?,?,?)",(a1,b1,c1))
    if c1<=10:
        d=showinfo(title="Alert Box",message="This item is less.Please add it soon")
    s=showinfo(title="Alert Box",message="Items are successfully addded")
    con.commit()
def listar():
    s5=showinfo(title="Alert Box",message="Click the LOAD button twice to see the items in the new window!Dont notice this message after clicking LOAD button for the second time")
    widget=Tk()
    widget.title("Stored DATA")
    widget.configure(background="yellow")
    var=cur.fetchall()
    cur.execute('SELECT * FROM inventory2')
    Label(widget,text="ITEM               COST              NUMBER",bg="POWDER BLUE",fg="BLUE").grid(row=0)
    Button(widget,text="ITEMS ALERT",bg="powder blue", fg="black", bd=4,command=messagebox).grid(row=1)
    print len(var)
    j=0
    while j< len(var):
        print var[j]
        Label(widget,text=var[j],fg="black",bd=6,font="20").grid(row=j+2)
        j=j+1
def messagebox():
    mg=Tk()
    mg.title("Item Status")
    connection=sqlite3.connect("inventory")
    cursor=connection.cursor()
    cursor.execute('SELECT iname,id FROM inventory2 where id<=10')
    var1=cursor.fetchall()
    if var1==None:
        s1=showinfo(title="Alert Box",message="There are no items which are less than 10")
    Label(mg,text="Note:The numeric value is the no.of items left which are less than 10",fg="red",font="16").grid(row=0)
    r=0
    while r< len(var1):
        print var1[r]
        Label(mg,text=var1[r],fg="green",font="13").grid(row=r+2)
        r=r+1
    s=showinfo(title="Alert Box",message="get them soon")
def box():
    global e1,e2
    widget2=Tk()
    widget2.title("Update Screen")
    widget2.configure(background="pink")
    Label(widget2,text="enter price of item to be updated").grid(row=0)
    e1=Entry(widget2)
    e1.grid(row=1,column=1)
    Label(widget2,text="enter no. of items to be added which is updated").grid(row=2)
    e2=Entry(widget2)
    e2.grid(row=3,column=1)
    Button(widget2, text='Add Now',bg="powder blue", fg="black", bd=4,command=update).grid(row =5, column=1, columnspan=4,
    sticky='w')     #   if i <3:
def update():
    global e1,e2
    z=e.get()
    x=float(e1.get())
    y=float(e2.get())
    try:
        cur.execute('delete from inventory2 where iname=?',(z,))
        cur.execute("insert into inventory2 values(?,?,?)",(z,x,y))
        print cur.fetchall()
        con.commit()
    except sqlite3.OperationalError as message:
        em=message.args[0]
        showerror("error",em)
    s4=showinfo(title="Alert Box",message="Your item is added .Now close this window and you can check")
    #delete * from inventory where iname=?
    #insert ...............
def search():                             #("SELECT * FROM addresses WHERE FIRST_NAME = ? ",t)
    yo=Tk()
    yo.title("Searched Item")
    r=str()
    r=d.get()
    connection=sqlite3.connect("inventory")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM inventory2 where iname=?',(r,))
    var2=cursor.fetchall()
    print len(var2)
    i=0
    Label(yo,text="the item info is ",bg="red",fg="white",font="40").grid(row=0)
    while i< len(var2):
        print var2[i]
        Label(yo,text="Note:The first entry displayed is item name",fg="blue",font="40").grid(row=1)
        Label(yo,text="Note:The second entry displayed is item price",fg="blue",font="40").grid(row=2)
        Label(yo,text="Note:The third entry displayed is item no.of items present",fg="blue",font="40").grid(row=3)
        Label(yo,text=var2[i],fg="red",font="40").grid(row=5)
        i=i+1
def reset():
    s2=showinfo(title="Alert Box",message="Fill your items again now")
    cur.execute("DROP TABLE inventory2")
    cur.execute("CREATE TABLE IF NOT EXISTS inventory2(iname varchar(10) primary key,ln int, id int )")
    con.commit()
def Help():
    s8=showinfo(title="Alert Box",message="Click on INSERT button to insert the item name,item price in Rs. and the no.of items to be added.Click on LOAD to display all the items that are added.Click on RESET to remove sll the entries added and start adding items in empty fresh table,Click on UPDATE to change information regarding any item.Click on SEARCH to find the information regarding any item by typing itemname in the entrybox")
def onclick1(x):
    a.insert(25,x)
def onclick2(y):
    b.insert(25,y)
def onclick3(z):
    c.insert(25,z)
def press1():
    root2=Tk()
    root2.title("Ename enter")
    Button(root2,text="q",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('q')).grid(row=12,column=7,sticky=N+W+S+E)
    Button(root2,text="w",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('w')).grid(row=12,column=8,sticky=N+W+S+E)
    Button(root2,text="e",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('e')).grid(row=12,column=9,sticky=N+W+S+E)
    Button(root2,text="r",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('r')).grid(row=12,column=10,sticky=N+W+S+E)
    Button(root2,text="t",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('t')).grid(row=12,column=11,sticky=N+W+S+E)
    Button(root2,text="y",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('y')).grid(row=12,column=12,sticky=N+W+S+E)
    Button(root2,text="u",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('u')).grid(row=12,column=13,sticky=N+W+S+E)
    Button(root2,text="i",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('i')).grid(row=12,column=14,sticky=N+W+S+E)
    Button(root2,text="o",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('o')).grid(row=12,column=15,sticky=N+W+S+E)
    Button(root2,text="p",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('p')).grid(row=12,column=16,sticky=N+W+S+E)
    Button(root2,text="7",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('7')).grid(row=12,column=17,sticky=N+W+S+E)
    Button(root2,text="8",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('8')).grid(row=12,column=18,sticky=N+W+S+E)
    Button(root2,text="9",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('9')).grid(row=12,column=19,sticky=N+W+S+E)
    Button(root2,text="a",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('a')).grid(row=13,column=7,sticky=N+W+S+E)
    Button(root2,text="s",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('s')).grid(row=13,column=8,sticky=N+W+S+E)
    Button(root2,text="d",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('d')).grid(row=13,column=9,sticky=N+W+S+E)
    Button(root2,text="f",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('f')).grid(row=13,column=10,sticky=N+W+S+E)
    Button(root2,text="g",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('g')).grid(row=13,column=11,sticky=N+W+S+E)
    Button(root2,text="h",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('h')).grid(row=13,column=12,sticky=N+W+S+E)
    Button(root2,text="j",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('j')).grid(row=13,column=13,sticky=N+W+S+E)
    Button(root2,text="k",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('k')).grid(row=13,column=14,sticky=N+W+S+E)
    Button(root2,text="l",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('l')).grid(row=13,column=15,sticky=N+W+S+E)
    Button(root2,text="-",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('-')).grid(row=13,column=16,sticky=N+W+S+E)
    Button(root2,text="4",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('4')).grid(row=13,column=17,sticky=N+W+S+E)
    Button(root2,text="5",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('5')).grid(row=13,column=18,sticky=N+W+S+E)
    Button(root2,text="6",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('6')).grid(row=13,column=19,sticky=N+W+S+E)
    Button(root2,text="z",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('z')).grid(row=14,column=7,sticky=N+W+S+E)
    Button(root2,text="x",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('x')).grid(row=14,column=8,sticky=N+W+S+E)
    Button(root2,text="c",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('c')).grid(row=14,column=9,sticky=N+W+S+E)
    Button(root2,text="v",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('v')).grid(row=14,column=10,sticky=N+W+S+E)
    Button(root2,text="b",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('b')).grid(row=14,column=11,sticky=N+W+S+E)
    Button(root2,text="n",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('n')).grid(row=14,column=12,sticky=N+W+S+E)
    Button(root2,text="m",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('m')).grid(row=14,column=13,sticky=N+W+S+E)
    Button(root2,text=",",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1(',')).grid(row=14,column=14,sticky=N+W+S+E)
    Button(root2,text=".",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('.')).grid(row=14,column=15,sticky=N+W+S+E)
    Button(root2,text="/",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('/')).grid(row=14,column=16,sticky=N+W+S+E)
    Button(root2,text="1",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('1')).grid(row=14,column=17,sticky=N+W+S+E)
    Button(root2,text="2",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('2')).grid(row=14,column=18,sticky=N+W+S+E)
    Button(root2,text="3",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick1('3')).grid(row=14,column=19,sticky=N+W+S+E)
def press2():
    root1=Tk()
    root1.title("Price enter")
    Button(root1,text="7",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('7')).grid(row=16,column=7,sticky=N+W+S+E)
    Button(root1,text="8",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('8')).grid(row=16,column=8,sticky=N+W+S+E)
    Button(root1,text="9",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclickw('9')).grid(row=16,column=9,sticky=N+W+S+E)
    Button(root1,text="4",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('4')).grid(row=17,column=7,sticky=N+W+S+E)
    Button(root1,text="5",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('5')).grid(row=17,column=8,sticky=N+W+S+E)
    Button(root1,text="6",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('6')).grid(row=17,column=9,sticky=N+W+S+E)
    Button(root1,text="1",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('1')).grid(row=18,column=7,sticky=N+W+S+E)
    Button(root1,text="2",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('2')).grid(row=18,column=8,sticky=N+W+S+E)
    Button(root1,text="3",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('3')).grid(row=18,column=9,sticky=N+W+S+E)
    Button(root1,text="/",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('/')).grid(row=19,column=7,sticky=N+W+S+E)
    Button(root1,text="0",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('0')).grid(row=19,column=8,sticky=N+W+S+E)
    Button(root1,text=".",width=5,height=3,bg="black",fg="powder blue",command=lambda :onclick2('.')).grid(row=19,column=9,sticky=N+W+S+E)
def press3():
    root3=Tk()
    root3.title("Quantity Enter")
    Button(root3,text="7",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('7')).grid(row=21,column=7,sticky=N+W+S+E)
    Button(root3,text="8",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('8')).grid(row=21,column=8,sticky=N+W+S+E)
    Button(root3,text="9",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('9')).grid(row=21,column=9,sticky=N+W+S+E)
    Button(root3,text="4",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('4')).grid(row=22,column=7,sticky=N+W+S+E)
    Button(root3,text="5",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('5')).grid(row=22,column=8,sticky=N+W+S+E)
    Button(root3,text="6",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('6')).grid(row=22,column=9,sticky=N+W+S+E)
    Button(root3,text="1",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('1')).grid(row=23,column=7,sticky=N+W+S+E)
    Button(root3,text="2",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('2')).grid(row=23,column=8,sticky=N+W+S+E)
    Button(root3,text="3",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('3')).grid(row=23,column=9,sticky=N+W+S+E)
    Button(root3,text="/",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('/')).grid(row=24,column=7,sticky=N+W+S+E)
    Button(root3,text="0",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('0')).grid(row=24,column=8,sticky=N+W+S+E)
    Button(root3,text=".",width=6,height=3,bg="black",fg="powder blue",command=lambda :onclick3('.')).grid(row=24,column=9,sticky=N+W+S+E)
Label(root,text="Type the name of the item to be added ",fg="black",bd=6).grid(row=0,column=0,sticky='e')
a=Entry(root)
a.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)
Label(root,text="Type the price of the item to be added",fg="black",bd=6).grid(row=1,column=0,sticky='e')
b=Entry(root)
b.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=9)
Label(root,text="Type the quantity of the item to be added      ",fg="black",bd=6).grid(row=2,column=0,sticky='e')
c=Entry(root)
c.grid(row=2,column=1,padx=2,pady=2,sticky='we',columnspan=9)
Button(root, text="Insert",bg="powder blue", fg="black", bd=4,command=insertar).grid(row=0, column=10, sticky='ew', padx=2,
pady=2)
Button(root, text="Load",bg="powder blue", fg="black", bd=4,command=listar).grid(row=1, column=10, sticky='ew', padx=2)
Button(root, text="Close DBMS", bg="powder blue", fg="black", command=delete).grid(row=2, column=10, sticky='ew', padx=2)
Button(root, text="Reset",bg="powder blue", fg="black", bd=4,command=reset).grid(row=3, column=10, sticky='ew',
padx=2)
d=Entry(root)
d.grid(row =5, column=1,
columnspan=6, sticky='w')
Button(root, text='Search',bg="powder blue", fg="black", bd=4,command=search).grid(row =7, column=1, columnspan=4,
sticky='w')
e=Entry(root)
e.grid(row =5, column=8,
columnspan=6, sticky='w')
Button(root, text='Update',bg="powder blue", fg="black", bd=4,command=box).grid(row =7, column=7, columnspan=4,
sticky='w')
Label(root, text='Enter the name of the item to be updated in the entry box above update button',bg="powder blue", fg="black", bd=4).grid(row=3, column=6,
sticky='w')
Label(root, text="To activate ONSCREE KEYBOARD for typing the NAME of the item to be added PRESS the button below",fg="black",bd=6).grid(row=10, column=6, sticky='w')
Button(root,text="Press Button",bg="powder blue", fg="black", bd=4,command=press1).grid(row=11,column=6)
Label(root, text="To activate ONSCREEN KEYBOARD for typing the PRICE of the item added PRESS the button below",fg="black",bd=6).grid(row=12, column=6, sticky='w')
Button(root,text="Press Button",bg="powder blue", fg="black", bd=4,command=press2).grid(row=13,column=6)
Label(root, text="To activate ONSCREEN KEYBOARD for typing the NO. of items added PRESS the button below",fg="black",bd=6).grid(row=14, column=6, sticky='w')
Button(root,text="Press Button",bg="powder blue", fg="black", bd=4,command=press3).grid(row=15,column=6)
Button(root,text="Help",bg="powder blue", fg="black", bd=4,command=Help).grid(row=17)
root.mainloop()
