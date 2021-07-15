from tkinter import *

import tkinter.font as font

root = Tk()

root.title("Calculator")

root.iconbitmap('C:/Users/HP/Desktop/cal.ico')

root.configure(bg='Grey')   #colouring whole background

myFont = font.Font(family='Comic Sans MS', size=20, weight = "bold") #creating the size and style of font

input = StringVar()            #converting data into string

e = Entry(root, text =  input, font=('Comic Sans MS', 20), width=25, borderwidth = 20, justify = RIGHT, bg = "Silver", fg = "Green")
e.grid(row=0, column=0, columnspan= 4,  ipady = 20)                  #ipady to increase the size of text box

val = ""            #passed null in val

def onClick(num):
    global val          #to store value
    val = val+str(num)  #if the value is not given
    input.set(val)

def onClear():
    global val
    val = ""
    input.set("")

def onEqual():
    global val
    output = str(eval(val))     #eval function evaluates the value
    input.set(output)


#Button desigining for input
button_C = Button(root, text = "C", padx = 200, pady = 10, bg = "Black", fg = "Silver", command = onClear)
button_C['font'] = myFont #using created font
button_C.grid(row = 1, column = 0, columnspan = 4)

button_7 = Button(root, text = "7", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(7))
button_7['font'] = myFont
button_7.grid(row = 2, column = 0)

button_8 = Button(root, text = "8", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(8))
button_8['font'] = myFont
button_8.grid(row = 2, column = 1)

button_9 = Button(root, text = "9", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(9))
button_9['font'] = myFont
button_9.grid(row = 2, column = 2)

button_div = Button(root, text = "÷", padx = 35, pady = 20, bg = "#00ffff", command=lambda: onClick("/"))
button_div['font'] = myFont
button_div.grid(row = 2, column = 3)

button_4 = Button(root, text = "4", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(4))
button_4['font'] = myFont
button_4.grid(row = 3, column = 0)

button_5 = Button(root, text = "5", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(5))
button_5['font'] = myFont
button_5.grid(row = 3, column = 1)

button_6 = Button(root, text = "6", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(6))
button_6['font'] = myFont
button_6.grid(row = 3, column = 2)

button_mul = Button(root, text = "x", padx = 35, pady = 20, bg = "#00ffff", command=lambda: onClick("*") )
button_mul['font'] = myFont
button_mul.grid(row = 3, column = 3)

button_1 = Button(root, text = "1", padx = 35, pady = 20, bg =  "silver", command=lambda: onClick(1))
button_1['font'] = myFont
button_1.grid(row = 4, column = 0)

button_2 = Button(root, text= "2", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(2))
button_2['font'] = myFont
button_2.grid(row = 4, column = 1)

button_3 = Button(root, text = "3", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(3))
button_3['font'] = myFont
button_3.grid(row = 4, column = 2)

button_sub = Button(root, text = "-", padx = 35, pady = 20, bg = "#00ffff", command=lambda: onClick("-"))
button_sub['font'] = myFont
button_sub.grid(row = 4, column = 3)

button_0 = Button(root, text = "0", padx = 35, pady = 20, bg = "Silver", command=lambda: onClick(0))
button_0['font'] = myFont
button_0.grid(row = 5, column = 0)

button_00 = Button(root, text = "00", padx = 26, pady = 20, bg = "Silver", command=lambda: [onClick(0), onClick(0)])
button_00['font'] = myFont
button_00.grid(row = 5, column = 1)

button_dot = Button(root, text = ".", padx = 37, pady = 20, bg = "Silver", command=lambda: onClick("."))
button_dot['font'] = myFont
button_dot.grid(row = 5, column = 2)

button_plus = Button(root, text = "+", padx = 35, pady = 20, bg = "#00ffff", command=lambda : onClick("+"))
button_plus['font'] = myFont
button_plus.grid(row = 5, column = 3)

button_result = Button(root, text = "=", padx = 200, pady = 10, fg = "Silver", bg = "Black", command= onEqual)
button_result['font']= myFont
button_result.grid(row = 6, column = 0, columnspan = 4)

root.mainloop()