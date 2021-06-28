import tkinter as tk
import qrcode

root = tk.Tk()
root.geometry("400x240")

# Creamos un objeto código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)


def getTextInput():
    result = textExample.get(1.0, tk.END+"-1c")
    print(result)
    # Agregamos la información
    qr.add_data(result)
    qr.make(fit=True)

    # Creamos una imagen para el objeto código QR
    imagen = qr.make_image()

    # Guardemos la imagen con la extension que queramos
    imagen.save('qr.png')

textExample = tk.Text(root, height=10)
textExample.pack()
btnRead = tk.Button(root, height=1, width=10, text="Read", command=getTextInput)

btnRead.pack()
root.mainloop()




