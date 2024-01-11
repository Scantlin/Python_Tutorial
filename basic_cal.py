from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 405)
        Form.setWindowIcon(QtGui.QIcon('c:/users/edna sarabia/desktop/python_tutorial/calc.png'))
        Form.setStyleSheet("background-color: black;")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 54, 54))
        self.pushButton.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #D4D4D2; ")
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 80, 54, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #D4D4D2;")
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 80, 54, 54))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #D4D4D2;")
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 80, 54, 54))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color: red; color: white;")
        self.pushButton_4.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #FF9500; ")
        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 145, 54, 54))
        self.pushButton_5.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #FF9500; ")
        
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 340, 54, 54))
        self.pushButton_6.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #FF9500; ")
        
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 500, 54, 54))
        self.pushButton_7.setStyleSheet("background-color: red; color: black;")
        
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 145, 54, 54))
        self.pushButton_8.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 145, 54, 54))
        self.pushButton_9.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 145, 54, 54))
        self.pushButton_10.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 210, 54, 54))
        self.pushButton_11.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 210, 54, 54))
        self.pushButton_12.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(140, 210, 54, 54))
        self.pushButton_13.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 210, 54, 54))
        self.pushButton_14.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #FF9500; ")
        
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 275, 54, 54))
        self.pushButton_15.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(80, 275, 54, 54))
        self.pushButton_16.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(140, 275, 54, 54))
        self.pushButton_17.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(200, 275, 54, 54))
        self.pushButton_18.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #FF9500; ")
        
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(20, 340, 114, 54))
        self.pushButton_19.setStyleSheet("border-radius : 27; border : 2px solid; background-color:  #505050; ")
        
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(140, 340, 54, 54))
        self.pushButton_20.setStyleSheet("border-radius : 27; border : 2px solid; background-color: #505050;")
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 268, 75))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter) #Align text in the center
        self.lineEdit.setStyleSheet("background-color: black; color: white; border: none;")
        self.lineEdit.setEnabled(True) #disable line edit from asking input from a user
        self.lineEdit.setFont(QFont('Arial', 15))
        
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
        self.pushButton_8.clicked.connect(lambda: self.append_text("4"))
        self.pushButton_9.clicked.connect(lambda: self.append_text("5"))
        self.pushButton_10.clicked.connect(lambda: self.append_text("6"))
        self.pushButton_11.clicked.connect(lambda: self.append_text("7"))
        self.pushButton_12.clicked.connect(lambda: self.append_text("8"))
        self.pushButton_13.clicked.connect(lambda: self.append_text("9"))
        self.pushButton_14.clicked.connect(lambda: self.append_text("*"))

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
        self.pushButton_8.setText(_translate("Form", "4"))
        self.pushButton_9.setText(_translate("Form", "5"))
        self.pushButton_10.setText(_translate("Form", "6"))
        self.pushButton_11.setText(_translate("Form", "7"))
        self.pushButton_12.setText(_translate("Form", "8"))
        self.pushButton_13.setText(_translate("Form", "9"))
        self.pushButton_14.setText(_translate("Form", "*"))

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
