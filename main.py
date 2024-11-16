from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculate")
root.geometry("700x530")

result_entry = Entry(root, font="Calibri 40")
result_entry.grid(row=1, column=1, columnspan=5, sticky='nsew', padx=6, pady=6, ipadx=15, ipady=23)

# def insert_1():
# result_entry.insert('end', '1')

btn1 = Button(root, text="1", command=lambda: result_entry.insert('end', '1'), bg='#83A6CE' ).grid(row=2, column=1, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
btn2 = Button(root, text="2", command=lambda: result_entry.insert('end', '2'), bg='#83A6CE' ).grid(row=2, column=2, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
btn3 = Button(root, text="3", command=lambda: result_entry.insert('end', '3'), bg='#83A6CE' ).grid(row=2, column=3, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)

btn4 = Button(root, text="4", command=lambda: result_entry.insert('end', '4'), bg='#83A6CE' ).grid(row=3, column=1, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
btn5 = Button(root, text="5", command=lambda: result_entry.insert('end', '5'), bg='#83A6CE' ).grid(row=3, column=2, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
btn6 = Button(root, text="6", command=lambda: result_entry.insert('end', '6'), bg='#83A6CE' ).grid(row=3, column=3, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)

btn7 = Button(root, text="7", command=lambda: result_entry.insert('end', '7'), bg='#83A6CE' ).grid(row=4, column=1, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
btn8 = Button(root, text="8", command=lambda: result_entry.insert('end', '8'), bg='#83A6CE' ).grid(row=4, column=2, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
btn9 = Button(root, text="9", command=lambda: result_entry.insert('end', '9'), bg='#83A6CE' ).grid(row=4, column=3, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)

btn0 = Button(root, text="0", command=lambda: result_entry.insert('end', '0'), bg='#83A6CE' ).grid(row=5,  column=1,columnspan=3, stick='we', padx=5, pady=5, ipadx=10, ipady=10)

btnDot = Button(root, text=".", command=lambda : result_entry.insert('end', '.'), bg="#7291B8").grid(row=6, column=3, columnspan=1, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=10)

def DelAll():
    result_entry.delete(0, 'end')

btnAc = Button(root, text="AC", command=DelAll, bg='#ED9E59').grid(row=6, column=1, columnspan=2, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=10)

def deleteNum():
    result_entry.delete((len(result_entry.get())-1),'end')

btnDel = Button(root, text="del", command=deleteNum, bg='#ED9E59').grid(row=6, column=4, columnspan=2, sticky='nsew', padx=5, pady=5, ipadx=10, ipady=10)

def Symbols(symbol):
    currentInput = result_entry.get()

    if(symbol in '+-*/'):
        if(currentInput[-1] in '+-*/'):
             return
            # currentInput = currentInput[:-1]
            # result_entry.delete(0, 'end')
            # result_entry.insert(0, currentInput)
    result_entry.insert('end', symbol)

BtnPlus = Button(root, text="+", command=lambda: Symbols('+'), bg='#D47F61').grid(row=2, column=4, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
BtnMinus = Button(root, text="-", command=lambda: Symbols('-'), bg='#D47F61').grid(row=3, column=4, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
BtnTimes = Button(root, text="*", command=lambda: Symbols('*'), bg='#D47F61').grid(row=2, column=5, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)
BtnDivide = Button(root, text="/", command=lambda: Symbols('/'), bg='#D47F61').grid(row=3, column=5, columnspan=1, stick='nsew', padx=5, pady=5, ipadx=10, ipady=10)

def Equal():
    result_calc = result_entry.get()
    result = eval(result_calc)
    #print(result)
    result_entry.delete(0, 'end')
    result_entry.insert(0, result)


BtnEquales = Button(root, text="=", command=Equal, bg='#4E769A').grid(row=4, column=4, columnspan=2, rowspan=2 , sticky='nsew', padx=5, pady=5, ipadx=6, ipady=6)

root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=2)
root.grid_columnconfigure(3, weight=2)
root.grid_columnconfigure(4, weight=2)
root.grid_columnconfigure(5, weight=2)

root.grid_rowconfigure(1, minsize=60)

def open_window():
    global color_entry

    color_window = Toplevel()
    color_window.title("Change color")
    color_window.geometry("300x200")

    color_label = Label(color_window, text="write color")
    color_label.pack()
    color_entry = Entry(color_window)
    color_entry.pack()

    Button(color_window, text="Apply Color", command=ApplyColors).pack()

def ApplyColors():
        color = color_entry.get()
        root['background'] = color



MainMenu = Menu(root)
root.config(menu=MainMenu)
#row -> ряд col -> колонки

ChangeColor = Menu(MainMenu, tearoff=0)
MainMenu.add_cascade(label="Setting Theme", menu=ChangeColor)
ChangeColor.add_command(label="Choose Color", command=open_window)
root.mainloop()