from PyQt5 import QtCore, QtGui, QtWidgets
from test_rc import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 351)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ag.png"), QtGui.QIcon.Normal)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 331, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 141, 61))
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid;\n"
"color: rgb(0, 170, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"border-top-color: rgb(255, 255, 0);\n"
"font: 75 27pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 200, 231, 61))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 110, 141, 61))
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid;\n"
"color: rgb(0, 170, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"border-top-color: rgb(255, 255, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Enter some notes about your task")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, 0, 551, 351))
        self.label.setStyleSheet("image: url(:/newPrefix/37614-highlowBackgroundImage-1584073286.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Guess the number"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/ag.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ff0000;\">Guess the number</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
