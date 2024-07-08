from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1312, 750)
        MainWindow.setStyleSheet("#button_back_tslg{font-family:century gothic;font-size:18px;background:rgba(170, 170, 131,0.6);border-radius:15px;}\n"
"#button_back_tslg:hover{background-color: rgb(135, 124, 255);}\n"
"#frame{background:url(:/picture/.img_hvtslg.jpg);}\n"
"#frame_2{background:url(:/picture/.img_cttslg.jpg);}\n"
"#frame_inp{background:#333;border-radius:30px;}\n"
"#pu{background:rgb(0, 255, 255);border-radius:35px;}\n"
"#inp_ktslg, #inp_dtslg , #inp_htslg{background:transparent;border:none;color:rgb(0, 255, 255);border-bottom:1px solid #717072;font-size:24px}\n"
"#out_tslg{font-size:25px;}\n"
"#button_enter_tslg{background:rgb(170, 255, 255);border-radius:15px;}\n"
"#button_enter_tslg:hover{background:rgb(0, 255, 255);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 13, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 500, 471, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 231, 41))
        self.label_5.setObjectName("label_5")
        self.out_tslg = QtWidgets.QLineEdit(self.groupBox_2)
        self.out_tslg.setGeometry(QtCore.QRect(30, 80, 421, 31))
        self.out_tslg.setText("")
        self.out_tslg.setObjectName("out_tslg")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(600, 70, 441, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_back_tslg = QtWidgets.QPushButton(self.centralwidget)
        self.button_back_tslg.setGeometry(QtCore.QRect(40, 30, 161, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.button_back_tslg.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/.icon_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back_tslg.setIcon(icon)
        self.button_back_tslg.setIconSize(QtCore.QSize(35, 35))
        self.button_back_tslg.setObjectName("button_back_tslg")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(1040, 70, 261, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_inp = QtWidgets.QFrame(self.centralwidget)
        self.frame_inp.setGeometry(QtCore.QRect(120, 160, 401, 291))
        self.frame_inp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inp.setObjectName("frame_inp")
        self.label_2 = QtWidgets.QLabel(self.frame_inp)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 31))
        self.label_2.setObjectName("label_2")
        self.inp_ktslg = QtWidgets.QLineEdit(self.frame_inp)
        self.inp_ktslg.setGeometry(QtCore.QRect(180, 89, 171, 31))
        self.inp_ktslg.setText("")
        self.inp_ktslg.setObjectName("inp_ktslg")
        self.label_3 = QtWidgets.QLabel(self.frame_inp)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 111, 31))
        self.label_3.setObjectName("label_3")
        self.inp_dtslg = QtWidgets.QLineEdit(self.frame_inp)
        self.inp_dtslg.setGeometry(QtCore.QRect(180, 149, 171, 31))
        self.inp_dtslg.setText("")
        self.inp_dtslg.setObjectName("inp_dtslg")
        self.inp_htslg = QtWidgets.QLineEdit(self.frame_inp)
        self.inp_htslg.setGeometry(QtCore.QRect(180, 209, 171, 31))
        self.inp_htslg.setText("")
        self.inp_htslg.setObjectName("inp_htslg")
        self.label_4 = QtWidgets.QLabel(self.frame_inp)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 131, 31))
        self.label_4.setObjectName("label_4")
        self.button_enter_tslg = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter_tslg.setGeometry(QtCore.QRect(140, 490, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_enter_tslg.setFont(font)
        self.button_enter_tslg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/.icon_enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_enter_tslg.setIcon(icon1)
        self.button_enter_tslg.setIconSize(QtCore.QSize(75, 75))
        self.button_enter_tslg.setObjectName("button_enter_tslg")
        self.pu = QtWidgets.QPushButton(self.centralwidget)
        self.pu.setGeometry(QtCore.QRect(220, 110, 181, 91))
        self.pu.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/.icon_input.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pu.setIcon(icon2)
        self.pu.setIconSize(QtCore.QSize(80, 80))
        self.pu.setObjectName("pu")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1040, 410, 251, 171))
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1030, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1312, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button_enter_tslg.clicked.connect(self.tslg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tỉ Số Lượng Giác"))
        self.label.setText(_translate("MainWindow", "Tỉ Số Lượng Giác Của Góc Nhọn:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết Quả: "))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#0000ff;\">Góc (α) Cần Tìm Là:</span></p></body></html>"))
        self.button_back_tslg.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#00ff00;\">Cạnh Kề = </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#00ff00;\">Cạnh Đối = </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ff00;\">Cạnh Huyền = </span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ff0000;\">*</span><span style=\" font-size:14pt;\"> Hãy nhập đúng số</span></p><p><span style=\" font-size:14pt;\">đo của cách cạnh </span></p><p><span style=\" font-size:14pt;\">để có kết quả đúng </span></p><p><span style=\" font-size:14pt;\">nhất!!</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">dev: Nguyen Trong Tuan</span></p></body></html>"))
    def tslg(self):
        try:
            import math
            self.out_tslg.setText("")
            ck=0 ; cd=0 ; ch=0
            a=0 ; b=0 ; c=0 ; sd=0 
            if self.inp_ktslg.isModified():
                try: ck=float(self.inp_ktslg.text())
                except: ck=0
            if self.inp_dtslg.isModified():
                try: cd=float(self.inp_dtslg.text())
                except: cd=0
            if self.inp_htslg.isModified():
                try: ch=float(self.inp_htslg.text())
                except: ch=0
                
            if cd>0 and ch>0:
                a=float(math.asin(cd/ch))
                sd= a*(180/math.pi)
            if ck>0 and ch>0:
                b=float(math.acos(ck/ch))
                sd= b*(180/math.pi)
            if cd>0 and ck>0:
                c=float(math.atan(cd/ck))
                sd= c*(180/math.pi)

            du=sd%1
            tpphut=(du*60)
            phut=tpphut//1
            duphut=tpphut%1
            giay=(duphut*60)
            do=str(sd//1)
            du=sd%1
            tpphut=(du*60)
            phut=str(tpphut//1)
            duphut=tpphut%1
            giay=str(duphut*60)
            kq= (do + "°  " + phut + "'  " +giay + "''  ")
            self.out_tslg.setText(str(kq))
        except:
            error="Bạn đã nhập sai các hệ số của tam giác!"
            self.out_tslg.setText(str(error))

import image_rc

import sys

def excepthook(type, value, traceback):
    print(type, value, traceback)
sys.excepthook = excepthook
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
