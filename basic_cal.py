from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(262, 267)
        Form.setWindowIcon(QtGui.QIcon('c:/users/edna sarabia/desktop/python_tutorial/calc.png'))
        Form.setStyleSheet("background-color: black;")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 61, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: red; color: white; ")
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 80, 61, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: red; color: white;")
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 80, 61, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: red; color: white;")
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 140, 61, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color: red; color: white;")
        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 140, 61, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("background-color: red; color: white;")
        
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 200, 61, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background-color: red; color: yellow;")
        
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 200, 61, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("background-color: red; color: black;")
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 161, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter) #Align text in the center
        self.lineEdit.setStyleSheet("background-color: blue; color: yellow;")
        self.lineEdit.setEnabled(False) #disable line edit from asking input from a user
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect button clicks to functions
        self.pushButton.clicked.connect(lambda: self.append_text("1"))
        self.pushButton_2.clicked.connect(lambda: self.append_text("2"))
        self.pushButton_3.clicked.connect(lambda: self.append_text("3"))
        self.pushButton_4.clicked.connect(lambda: self.append_text("+"))
        self.pushButton_5.clicked.connect(lambda: self.append_text("-"))
        self.pushButton_6.clicked.connect(self.calculate_result)
        self.pushButton_7.clicked.connect(self.clear_line_edit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "+"))
        self.pushButton_5.setText(_translate("Form", "-"))
        self.pushButton_6.setText(_translate("Form", "="))
        self.pushButton_7.setText(_translate("Form", "Clear"))

    def append_text(self, text):
        current_text = self.lineEdit.text()
        new_text = current_text + text
        self.lineEdit.setText(new_text)
            
    def calculate_result(self):
        try:
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        except Exception as e:
            self.lineEdit.setText("Error")
            
    def clear_line_edit(self):
        self.lineEdit.clear()
        print("deleted")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
