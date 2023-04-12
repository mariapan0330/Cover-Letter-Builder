# print('this is a test')
# inp = input("what is your name? ")
# print(inp)

# do a python -m PyInstaller --onefile --console main.py in the console when you're done

from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
import os

# identifies the w and h of the A4 document
width,height=A4

def make_cover_letter():
    # ask for the name of hiring manager
    manager = input("Hiring Manager (leave blank if unknown): ").title()
    if manager.lower() == 'q':
        return
    elif manager == '':
        manager = "Hiring Manager"

    # ask for the role title
    role= input("Role: ")
    while role == '':
        role = input("Invalid. Role: ")
    if role.lower() == 'q':
        return

    # ask for the company.
    company = input("Company: ")
    while company == '':
        company = input("Invalid. Company: ")
    if company.lower() == 'q':
        return

    # make a new canvas to draw on at the specified relative location, and with the A4 size.
    c = canvas.Canvas("./Cover Letters/Cover Letter.pdf", pagesize=A4)

    p1=Paragraph(f"""Dear {manager}, <br/><br/>

    I’m happy to see that the position of {role} is available at {company}! As a full-stack developer with experience in Java and Python, I am excited to put my skills to use maintaining and improving the user experience you have perfected. <br/><br/>

    My experience in full-stack development specializing in Python, JavaScript, SQL, PostgreSQL, Flask, and React makes me an ideal candidate for this role. I love the problem-solving process of learning new things and fine-tuning my skills, and I consistently ensure a thorough design that accounts for edge cases and provides an intuitive end-user experience. <br/><br/>

    I value the knowledge gained through diverse experiences, and I believe I provide a unique skill set to the teams you are building. I graduated from Trinity College Dublin with a BA in Psychology, with a minor in Sociology. I also had the opportunity to travel in Europe as an international student and to practice public relations and communications in my position as the PR officer in a college society. <br/><br/>

    These experiences, along with my coding experience and personal projects leave me in an optimal position to both learn from my participation and benefit your team at {company}. <br/><br/>

    Sincerely,<br/>
    Maria Panagos
    """)
    p1.wrapOn(c,500,450)
    p1.drawOn(c,width-550,height-290)

    c.save()

os.system('cls')
print("=======================================================")
print("\n********** WELCOME TO THE COVER LETTER MAKER **********\n")
print("=======================================================")
doQuit = input("Enter (q) to quit at any time. Enter (any) key to continue: ").lower()
while doQuit != 'q':
    make_cover_letter()
    print("==========\nThanks for using the Cover Letter Maker.")
    doQuit = input("Enter (q) to quit at any time. Enter (any) key to continue: ").lower()
    if doQuit == 'q':
        break
    os.system('cls')