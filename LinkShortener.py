import pyshorteners

link = input("Ingresa el link: ")
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print(x)
