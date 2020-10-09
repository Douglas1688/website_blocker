from tkinter import *
import tkinter as tk
from tkinter import messagebox

def limpiar():
    txtweb.delete(0,END)
    txtunlockweb.delete(0,END)


def block():

    hostspath = "C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    web = txtweb.get()
    with open(hostspath,"a+") as file:
        file.writelines(redirect+" "+web+"\n")
        messagebox.showinfo(message="Página Bloqueada",title="Bloqueo")

    limpiar()

def unlock():
    hostspath = "C:\Windows\System32\drivers\etc\hosts"
    web = txtunlockweb.get()
    with open(hostspath, "r+") as file:
        content = file.readlines()
        i=0
        for elem in content:
            if web in elem:
                del content[i]
                break
            else:
                i+=1
                continue
        file.close()
        new_file = open(hostspath,"w+")
        for elem in content:
            new_file.write(elem)
        new_file.close()
    messagebox.showinfo(message="Página desbloqueada",title="Unblock")
    limpiar()




def actualizarboton():
    text_list.config(state="normal")
    text_list.delete(1.0,END)
    redirect = "127.0.0.1 "
    cadena= []
    hostspath = "C:\Windows\System32\drivers\etc\hosts"
    """with open(hostspath, "r") as file:
        lines = file.readlines()
    for elem in lines:
        if elem == "\n":
            continue
        else:
            cadena.append(elem.lstrip(redirect).strip())"""
    with open(hostspath,"r") as file:
        text_list.insert(tk.INSERT, file.read())
    file.close()

    text_list.config(state="disable")

    text_list.pack()

root = Tk()
root.title("Bloqueador de Sitios Web")
root.geometry("400x400")
txtweb = Entry(root)
txtweb.pack()

btnweb = Button(root, text="Bloquear",command=block)
btnweb.pack()

txtunlockweb = Entry(root)
txtunlockweb.pack()

btnunlockweb = Button(root, text="Desbloquear",command=unlock)
btnunlockweb.pack()

text_list = Text(root, width=30, height=15)
text_list.config(state="disable")
text_list.pack()


btn_actualizar = Button(root,text="Actualizar",command=actualizarboton)
btn_actualizar.pack()

root.mainloop()
