from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random


class Ui_Game(object):
    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.setFixedSize(420, 580)
        icon = QtGui.QIcon(":/newPrefix/rock.png")
        Game.setWindowIcon(icon)
        Game.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        status_bar = QtWidgets.QStatusBar(Game)
        status_bar.setStyleSheet("background-color: rgb(0, 0, 0); color: white;")
        Game.setStatusBar(status_bar)

        self.pushButton = QtWidgets.QPushButton(Game)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 121, 121))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/scissors.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.check("scissors", self.pushButton))

        self.pushButton_4 = QtWidgets.QPushButton(Game)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 110, 121, 121))
        self.pushButton_4.setStyleSheet("image: url(:/newPrefix/paper.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.check("paper", self.pushButton_4))

        self.pushButton_2 = QtWidgets.QPushButton(Game)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 110, 121, 121))
        self.pushButton_2.setStyleSheet("image: url(:/newPrefix/rock.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.check("rock", self.pushButton_2))

        self.label = QtWidgets.QLabel(Game)
        self.label.setGeometry(QtCore.QRect(40, 10, 360, 68))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                 "font: 30pt \"Niagara Solid\"; \n"
                                 "color: rgb(85, 255, 127);")
        self.label.setObjectName("label")

        self.lineEdit_2 = QtWidgets.QLineEdit(Game)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 290, 121, 121))
        self.lineEdit_2.setStyleSheet("border: none;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.label_2 = QtWidgets.QLabel(Game)
        self.label_2.setGeometry(QtCore.QRect(100, 250, 231, 20))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Game)
        self.label_3.setGeometry(QtCore.QRect(100, 75, 231, 20))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Game)
        self.lineEdit.setGeometry(QtCore.QRect(72, 440, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        
        self.label_4 = QtWidgets.QLabel(Game)
        self.label_4.setGeometry(QtCore.QRect(117, 480, 200, 100))
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: aqua; border: 2px solid brown; font-size: 18px")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        
        self.score_human = 0
        self.score_computer = 0

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def check(self, user_choice, clicked_button):
        for button in [self.pushButton, self.pushButton_4, self.pushButton_2]:
            button.setStyleSheet(button.styleSheet().replace("border: 2px solid rgb(85, 255, 127);", " "))

        # Highlight the clicked button
        clicked_button.setStyleSheet(clicked_button.styleSheet() + "border: 2px solid rgb(85, 255, 127);")

        computer_choice = random.choice(["rock", "paper", "scissors"])

        if computer_choice == "scissors":
            self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/scissors.png);")
        elif computer_choice == "rock":
            self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/rock.png);")
        elif computer_choice == "paper":
            self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/paper.png);")

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
                (user_choice == "rock" and computer_choice == "scissors") or
                (user_choice == "paper" and computer_choice == "rock") or
                (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
            self.score_human += 1
        else:
            result = "Computer wins!"
            self.score_computer += 1
        
        self.lineEdit.setText(f"{result}")
        if result == "You win!":
            self.lineEdit.setStyleSheet("color: gold; font-size: 16pt")
        elif result == "It's a tie!":
            self.lineEdit.setStyleSheet("color: green; font-size: 16pt")
        else:
            self.lineEdit.setStyleSheet("color: red; font-size: 16pt")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_4.setText(f"Score!\nHuman: {self.score_human} Computer: {self.score_computer}")
        
        if self.score_computer == 5 or self.score_human == 5:
            Box = QMessageBox()
            Box.setWindowTitle("Results")
            if self.score_human == 5:
                Box.setText("You Won in this Match")
            elif self.score_computer == 5: 
                Box.setText("You Lost in this Match")
            self.score_human = 0
            self.score_computer = 0
            self.label_4.setText("Score!\nHuman Vs Computer")
            Box.exec_()

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "Rock Paper and Scissors"))
        self.label.setText(_translate("Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-style:italic;\">Rock Paper and Scissors</span></p></body></html>"))
        self.label_2.setText(_translate("Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#55ffff;\">COMPUTER</span></p></body></html>"))
        self.label_3.setText(_translate("Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#00ffff;\">HUMAN</span></p></body></html>"))
        self.label_4.setText(_translate("Game", "Score!\nHuman Vs Computer"))

import test_rc_1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QWidget()
    ui = Ui_Game()
    ui.setupUi(Game)
    Game.show()
    sys.exit(app.exec_())
