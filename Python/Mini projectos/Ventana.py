import tkinter as tk
ventana=tk.Tk()
ventana.title("Calculadora")
#anchoxalto
ventana.geometry('380x500')
ventana.configure(background='turquoise')
etiqueta1=tk.Label(ventana,text="Calculadora estandar",bg="black",fg="white")
etiqueta1.pack(ipady=20)
etiqueta1.pack(fill=tk.X)
etiqueta2=tk.Label(ventana,text="Izquierda",bg="white",fg="black")
etiqueta2.pack(padx=20,pady=20,ipadx=20,ipady=20)
etiqueta2.pack(side=tk.LEFT)
etiqueta3=tk.Label(ventana,text="Derecha",bg="white",fg="black")
etiqueta3.pack(padx=20,pady=20,ipadx=20,ipady=20)
etiqueta3.pack(side=tk.RIGHT)



ventana.mainloop()