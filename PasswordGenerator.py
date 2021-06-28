import random
from tkinter import *
import string

def generate_password ():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbols = random.choice(string.punctuation)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(symbols)
        password.append(number)

        y = " ".join(str(x) for x in password)
        lbl.config(text = y)

root = Tk()
root.geometry("300x300")
btn = Button(root, text = "Generar Contraseña", command = generate_password)
btn.grid(row=2, column=2)
lbl = Label(root, font = ("Times",15,"bold"))
lbl.grid(row=4, column=2)
root.mainloop()
