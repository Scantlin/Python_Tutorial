# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guess.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(False)
        Form.resize(518, 351)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 331, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 110, 141, 61))
        self.textEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid;\n"
"color: rgb(0, 170, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"border-top-color: rgb(255, 255, 0);\n"
"font: 75 27pt \"MS Shell Dlg 2\";")
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 200, 231, 61))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 110, 141, 61))
        self.textEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: 2px solid;\n"
"color: rgb(0, 170, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"border-top-color: rgb(255, 255, 0);\n"
"font: 75 27pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setTabChangesFocus(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, 0, 551, 351))
        self.label.setStyleSheet("image: url(:/newPrefix/37614-highlowBackgroundImage-1584073286.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.textEdit_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/ag.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ff0000;\">Guess the number</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
