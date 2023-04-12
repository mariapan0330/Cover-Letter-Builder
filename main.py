# do a python -m PyInstaller --onefile --windowed --icon=birb.ico --clean main.py in the console when you're done

from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
import os
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


def make_cover_letter(manager, role, company):
    # make a new canvas to draw on at the specified relative location, and with the A4 size.
    width,height=A4
    c = canvas.Canvas("./Cover Letters/Cover Letter.pdf", pagesize=A4)
    if manager == '':
        manager = "Hiring Manager"
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



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the widgets
        self.manager_label = QLabel("Hiring Manager (leave blank if unknown):")
        self.manager_input = QLineEdit()
        self.role_label = QLabel("Role:")
        self.role_input = QLineEdit()
        self.company_label = QLabel("Company:")
        self.company_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_info)
        self.submission_summary = QLabel(self)

        # Set the layout
        layout = QVBoxLayout()
        layout.setContentsMargins(100,100,100,100)
        layout.addWidget(self.manager_label)
        layout.addWidget(self.manager_input)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(self.company_label)
        layout.addWidget(self.company_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.submission_summary)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def submit_info(self):
        manager = self.manager_input.text().title()
        role = self.role_input.text()
        company = self.company_input.text()
        print(f"Manager: {manager}\nRole: {role}\nCompany: {company}")
        self.submission_summary.setText(f"SUBMITTED\nManager: {manager}\nRole: {role}\nCompany: {company}")
        make_cover_letter(manager, role, company)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())