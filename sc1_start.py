from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1279, 750)
        MainWindow.setStyleSheet("#frame_2{\n"
"background-image: url(:/test1/.bgr_mo_daupng.png);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1312, 750))
        self.frame_2.setStyleSheet("#start{background:rgba(0, 255, 127,0.7);border-radius:10px;font-size:50px;font-family:century gothic;}\n"
"#start:hover{font-family:Courier New;background-color: rgb(0, 255, 0);border-radius:20px;font-size:60px}\n"
"#block{background-color:rgb(78, 184, 242);font-size:22px;}\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.start = QtWidgets.QPushButton(self.frame_2)
        self.start.setGeometry(QtCore.QRect(90, 220, 201, 111))
        self.start.setObjectName("start")
        self.block = QtWidgets.QPushButton(self.frame_2)
        self.block.setGeometry(QtCore.QRect(780, 660, 491, 41))
        self.block.setObjectName("block")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(990, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1279, 26))
        self.menubar.setObjectName("menubar")
        self.menuEasy_Math_v1_1 = QtWidgets.QMenu(self.menubar)
        self.menuEasy_Math_v1_1.setObjectName("menuEasy_Math_v1_1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEasy_Math_v1_1.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Start"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.block.setText(_translate("MainWindow", "Báo Cáo Lỗi: trongtuan150409@gmail.com"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">dev: Nguyen Trong Tuan</span></p></body></html>"))
        self.menuEasy_Math_v1_1.setTitle(_translate("MainWindow", "Easy Math -v1.4"))
import start_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
