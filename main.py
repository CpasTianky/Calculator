import re
from PyQt6.QtWidgets import *
import sys

""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked!")

app = QApplication(sys.argv)
    
window = MainWindow()
window.show()

app.exec() """
welcome = "Welcome to my fantastic calculator !"
rep = 'y'
while rep == 'y':
    print(welcome)
    x = input("Enter an operation \n")
    num = re.split('[+|-]', x)
    opp = x[len(num[0])]

    match opp:
        case '+':
            res = int(num[0]) + int(num[1])
        case '-':
            res = int(num[0]) - int(num[1])
        case '/':
            res = int(num[0]) / int(num[1])
        case 'x':
            res = int(num[0]) . int(num[1])
    print(res)

    rep = input("Again ? y/n \n")