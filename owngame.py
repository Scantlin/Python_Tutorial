from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import turtle
from test_rc import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(518, 351)
        Form.setWindowIcon(QtGui.QIcon(":/newPrefix/333237728_219566600521895_5681794888765001149_n (1).jpg"))
        Form.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle("Menu")
        self.menuFile.setStyleSheet("background-color: lightblue")
        self.menubar.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.actionExit = QtWidgets.QAction(Form)
        self.actionExit.setText("Help")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.triggered.connect(self.show_help_dialog)
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 331, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 141, 61))
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
    "border: 2px solid;\n"
    "color: rgb(255, 255, 0); color: rgb(255, 255, 0);\n"
    "border-color: rgb(255, 255, 0);\n"
    "font: 75 25pt \"MS Shell Dlg 2\";\n"
    "selection-background-color: rgb(0, 170, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.returnPressed.connect(self.check_guess)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("color: red; font: 20 12pt")
        self.label_3.setObjectName("label_3")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 110, 141, 61))
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid;\n"
"color: black;\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 25pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setPlaceholderText("Answer")
        self.lineEdit_2.setEnabled(False)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, 0, 551, 351))
        self.label.setStyleSheet("image: url(:/newPrefix/37614-highlowBackgroundImage-1584073286.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(215, 200, 50, 50)
        self.pushButton.setStyleSheet("border-radius : 25; border : 2px solid; background-color: #D4D4D2; border-color: yellow")
        self.pushButton.clicked.connect(self.check_guess)
        
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setGeometry(325, 200, 50, 50)
        self.clearButton.setStyleSheet("border-radius: 25; border: 2px solid; background-color: #D4D4D2; border-color: blue;")
        self.clearButton.setText("Clear")
        self.clearButton.clicked.connect(self.clearLineEdit)
        
        self.clear_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+B"), Form)
        self.clear_shortcut.activated.connect(self.clearLineEdit)
        
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.menubar.raise_()
        self.clearButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Guess the number"))
        self.label_2.setText(_translate("Form", "<html><head/><body><i><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ff0000;\">Guess the number</span></p></i></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\"></span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Enter"))
        
        
    def check_guess(self):
        # Get the user's guess from the QLineEdit
        user_guess = int(self.lineEdit.text()) if self.lineEdit.text().isdigit() else None

        if user_guess is not None:
            # Generate a random number
            random_number = random.randrange(1, 11)

            # Compare the user's guess with the random number
            if user_guess == random_number:
                self.lineEdit_2.setText(str(random_number))
                self.label_3.setGeometry(QtCore.QRect(157, 250, 280, 61))
                self.label_3.setText("Congratulations! You guessed correctly!")
            elif user_guess > 10 or user_guess < 1:
                self.label_3.setGeometry(QtCore.QRect(160, 250, 280, 61))
                self.label_3.setText("The number to guess is within 1 - 10")
                self.lineEdit_2.clear()
            else:
                self.lineEdit_2.setText(str(random_number))
                self.label_3.setGeometry(QtCore.QRect(180, 250, 280, 61))
                self.label_3.setText("Oops! Wrong guess. Try again!")
        else:
            # Display a message if the user input is not a valid number
            warning_box = QMessageBox()
            warning_box.setWindowTitle("Error Input")
            warning_box.setText("""Please enter a number in ranges 1-5 \nYour input is invalid! Things to remember \n\n• The letter should not used as an guess\n• Your answer if exceeded in 10 then automatic wrong""")
            warning_box.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.SplashScreen)
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.exec_()
        
    def clearLineEdit(self):
        # Clear the content of the two QLineEdit widgets
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_3.clear()

        
    def show_help_dialog(self):
        help_text = """This Game is developed by Scantlin Cayson \nYour task is to guess what is the random number! the number is from 1 - 10
\n• input your answer into the 'Guess Box' then click enter, the random number reveal once you already submit your answer \n• Enjoy the game"""

        help_box = QMessageBox()
        help_box.setWindowIcon(QtGui.QIcon(":/newPrefix/ag.png"))
        help_box.setIcon(QMessageBox.Question)
        help_box.setWindowTitle("How to use this program")
        help_box.setStyleSheet("background-color: lightblue; color: black;")
        
        help_box.setText(help_text)
        help_box.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
