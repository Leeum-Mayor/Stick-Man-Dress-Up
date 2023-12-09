# Form implementation generated from reading ui file 'guidesign.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Stick-man Dress-Up")
        MainWindow.setFixedSize(1100, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(parent=self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1100, 800))
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/background.png"))
        self.background.setObjectName("background")
        self.stickman = QtWidgets.QLabel(parent=self.centralwidget)
        self.stickman.setGeometry(QtCore.QRect(320, 190, 291, 611))
        self.stickman.setText("")
        self.stickman.setPixmap(QtGui.QPixmap("images/stick-man-default.png"))
        self.stickman.setScaledContents(True)
        self.stickman.setObjectName("stickman")
        self.hatSubframe1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.hatSubframe1.setEnabled(True)
        self.hatSubframe1.setGeometry(QtCore.QRect(690, 0, 411, 80))
        self.hatSubframe1.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.hatSubframe1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hatSubframe1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hatSubframe1.setObjectName("hatSubframe1")
        self.hat0Button = QtWidgets.QRadioButton(parent=self.hatSubframe1)
        self.hat0Button.setGeometry(QtCore.QRect(10, 33, 19, 16))
        self.hat0Button.setText("")
        self.hat0Button.setChecked(True)
        self.hat0Button.setObjectName("hat0Button")
        self.hat0Label = QtWidgets.QLabel(parent=self.hatSubframe1)
        self.hat0Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.hat0Label.setText("")
        self.hat0Label.setPixmap(QtGui.QPixmap("images/none.png"))
        self.hat0Label.setObjectName("hat0Label")
        self.hat1Button = QtWidgets.QRadioButton(parent=self.hatSubframe1)
        self.hat1Button.setGeometry(QtCore.QRect(142, 33, 19, 16))
        self.hat1Button.setText("")
        self.hat1Button.setObjectName("hat1Button")
        self.hat2Button = QtWidgets.QRadioButton(parent=self.hatSubframe1)
        self.hat2Button.setGeometry(QtCore.QRect(275, 33, 19, 16))
        self.hat2Button.setText("")
        self.hat2Button.setObjectName("hat2Button")
        self.hat1Label = QtWidgets.QLabel(parent=self.hatSubframe1)
        self.hat1Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.hat1Label.setText("")
        self.hat1Label.setPixmap(QtGui.QPixmap("images/hat1.png"))
        self.hat1Label.setScaledContents(True)
        self.hat1Label.setObjectName("hat1Label")
        self.hat2Label = QtWidgets.QLabel(parent=self.hatSubframe1)
        self.hat2Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.hat2Label.setText("")
        self.hat2Label.setPixmap(QtGui.QPixmap("images/hat2.png"))
        self.hat2Label.setScaledContents(True)
        self.hat2Label.setObjectName("hat2Label")
        self.topFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.topFrame.setGeometry(QtCore.QRect(690, 190, 411, 211))
        self.topFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topFrame.setObjectName("topFrame")
        self.topSubframe2 = QtWidgets.QFrame(parent=self.topFrame)
        self.topSubframe2.setGeometry(QtCore.QRect(0, 120, 411, 80))
        self.topSubframe2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topSubframe2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topSubframe2.setObjectName("topSubframe2")
        self.top3Button = QtWidgets.QRadioButton(parent=self.topSubframe2)
        self.top3Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.top3Button.setText("")
        self.top3Button.setObjectName("top3Button")
        self.top3Label = QtWidgets.QLabel(parent=self.topSubframe2)
        self.top3Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.top3Label.setText("")
        self.top3Label.setPixmap(QtGui.QPixmap("images/top3.png"))
        self.top3Label.setScaledContents(True)
        self.top3Label.setObjectName("top3Label")
        self.top4Label = QtWidgets.QLabel(parent=self.topSubframe2)
        self.top4Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.top4Label.setText("")
        self.top4Label.setPixmap(QtGui.QPixmap("images/top4.png"))
        self.top4Label.setScaledContents(True)
        self.top4Label.setObjectName("top4Label")
        self.top4Button = QtWidgets.QRadioButton(parent=self.topSubframe2)
        self.top4Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.top4Button.setText("")
        self.top4Button.setObjectName("top4Button")
        self.top5Button = QtWidgets.QRadioButton(parent=self.topSubframe2)
        self.top5Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.top5Button.setText("")
        self.top5Button.setObjectName("top5Button")
        self.top5Label = QtWidgets.QLabel(parent=self.topSubframe2)
        self.top5Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.top5Label.setText("")
        self.top5Label.setPixmap(QtGui.QPixmap("images/top5.png"))
        self.top5Label.setScaledContents(True)
        self.top5Label.setObjectName("top5Label")
        self.topSubframe1 = QtWidgets.QFrame(parent=self.topFrame)
        self.topSubframe1.setGeometry(QtCore.QRect(0, 10, 411, 80))
        self.topSubframe1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topSubframe1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topSubframe1.setObjectName("topSubframe1")
        self.top0Button = QtWidgets.QRadioButton(parent=self.topSubframe1)
        self.top0Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.top0Button.setText("")
        self.top0Button.setObjectName("top0Button")
        self.top0Button.setChecked(True)
        self.top0Label = QtWidgets.QLabel(parent=self.topSubframe1)
        self.top0Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.top0Label.setText("")
        self.top0Label.setPixmap(QtGui.QPixmap("images/none.png"))
        self.top0Label.setObjectName("top0Label")
        self.top1Label = QtWidgets.QLabel(parent=self.topSubframe1)
        self.top1Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.top1Label.setText("")
        self.top1Label.setPixmap(QtGui.QPixmap("images/top1.png"))
        self.top1Label.setScaledContents(True)
        self.top1Label.setObjectName("top1Label")
        self.top1Button = QtWidgets.QRadioButton(parent=self.topSubframe1)
        self.top1Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.top1Button.setText("")
        self.top1Button.setObjectName("top1Button")
        self.top2Button = QtWidgets.QRadioButton(parent=self.topSubframe1)
        self.top2Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.top2Button.setText("")
        self.top2Button.setObjectName("top2Button")
        self.top2Label = QtWidgets.QLabel(parent=self.topSubframe1)
        self.top2Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.top2Label.setText("")
        self.top2Label.setPixmap(QtGui.QPixmap("images/top2.png"))
        self.top2Label.setScaledContents(True)
        self.top2Label.setObjectName("top2Label")
        self.hatSubframe2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.hatSubframe2.setGeometry(QtCore.QRect(690, 100, 411, 80))
        self.hatSubframe2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hatSubframe2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hatSubframe2.setObjectName("hatSubframe2")
        self.hat3Button = QtWidgets.QRadioButton(parent=self.hatSubframe2)
        self.hat3Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.hat3Button.setText("")
        self.hat3Button.setObjectName("hat3Button")
        self.hat3Label = QtWidgets.QLabel(parent=self.hatSubframe2)
        self.hat3Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.hat3Label.setText("")
        self.hat3Label.setPixmap(QtGui.QPixmap("images/hat3.png"))
        self.hat3Label.setScaledContents(True)
        self.hat3Label.setObjectName("hat3Label")
        self.hat4Button = QtWidgets.QRadioButton(parent=self.hatSubframe2)
        self.hat4Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.hat4Button.setText("")
        self.hat4Button.setObjectName("hat4Button")
        self.hat4Label = QtWidgets.QLabel(parent=self.hatSubframe2)
        self.hat4Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.hat4Label.setText("")
        self.hat4Label.setPixmap(QtGui.QPixmap("images/hat4.png"))
        self.hat4Label.setScaledContents(True)
        self.hat4Label.setObjectName("hat4Label")
        self.hat5Button = QtWidgets.QRadioButton(parent=self.hatSubframe2)
        self.hat5Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.hat5Button.setText("")
        self.hat5Button.setObjectName("hat5Button")
        self.hat5Label = QtWidgets.QLabel(parent=self.hatSubframe2)
        self.hat5Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.hat5Label.setText("")
        self.hat5Label.setPixmap(QtGui.QPixmap("images/hat5.png"))
        self.hat5Label.setScaledContents(True)
        self.hat5Label.setObjectName("hat5Label")
        self.pantsFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.pantsFrame.setGeometry(QtCore.QRect(690, 400, 411, 211))
        self.pantsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pantsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pantsFrame.setObjectName("pantsFrame")
        self.pantsSubframe2 = QtWidgets.QFrame(parent=self.pantsFrame)
        self.pantsSubframe2.setGeometry(QtCore.QRect(0, 120, 411, 80))
        self.pantsSubframe2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pantsSubframe2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pantsSubframe2.setObjectName("pantsSubframe2")
        self.pants3Button = QtWidgets.QRadioButton(parent=self.pantsSubframe2)
        self.pants3Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.pants3Button.setText("")
        self.pants3Button.setObjectName("pants3Button")
        self.pants3Label = QtWidgets.QLabel(parent=self.pantsSubframe2)
        self.pants3Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.pants3Label.setText("")
        self.pants3Label.setPixmap(QtGui.QPixmap("images/pants3.png"))
        self.pants3Label.setScaledContents(True)
        self.pants3Label.setObjectName("pants3Label")
        self.pants4Label = QtWidgets.QLabel(parent=self.pantsSubframe2)
        self.pants4Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.pants4Label.setText("")
        self.pants4Label.setPixmap(QtGui.QPixmap("images/pants4.png"))
        self.pants4Label.setScaledContents(True)
        self.pants4Label.setObjectName("pants4Label")
        self.pants4Button = QtWidgets.QRadioButton(parent=self.pantsSubframe2)
        self.pants4Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.pants4Button.setText("")
        self.pants4Button.setObjectName("pants4Button")
        self.pants5Button = QtWidgets.QRadioButton(parent=self.pantsSubframe2)
        self.pants5Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.pants5Button.setText("")
        self.pants5Button.setObjectName("pants5Button")
        self.pants5Label = QtWidgets.QLabel(parent=self.pantsSubframe2)
        self.pants5Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.pants5Label.setText("")
        self.pants5Label.setPixmap(QtGui.QPixmap("images/pants5.png"))
        self.pants5Label.setScaledContents(True)
        self.pants5Label.setObjectName("pants5Label")
        self.pantsSubframe1 = QtWidgets.QFrame(parent=self.pantsFrame)
        self.pantsSubframe1.setGeometry(QtCore.QRect(0, 20, 411, 80))
        self.pantsSubframe1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pantsSubframe1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pantsSubframe1.setObjectName("pantsSubframe1")
        self.pants0Button = QtWidgets.QRadioButton(parent=self.pantsSubframe1)
        self.pants0Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.pants0Button.setText("")
        self.pants0Button.setObjectName("pants0Button")
        self.pants0Button.setChecked(True)
        self.pants0Label = QtWidgets.QLabel(parent=self.pantsSubframe1)
        self.pants0Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.pants0Label.setText("")
        self.pants0Label.setPixmap(QtGui.QPixmap("images/none.png"))
        self.pants0Label.setObjectName("pants0Label")
        self.pants1Label = QtWidgets.QLabel(parent=self.pantsSubframe1)
        self.pants1Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.pants1Label.setText("")
        self.pants1Label.setPixmap(QtGui.QPixmap("images/pants1.png"))
        self.pants1Label.setScaledContents(True)
        self.pants1Label.setObjectName("pants1Label")
        self.pants1Button = QtWidgets.QRadioButton(parent=self.pantsSubframe1)
        self.pants1Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.pants1Button.setText("")
        self.pants1Button.setObjectName("pants1Button")
        self.pants2Button = QtWidgets.QRadioButton(parent=self.pantsSubframe1)
        self.pants2Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.pants2Button.setText("")
        self.pants2Button.setObjectName("pants2Button")
        self.pants2Label = QtWidgets.QLabel(parent=self.pantsSubframe1)
        self.pants2Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.pants2Label.setText("")
        self.pants2Label.setPixmap(QtGui.QPixmap("images/pants2.png"))
        self.pants2Label.setScaledContents(True)
        self.pants2Label.setObjectName("pants2Label")
        self.shoeFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.shoeFrame.setGeometry(QtCore.QRect(690, 620, 411, 181))
        self.shoeFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.shoeFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.shoeFrame.setObjectName("shoeFrame")
        self.shoeSubframe2 = QtWidgets.QFrame(parent=self.shoeFrame)
        self.shoeSubframe2.setGeometry(QtCore.QRect(0, 100, 411, 80))
        self.shoeSubframe2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.shoeSubframe2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.shoeSubframe2.setObjectName("shoeSubframe2")
        self.shoe3Button = QtWidgets.QRadioButton(parent=self.shoeSubframe2)
        self.shoe3Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.shoe3Button.setText("")
        self.shoe3Button.setObjectName("shoe3Button")
        self.shoe3Label = QtWidgets.QLabel(parent=self.shoeSubframe2)
        self.shoe3Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.shoe3Label.setText("")
        self.shoe3Label.setPixmap(QtGui.QPixmap("images/shoe3.png"))
        self.shoe3Label.setObjectName("shoe3Label")
        self.shoe4Label = QtWidgets.QLabel(parent=self.shoeSubframe2)
        self.shoe4Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.shoe4Label.setText("")
        self.shoe4Label.setPixmap(QtGui.QPixmap("images/shoe4.png"))
        self.shoe4Label.setObjectName("shoe4Label")
        self.shoe4Button = QtWidgets.QRadioButton(parent=self.shoeSubframe2)
        self.shoe4Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.shoe4Button.setText("")
        self.shoe4Button.setObjectName("shoe4Button")
        self.shoe5Button = QtWidgets.QRadioButton(parent=self.shoeSubframe2)
        self.shoe5Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.shoe5Button.setText("")
        self.shoe5Button.setObjectName("shoe5Button")
        self.shoe5Label = QtWidgets.QLabel(parent=self.shoeSubframe2)
        self.shoe5Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.shoe5Label.setText("")
        self.shoe5Label.setPixmap(QtGui.QPixmap("images/shoe5.png"))
        self.shoe5Label.setObjectName("shoe5Label")
        self.shoeSubframe1 = QtWidgets.QFrame(parent=self.shoeFrame)
        self.shoeSubframe1.setGeometry(QtCore.QRect(0, 0, 411, 80))
        self.shoeSubframe1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.shoeSubframe1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.shoeSubframe1.setObjectName("shoeSubframe1")
        self.shoe0Button = QtWidgets.QRadioButton(parent=self.shoeSubframe1)
        self.shoe0Button.setGeometry(QtCore.QRect(10, 33, 16, 16))
        self.shoe0Button.setText("")
        self.shoe0Button.setObjectName("shoe0Button")
        self.shoe0Button.setChecked(True)
        self.shoe0Label = QtWidgets.QLabel(parent=self.shoeSubframe1)
        self.shoe0Label.setGeometry(QtCore.QRect(40, 10, 60, 60))
        self.shoe0Label.setText("")
        self.shoe0Label.setPixmap(QtGui.QPixmap("images/none.png"))
        self.shoe0Label.setObjectName("shoe0Label")
        self.shoe1Label = QtWidgets.QLabel(parent=self.shoeSubframe1)
        self.shoe1Label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.shoe1Label.setText("")
        self.shoe1Label.setPixmap(QtGui.QPixmap("images/shoe1.png"))
        self.shoe1Label.setObjectName("shoe1Label")
        self.shoe1Button = QtWidgets.QRadioButton(parent=self.shoeSubframe1)
        self.shoe1Button.setGeometry(QtCore.QRect(142, 33, 16, 16))
        self.shoe1Button.setText("")
        self.shoe1Button.setObjectName("shoe1Button")
        self.shoe2Button = QtWidgets.QRadioButton(parent=self.shoeSubframe1)
        self.shoe2Button.setGeometry(QtCore.QRect(275, 33, 16, 16))
        self.shoe2Button.setText("")
        self.shoe2Button.setObjectName("shoe2Button")
        self.shoe2Label = QtWidgets.QLabel(parent=self.shoeSubframe1)
        self.shoe2Label.setGeometry(QtCore.QRect(310, 10, 60, 60))
        self.shoe2Label.setText("")
        self.shoe2Label.setPixmap(QtGui.QPixmap("images/shoe2.png"))
        self.shoe2Label.setObjectName("shoe2Label")
        self.outfit1Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit1Button.setGeometry(QtCore.QRect(10, 10, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.outfit1Button.setFont(font)
        self.outfit1Button.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.outfit1Button.setObjectName("outfit1Button")

        self.outfit1Load = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit1Load.setGeometry(QtCore.QRect(10, 10, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.outfit1Load.setFont(font)
        self.outfit1Load.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.outfit1Load.setObjectName("outfit1Load")

        self.outfit2Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit2Button.setGeometry(QtCore.QRect(10, 120, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.outfit2Button.setFont(font)
        self.outfit2Button.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.outfit2Button.setObjectName("outfit2Button")

        self.outfit2Load = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit2Load.setGeometry(QtCore.QRect(10, 120, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.outfit2Load.setFont(font)
        self.outfit2Load.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.outfit2Load.setObjectName("outfit2Load")

        self.outfit3Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit3Button.setGeometry(QtCore.QRect(10, 230, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.outfit3Button.setFont(font)
        self.outfit3Button.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.outfit3Button.setObjectName("outfit3Button")

        self.outfit3Load = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit3Load.setGeometry(QtCore.QRect(10, 230, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        self.outfit3Load.setFont(font)
        self.outfit3Load.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.outfit3Load.setObjectName("outfit3Load")

        self.outfit3Delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit3Delete.setGeometry(QtCore.QRect(230, 280, 30, 30))
        self.outfit3Delete.setStyleSheet("background-color: rgb(69, 163, 220);")
        self.outfit3Delete.setText("")
        self.outfit3Delete.setObjectName("outfit3Delete")
        self.outfit2Delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit2Delete.setGeometry(QtCore.QRect(230, 170, 30, 30))
        self.outfit2Delete.setStyleSheet("background-color: rgb(69, 163, 220);")
        self.outfit2Delete.setText("")
        self.outfit2Delete.setObjectName("outfit2Delete")
        self.outfit1Delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outfit1Delete.setGeometry(QtCore.QRect(230, 60, 30, 30))
        self.outfit1Delete.setStyleSheet("background-color: rgb(69, 163, 220);")
        self.outfit1Delete.setText("")
        self.outfit1Delete.setObjectName("outfit1Delete")
        self.topWearing = QtWidgets.QLabel(parent=self.centralwidget)
        self.topWearing.setGeometry(QtCore.QRect(380, 450, 170, 205))
        self.topWearing.setText("")
        self.topWearing.setPixmap(QtGui.QPixmap(""))
        self.topWearing.setScaledContents(True)
        self.topWearing.setObjectName("topWearing")
        self.hatWearing = QtWidgets.QLabel(parent=self.centralwidget)
        self.hatWearing.setGeometry(QtCore.QRect(350, 80, 240, 240))
        self.hatWearing.setText("")
        self.hatWearing.setPixmap(QtGui.QPixmap(""))
        self.hatWearing.setScaledContents(True)
        self.hatWearing.setObjectName("hatWearing")
        self.pantsWearing = QtWidgets.QLabel(parent=self.centralwidget)
        self.pantsWearing.setGeometry(QtCore.QRect(390, 660, 151, 131))
        self.pantsWearing.setText("")
        self.pantsWearing.setPixmap(QtGui.QPixmap(""))
        self.pantsWearing.setScaledContents(True)
        self.pantsWearing.setObjectName("pantsWearing")
        self.shoeWearing = QtWidgets.QLabel(parent=self.centralwidget)
        self.shoeWearing.setGeometry(QtCore.QRect(367, 750, 201, 50))
        self.shoeWearing.setText("")
        self.shoeWearing.setPixmap(QtGui.QPixmap(""))
        self.shoeWearing.setScaledContents(True)
        self.shoeWearing.setObjectName("shoeWearing")

        self.hatGroup = QtWidgets.QButtonGroup()
        for i in range(6):
            button_name = getattr(self, f'hat{i}Button')

            self.hatGroup.addButton(button_name, i + 1)

        self.topGroup = QtWidgets.QButtonGroup()
        for i in range(6):
            for i in range(6):
                button_name = getattr(self, f'top{i}Button')

                self.topGroup.addButton(button_name, i + 1)

        self.pantsGroup = QtWidgets.QButtonGroup()
        for i in range(6):
            button_name = getattr(self, f'pants{i}Button')

            self.pantsGroup.addButton(button_name, i + 1)

        self.shoeGroup = QtWidgets.QButtonGroup()
        for i in range(6):
            button_name = getattr(self, f'shoe{i}Button')

            self.shoeGroup.addButton(button_name, i + 1)

        for i in range(1, 4):
            deleteName = getattr(self, f'outfit{i}Delete')
            deleteName.setIcon(QtGui.QIcon(QPixmap("images/delete")))

        self.background.raise_()
        self.stickman.raise_()
        self.topFrame.raise_()
        self.hatSubframe1.raise_()
        self.hatSubframe2.raise_()
        self.pantsFrame.raise_()
        self.shoeFrame.raise_()
        self.outfit1Load.raise_()
        self.outfit1Button.raise_()
        self.outfit2Load.raise_()
        self.outfit2Button.raise_()
        self.outfit3Load.raise_()
        self.outfit3Button.raise_()
        self.outfit3Delete.raise_()
        self.outfit2Delete.raise_()
        self.outfit1Delete.raise_()
        self.topWearing.raise_()
        self.hatWearing.raise_()
        self.shoeWearing.raise_()
        self.pantsWearing.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outfit1Button.setText(_translate("MainWindow", "SAVE OUTFIT 1"))
        self.outfit1Load.setText(_translate("MainWindow", "LOAD OUTFIT 1"))
        self.outfit2Button.setText(_translate("MainWindow", "SAVE OUTFIT 2"))
        self.outfit2Load.setText(_translate("MainWindow", "LOAD OUTFIT 2"))
        self.outfit3Button.setText(_translate("MainWindow", "SAVE OUTFIT 3"))
        self.outfit3Load.setText(_translate("MainWindow", "LOAD OUTFIT 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
