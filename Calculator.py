from tkinter import *
root = Tk()

e = Entry(root, borderwidth=4, bg="black", fg="yellow", width=48)
e.grid(column=1, row=1,  columnspan=4)
e.configure(font=("Times New Roman", 18))
null1=Label(root, width=1)
null1.grid(row=3, column=0)

def numberDisplay(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def buttonMultiply():
    firstNumber = e.get()
    global fNum
    fNum = int(firstNumber) #global variable we can use outside of function
    e.delete(0, END)

def buttonEqual():
    secondNumber = e.get()
    e.delete(0, END)
    e.insert(0, fNum * int(secondNumber))


button0 = Button(root, pady=40, padx=70, text="0", bg="yellow", command=lambda: numberDisplay(0))
clearButton = Button(root, text="clear", padx=34, pady=40, bg="black", fg="yellow", command=buttonClear)
multiplyButton = Button(root, text="X", padx=67, pady=40, bg="black", fg="yellow", command=buttonMultiply)
equalButton = Button(root, text="=", padx=268, pady=25, bg="black", fg="yellow", command=buttonEqual)

button1 = Button(root, text="1", pady=40, padx=73, bg="yellow", command=lambda: numberDisplay(1))
button2 = Button(root, text="2", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(2))
button3 = Button(root, text="3", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(3))

button4 = Button(root, text="4", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(4))
button5 = Button(root, text="5", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(5))
button6 = Button(root, text="6", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(6))

button7 = Button(root, text="7", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(7))
button8 = Button(root, text="8", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(8))
button9 = Button(root, text="9", pady=40, padx=70, bg="yellow", command=lambda: numberDisplay(9))



#placing el buttons
button0.grid(row=6, column=2)
clearButton.grid(row=6, column=3)
multiplyButton.grid(row=6, column=1)
equalButton.grid(row=7, column=1, columnspan=3)

button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)

button4.grid(row=4, column=1)
button5.grid(row=4, column=2)
button6.grid(row=4, column=3)

button7.grid(row=5, column=1)
button8.grid(row=5, column=2)
button9.grid(row=5, column=3)


button0.configure(font=("Comic Sans MS", 30))
clearButton.configure(font=("Comic Sans MS", 30))
multiplyButton.configure(font=("Comic Sans MS", 30))
equalButton.configure(font=("Comic Sans MS", 30))

button1.configure(font=("Comic Sans MS", 30))
button2.configure(font=("Comic Sans MS", 30))
button3.configure(font=("Comic Sans MS", 30))

button4.configure(font=("Comic Sans MS", 30))
button5.configure(font=("Comic Sans MS", 30))
button6.configure(font=("Comic Sans MS", 30))

button7.configure(font=("Comic Sans MS", 30))
button8.configure(font=("Comic Sans MS", 30))
button9.configure(font=("Comic Sans MS", 30))


root.mainloop()