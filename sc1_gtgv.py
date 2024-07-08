from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1312, 750)
        MainWindow.setStyleSheet("#button_back_gtgv{font-family:century gothic;font-size:18px;background:rgba(170, 170, 131,0.6);border-radius:15px;}\n"
"#button_back_gtgv:hover{background-color: rgb(135, 124, 255);font-size:20px;}#inp_cgv  , #inp_tan , #inp_cotg , #inp_ch , #inp_ch , #inp_cos , #inp_sin{background:transparent;border:none;border-bottom:1px solid #717072;font-size: 21px;}\n"
"#out_cgv1 , #out_cgv2 , #out_ch , #out_d , #out_k{background:transparent;border:none;border-bottom:1px solid #717072;font-size: 21px;}\n"
"#enter1 , #enter2{background:rgb(80, 255, 130);border-radius:25px;font-size: 22px;}\n"
"#enter1:hover , #enter2:hover{background:rgb(0, 255, 0);border-radius:25px;font-size: 30px;}\n"
"#frame, #frame_2 , #frame_3{border:1px solid rgb(0, 0, 0);}\n"
"#out_kl{font-size: 22px;border:1.5px solid rgb(255, 0, 4)}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_back_gtgv = QtWidgets.QPushButton(self.centralwidget)
        self.button_back_gtgv.setGeometry(QtCore.QRect(40, 30, 161, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.button_back_gtgv.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/.icon_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back_gtgv.setIcon(icon)
        self.button_back_gtgv.setIconSize(QtCore.QSize(35, 35))
        self.button_back_gtgv.setObjectName("button_back_gtgv")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 10, 501, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 80, 451, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.inp_cgv = QtWidgets.QLineEdit(self.frame)
        self.inp_cgv.setGeometry(QtCore.QRect(190, 39, 220, 31))
        self.inp_cgv.setText("")
        self.inp_cgv.setObjectName("inp_cgv")
        self.inp_tan = QtWidgets.QLineEdit(self.frame)
        self.inp_tan.setGeometry(QtCore.QRect(190, 90, 221, 31))
        self.inp_tan.setObjectName("inp_tan")
        self.inp_cotg = QtWidgets.QLineEdit(self.frame)
        self.inp_cotg.setGeometry(QtCore.QRect(190, 149, 221, 31))
        self.inp_cotg.setText("")
        self.inp_cotg.setObjectName("inp_cotg")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 161, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.label_4.setObjectName("label_4")
        self.enter1 = QtWidgets.QPushButton(self.frame)
        self.enter1.setGeometry(QtCore.QRect(120, 200, 191, 61))
        self.enter1.setObjectName("enter1")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(750, 80, 491, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.inp_ch = QtWidgets.QLineEdit(self.frame_2)
        self.inp_ch.setGeometry(QtCore.QRect(210, 36, 201, 31))
        self.inp_ch.setObjectName("inp_ch")
        self.inp_sin = QtWidgets.QLineEdit(self.frame_2)
        self.inp_sin.setGeometry(QtCore.QRect(211, 92, 201, 31))
        self.inp_sin.setObjectName("inp_sin")
        self.inp_cos = QtWidgets.QLineEdit(self.frame_2)
        self.inp_cos.setGeometry(QtCore.QRect(210, 141, 201, 31))
        self.inp_cos.setObjectName("inp_cos")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 161, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 101, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 150, 121, 31))
        self.label_7.setObjectName("label_7")
        self.enter2 = QtWidgets.QPushButton(self.frame_2)
        self.enter2.setGeometry(QtCore.QRect(140, 210, 201, 61))
        self.enter2.setObjectName("enter2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(410, 410, 521, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.out_cgv1 = QtWidgets.QLineEdit(self.frame_3)
        self.out_cgv1.setGeometry(QtCore.QRect(260, 16, 211, 21))
        self.out_cgv1.setText("")
        self.out_cgv1.setObjectName("out_cgv1")
        self.out_cgv2 = QtWidgets.QLineEdit(self.frame_3)
        self.out_cgv2.setGeometry(QtCore.QRect(260, 60, 211, 21))
        self.out_cgv2.setText("")
        self.out_cgv2.setObjectName("out_cgv2")
        self.out_ch = QtWidgets.QLineEdit(self.frame_3)
        self.out_ch.setGeometry(QtCore.QRect(260, 100, 211, 20))
        self.out_ch.setText("")
        self.out_ch.setObjectName("out_ch")
        self.out_d = QtWidgets.QLineEdit(self.frame_3)
        self.out_d.setGeometry(QtCore.QRect(260, 140, 211, 20))
        self.out_d.setText("")
        self.out_d.setObjectName("out_d")
        self.out_k = QtWidgets.QLineEdit(self.frame_3)
        self.out_k.setGeometry(QtCore.QRect(260, 180, 211, 21))
        self.out_k.setText("")
        self.out_k.setObjectName("out_k")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 201, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 181, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 171, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(20, 170, 91, 21))
        self.label_12.setObjectName("label_12")
        self.out_kl = QtWidgets.QLineEdit(self.centralwidget)
        self.out_kl.setGeometry(QtCore.QRect(390, 650, 561, 31))
        self.out_kl.setText("")
        self.out_kl.setObjectName("out_kl")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1020, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
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
        self.enter1.clicked.connect(self.a1)
        self.enter2.clicked.connect(self.a2)

    def err(self):
        self.inp_cgv.setText(str(""))
        self.inp_tan.setText(str(""))
        self.inp_cos.setText(str(""))
        self.inp_cotg.setText(str(""))
        self.inp_ch.setText(str(""))
        self.inp_sin.setText(str(""))
        self.out_cgv1.setText(str(""))
        self.out_cgv2.setText(str(""))
        self.out_ch.setText(str(""))
        self.out_d.setText(str(""))
        self.out_k.setText(str(""))
    def a1(self):
        import math
        v=0 ; d1=0 ; k1=0
        if self.inp_cgv.isModified():
            try: v=float(self.inp_cgv.text())
            except: self.out_cgv1.setText(str("không đủ giữ kiện"))
        if self.inp_tan.isModified():
            try: d1=float(self.inp_tan.text())
            except: d1=0
        if self.inp_cotg.isModified():
            try: k1=float(self.inp_cotg.text())
            except: k1=0

        if v>0 and d1>0:
            try:
                cgv=v*math.tan(d1*math.pi/180)
                hk=math.sqrt(v**2+cgv**2)
                gk=90-d1
                self.out_cgv1.setText(str(cgv))
                self.out_cgv2.setText(str(v))
                self.out_ch.setText(str(hk))
                self.out_d.setText(str(d1))
                self.out_k.setText(str(gk))
            except: self.err()

        if v>0 and k1>0:
            try:
                gd=90-k1
                cgv=v*math.tan(gd*math.pi/180)
                hk=math.sqrt(v**2+cgv**2)
                self.out_cgv1.setText(str(cgv))
                self.out_cgv2.setText(str(v))
                self.out_ch.setText(str(hk))
                self.out_d.setText(str(gd))
                self.out_k.setText(str(k1))
            except: self.err()


    def a2(self):
        ch=0 ; d2=0 ; k2=0
        import math
        if self.inp_ch.isModified():
            try: ch=float(self.inp_ch.text())
            except: ch=0 and self.out_cgv1.setText(str("không đủ giữ kiện"))
        if self.inp_sin.isModified():
            try: d2=float(self.inp_sin.text())
            except: d2=0
        if self.inp_cos.isModified():
            try: k2=float(self.inp_cos.text())
            except: k2=0

        if ch>0 and d2>0:
            try:
                cgv=ch*math.sin(d2*math.pi/180)
                cgv2=math.sqrt(ch**2-cgv**2)
                gk=90-d2
                self.out_cgv1.setText(str(cgv))
                self.out_cgv2.setText(str(cgv2))
                self.out_ch.setText(str(ch))
                self.out_d.setText(str(d2))
                self.out_k.setText(str(gk))
            except: self.err()
        if ch>0 and k2>0:
            try:
                cgv=ch*math.cos(k2*math.pi/180)
                cgv2=math.sqrt(ch**2-cgv**2)
                gd=90-k2
                self.out_cgv1.setText(str(cgv))
                self.out_cgv2.setText(str(cgv2))
                self.out_ch.setText(str(ch))
                self.out_d.setText(str(gd))
                self.out_k.setText(str(k2))
            except: 
                self.err()  
     

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giải tam giác vuông"))
        self.button_back_gtgv.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#0055ff;\">Giải tam giác vuông: </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Cạnh góc vuông:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Góc đối:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Góc kề:</span></p></body></html>"))
        self.enter1.setText(_translate("MainWindow", "Enter"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Cạnh huyền:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Góc đối:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Góc kề:</span></p></body></html>"))
        self.enter2.setText(_translate("MainWindow", "Enter"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cạnh góc vuông </span><span style=\" font-size:12pt; vertical-align:sub;\">(tìm)</span><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cạnh góc vuông:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cạnh huyền:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Góc đối:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Góc kề:</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">dev: Nguyen Trong Tuan</span></p></body></html>"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
