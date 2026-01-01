import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer, Qt
import time
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(200, 150)
        Form.setWindowTitle("Restrict")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)  # Remove default title bar
        Form.setStyleSheet("background-color: black")
        Form.setWindowIcon(QtGui.QIcon("c:/users/scant/desktop/python_Tutorial/restrict_icon.png"))

        self.titleBar = QtWidgets.QWidget(Form)  # Custom title bar
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.titleBar.setStyleSheet("background-color: black")

        self.title = QtWidgets.QLabel(self.titleBar)
        self.title.setText("Restrict")
        self.title.setGeometry(27,0,40,20)
        self.title.setStyleSheet("color: red")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(5, 2, 18, 16)  # Set label geometry to cover the whole window
        pixmap = QtGui.QPixmap("c:/users/scant/desktop/python_Tutorial/restrict_icon.png")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        self.closeButton = QtWidgets.QPushButton(self.titleBar)
        self.closeButton.setGeometry(QtCore.QRect(180, 0, 20, 20))
        self.closeButton.setStyleSheet("color: red")
        self.closeButton.setText("X")
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.clicked.connect(Form.close)

        self.minimizeButton = QtWidgets.QPushButton(self.titleBar)
        self.minimizeButton.setGeometry(QtCore.QRect(160, 0, 20, 20))
        self.minimizeButton.setStyleSheet("color: yellow")
        self.minimizeButton.setText("–")
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.clicked.connect(Form.minimizeWindow)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setToolTip("Click this to start the timer")
        self.pushButton.setGeometry(20, 35, 50, 50)
        self.pushButton.setStyleSheet("border-radius: 25; background-color: red; color: gold; font: 10pt;")
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setText("JS")
        self.pushButton.clicked.connect(self.strict)

        self.numenter = QtWidgets.QLineEdit(Form)
        self.numenter.setGeometry(QtCore.QRect(100, 45, 75, 30))
        self.numenter.setAlignment(QtCore.Qt.AlignCenter)
        self.numenter.setPlaceholderText("Enter seconds")
        self.numenter.setStyleSheet("color: lightgreen; font: 7.9pt")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 100, 100, 40)) #X, Y, Width, Length
        self.lineEdit_2.setStyleSheet("background-color: rgb(5, 5, 5);\n"
                                       "color: red;\n"
                                       "border: 2px solid;\n"
                                       "border-color: black;\n"
                                       "font: 75 13pt \"New Times Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setPlaceholderText("Counter")
        self.lineEdit_2.setEnabled(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def minimizeWindow(self):
        if not self.isMinimized():
            self.showMinimized()
        else:
            self.showNormal()

    def strict(self):
        input_text = self.numenter.text().strip()
        self.counter = int(input_text)

        self.timer.start(1000)  # Timer triggers every 1000 milliseconds (1 second)
        time.sleep(1)
        self.numenter.clear()
        self.numenter.setPlaceholderText("Restricting")
        self.numenter.setEnabled(False)

        self.restrict_animation = QTimer()
        self.restrict_animation.timeout.connect(self.update_placeholder)
        self.restrict_animation.start(1000)

    def update_placeholder(self):
        current_text = self.numenter.placeholderText()
        if current_text.endswith("..."):
            new_text = current_text[:-3]  # Remove the last three dots
        else:
            new_text = current_text + "."  # Add a dot

        self.numenter.setPlaceholderText(new_text)

    def update_timer(self):
        hours = self.counter // 3600
        minutes = (self.counter % 3600) // 60
        seconds = self.counter % 60
        self.lineEdit_2.setText("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
        self.counter -= 1

        if self.counter == -1:
            self.restrict_animation.stop()
            self.numenter.setPlaceholderText("Restricted")
            self.timer.stop()
            self.showRestartMessage()
            self.close()

    def showRestartMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Restricting")
        msg.setStyleSheet("background-color: black; color: lightgreen")
        msg.setText("Your time is Up, Goodbye!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        #msg.exec_()
        #time.sleep(1)
        #os.system("shutdown /r /t 1")

class MyForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draggable = True # Variable to control dragging
        self.setMouseTracking(True)  # Enable mouse tracking

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset') and self.draggable:
            self.move(self.mapToGlobal(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.draggable:
            del self.offset
            
    def closeEvent(self, event):
        QtWidgets.qApp.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyForm()
    Form.show()
    sys.exit(app.exec_())
