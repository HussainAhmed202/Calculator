from tkinter import *

root = Tk()
root.title('CALCULATOR')
root.geometry('300x300')
root.iconbitmap("icon.ico")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)


def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current+str(num))


def press_add():
    global f_num
    global operator

    first_num = e.get()
    operator = "add"
    f_num = float(first_num)
    e.delete(0, END)


def press_subtract():
    global f_num
    global operator

    first_num = e.get()
    operator = "subt"
    f_num = float(first_num)
    e.delete(0, END)


def press_mult():
    global f_num
    global operator

    first_num = e.get()
    operator = "mult"
    f_num = float(first_num)
    e.delete(0, END)


def press_div():
    global f_num
    global operator

    first_num = e.get()
    operator = "div"
    f_num = float(first_num)
    e.delete(0, END)


def press_equal():
    second_num = e.get()
    e.delete(0, END)
    if operator == "add":
        e.insert(0, f_num + float(second_num))

    elif operator == "subt":
        e.insert(0, f_num - float(second_num))

    elif operator == "mult":
        e.insert(0, f_num * float(second_num))
    else:
        e.insert(0, f_num / float(second_num))


def press_clear():
    e.delete(0, END)


zero = Button(root, text="0", command=lambda: button_click(0))
button_1 = Button(root, text="1", command=lambda: button_click(1))
button_2 = Button(root, text="2", command=lambda: button_click(2))
button_3 = Button(root, text="3", command=lambda: button_click(3))
button_4 = Button(root, text="4", command=lambda: button_click(4))
button_5 = Button(root, text="5", command=lambda: button_click(5))
button_6 = Button(root, text="6", command=lambda: button_click(6))
button_7 = Button(root, text="7", command=lambda: button_click(7))
button_8 = Button(root, text="8", command=lambda: button_click(8))
button_9 = Button(root, text="9", command=lambda: button_click(9))


add = Button(root, text="+", command=press_add)
add.grid(row=2, column=3, ipadx=20, ipady=35, rowspan=2, pady=(10, 0))

subt = Button(root, text="-", command=press_subtract)
subt.grid(row=1, column=3, ipady=10, ipadx=20, pady=(10, 0))

mult = Button(root, text="X", command=press_mult)
mult.grid(row=1, column=2, ipady=10, ipadx=20, pady=(10, 0))

div = Button(root, text="/", command=press_div)
div.grid(row=1, column=1, ipady=10, ipadx=20, pady=(10, 0))

equal = Button(root, text="=", command=press_equal)
equal.grid(row=4, column=3, rowspan=2, ipadx=20, ipady=35)


dot = Button(root, text=".", command=lambda: button_click("."))
dot.grid(row=5, column=2, ipady=10, ipadx=20)


clear = Button(root, text="CLS", command=press_clear)
clear.grid(row=1, column=0, ipadx=15, ipady=10, pady=(10, 0))

button_1.grid(row=4, column=0, ipadx=20, ipady=10)
button_2.grid(row=4, column=1, ipadx=20, ipady=10)
button_3.grid(row=4, column=2, ipadx=20, ipady=10)
button_4.grid(row=3, column=0, ipadx=20, ipady=10)
button_5.grid(row=3, column=1, ipadx=20, ipady=10)
button_6.grid(row=3, column=2, ipadx=20, ipady=10)
button_7.grid(row=2, column=0, ipadx=20, ipady=10)
button_8.grid(row=2, column=1, ipadx=20, ipady=10)
button_9.grid(row=2, column=2, ipadx=20, ipady=10)

zero.grid(row=5, column=0, ipadx=55, ipady=10, columnspan=2)


root.mainloop()