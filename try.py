# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox


class Ui_Form(object):
    def clicked(self):
        y_text = "Hello World"
        y = QMessageBox()
        y.setIcon(QMessageBox.Information)
        y.setText(y_text)
        y.exec_()
    
    def push(self):
        x = QDialog()
        x.exec_()
        
        
    def setupUi(self, Form):
        Form.setObjectName("Try")
        Form.resize(400, 300)
        self.Button = QtWidgets.QPushButton(Form)
        self.Button.setGeometry(QtCore.QRect(150, 50, 81, 41))
        self.Button.setObjectName("Button")
        self.Button.clicked.connect(self.clicked)
        self.Button2 = QtWidgets.QPushButton(Form)
        self.Button2.setGeometry(QtCore.QRect(150,100,81,41))
        self.Button2.clicked.connect(self.push)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Try", "Try"))
        self.Button.setText(_translate("Try", "Click me"))
        self.Button2.setText(_translate("Try", "Push me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
