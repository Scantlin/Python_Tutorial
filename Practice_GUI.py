from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("Hello world")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Hello World")
    win.setGeometry(200,200,300,300)

    label = QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.setStyleSheet("background-color: white; color: black;")
    label.move(100,5)

    B1 = QtWidgets.QPushButton(win)
    B1.setText("Click me")
    B1.move(99,49)
    B1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()