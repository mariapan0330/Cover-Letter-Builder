# print('this is a test')
# inp = input("what is your name? ")
# print(inp)

# do a python -m PyInstaller --onefile --console main.py in the console when you're done

from reportlab.pdfgen import canvas

def hello(c):
    c.drawString(100,100,"Hello World")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()