
from tkinter import Tk
from tkinter.ttk import Button
from tkinter import *
root=Tk
root= Tk()
root.title("Calculadora")
root.geometry('380x500')

display = Entry(root)
display.grid( padx=50,pady=20,row=1, columnspan=6, sticky=W+E)

i=0
def uso_numero (n):
    global i
    display.insert(i, n)
    i+=1

def operacion(operator):
    global i
    operator_lenght= len(operator)
    display.insert(i, operator)
    i+=operator_lenght

def borrartodo():
    display.delete(0, END)

def miniborrado():
    display_state= display.get()
    if len(display_state):
        display_new_state=display_state[:-1]
        borrartodo()
        display.insert(0, display_new_state)
    else:
        borrartodo()
        display.insert(0, "Error")

def resultado():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        borrartodo()
        display.insert(0,result)
    except:
        borrartodo()
        display.insert(0,"error")
#Buttons
Button(root, text="1", padx=25,pady=20, command=lambda:uso_numero(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", padx=25,pady=20, command=lambda:uso_numero(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", padx=25,pady=20, command=lambda:uso_numero(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", padx=25,pady=20, command=lambda:uso_numero(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", padx=25,pady=20, command=lambda:uso_numero(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", padx=25,pady=20, command=lambda:uso_numero(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", padx=25,pady=20, command=lambda:uso_numero(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", padx=25,pady=20, command=lambda:uso_numero(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", padx=15,pady=20, command=lambda:uso_numero(9)).grid(row=4, column=2, sticky=W+E)

#Buttons ayuda
Button(root, text="AC", padx=25,pady=20, command=lambda:borrartodo()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", padx=25,pady=20, command=lambda:uso_numero(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", padx=25,pady=20, command=lambda:operacion("%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", padx=15,pady=20, command=lambda:operacion("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", padx=15,pady=20, command=lambda:operacion("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", padx=15,pady=20, command=lambda:operacion("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", padx=15,pady=20, command=lambda:operacion("/")).grid(row=5, column=3, sticky=W+E)

Button(root, text="←", padx=15,pady=20,command=lambda:miniborrado()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", padx=15,pady=20, command=lambda:operacion("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", padx=15,pady=20, command=lambda:operacion("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", padx=15,pady=20, command=lambda:operacion("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", padx=15,pady=20, command=lambda:operacion(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", padx=15,pady=20,command=lambda:resultado()).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()