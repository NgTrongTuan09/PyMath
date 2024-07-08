from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 100, 271, 371))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 280, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.out_a = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.out_a.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.out_a.setText("")
        self.out_a.setObjectName("out_a")
        self.out_b = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.out_b.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.out_b.setObjectName("out_b")
        self.out_c = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.out_c.setGeometry(QtCore.QRect(70, 140, 113, 20))
        self.out_c.setObjectName("out_c")
        self.out_bp = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.out_bp.setGeometry(QtCore.QRect(70, 190, 113, 20))
        self.out_bp.setObjectName("out_bp")
        self.out_cp = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.out_cp.setGeometry(QtCore.QRect(70, 240, 113, 20))
        self.out_cp.setObjectName("out_cp")
        self.out_h = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.out_h.setGeometry(QtCore.QRect(70, 290, 113, 20))
        self.out_h.setObjectName("out_h")
        self.button_back_htl = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_back_htl.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_back_htl.setFont(font)
        self.button_back_htl.setObjectName("button_back_htl")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 110, 241, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.inp_a = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inp_a.setGeometry(QtCore.QRect(50, 40, 113, 20))
        self.inp_a.setObjectName("inp_a")
        self.inp_c = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inp_c.setGeometry(QtCore.QRect(50, 130, 113, 20))
        self.inp_c.setObjectName("inp_c")
        self.inp_bp = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inp_bp.setGeometry(QtCore.QRect(50, 180, 113, 20))
        self.inp_bp.setObjectName("inp_bp")
        self.inp_cp = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inp_cp.setGeometry(QtCore.QRect(50, 230, 113, 20))
        self.inp_cp.setObjectName("inp_cp")
        self.inp_h = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inp_h.setGeometry(QtCore.QRect(50, 290, 113, 20))
        self.inp_h.setObjectName("inp_h")
        self.inp_b = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inp_b.setGeometry(QtCore.QRect(50, 90, 113, 20))
        self.inp_b.setObjectName("inp_b")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 47, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 90, 47, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(10, 130, 47, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 180, 47, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 230, 47, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(10, 290, 47, 21))
        self.label_20.setObjectName("label_20")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 20, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(760, 40, 171, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 111, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(0, 190, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(370, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_enter.setFont(font)
        self.button_enter.setObjectName("button_enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button_enter.clicked.connect(self.htluong)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kết Quả: "))
        self.label_2.setText(_translate("MainWindow", "a="))
        self.label_3.setText(_translate("MainWindow", "b="))
        self.label_4.setText(_translate("MainWindow", "c="))
        self.label_5.setText(_translate("MainWindow", "b\'="))
        self.label_6.setText(_translate("MainWindow", "c\'="))
        self.label_7.setText(_translate("MainWindow", "h="))
        self.button_back_htl.setText(_translate("MainWindow", "Back"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập Các Hệ Số: "))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">a=</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">b=</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">c=</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">b\'=</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">c\'=</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">h=</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Hệ Thức Về Cạnh Và Đường Cao Trong Tam Giác Vuông:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Công Thức:"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>(1)   b<span style=\" vertical-align:super;\">2</span>=a.b\'</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>(2)  c<span style=\" vertical-align:super;\">2</span>=a.c\'</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>(3)  b<span style=\" vertical-align:super;\">2</span>+c<span style=\" vertical-align:super;\">2</span>=a<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "(4)  b.c=a.h"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>(5)  h<span style=\" vertical-align:super;\">2</span>=b\'.c\'</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>(6)  1/h<span style=\" vertical-align:super;\">2</span> = 1/b<span style=\" vertical-align:super;\">2</span> + 1/c<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.button_enter.setText(_translate("MainWindow", "Enter -->"))

    def htluong(self):
        if self.inp_a.isModified():
            a=float(self.inp_a.text())
        else:
            a=0

        if self.inp_b.isModified():
            b=float(self.inp_b.text())
        else:
            b=0
        if self.inp_c.isModified():
            c=float(self.inp_c.text())
        else:
            c=0
        if self.inp_bp.isModified():
            bp=float(self.inp_bp.text())
        else:
            bp=0
        if self.inp_cp.isModified():
            cp=float(self.inp_cp.text())
        else:
            cp=0
        if self.inp_h.isModified():
            h=float(self.inp_h.text())
        else:
            h=0
        import math
        if a>0 and b>0 :
            ck=math.sqrt(a**2-b**2)
            bpk=b**2/a
            cpk=ck**2/a
            hk=math.sqrt(bpk*cpk)
            self.out_a.setText(str(a))
            self.out_b.setText(str(b))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(hk))
        if a>0 and c>0:
            bk=math.sqrt(a**2-c**2)
            bpk=bk**2/a 
            cpk=c**2/a
            hk=math.sqrt(bpk*cpk)
            self.out_a.setText(str(a))
            self.out_b.setText(str(bk))
            self.out_c.setText(str())
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(hk))
        if a>0 and h>0 :
            print('updating...')
        if a>0 and bp>0 or c<0 or h<0 or b<0 or cp<0:
            bk=math.sqrt(a*bp)
            ck=math.sqrt(a**2-bk**2)
            cpk=c**2/a
            hk=math.sqrt(cpk*bp)
            self.out_a.setText(str(a))
            self.out_b.setText(str(bk))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bp))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(hk))
        if a>0 and cp>0:
            bk=math.sqrt(a*cp)
            ck=math.sqrt(a**2-bk**2)
            bpk=bk**2/a
            hk=math.sqrt(bpk*cp)
            self.out_a.setText(str(a))
            self.out_b.setText(str(bk))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cp))
            self.out_h.setText(str(hk))
        if b>0 and c>0:
            ak=math.sqrt(b**2+c**2)
            bpk=b**2/ak
            cpk=c**2/ak
            hk=math.sqrt(bpk*cpk)
            self.out_a.setText(str(ak))
            self.out_b.setText(str(b))
            self.out_c.setText(str(c))
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(hk))
        if b>0 and h>0:
            bpk=math.sqrt(b**2-h**2)
            ak=b**2/bpk
            cpk=h**2/bpk
            ck=math.sqrt(ak*cpk)
            self.out_a.setText(str(ak))
            self.out_b.setText(str(b))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(h))
        if b>0 and bp>0:
            ak=b**2/bp
            ck=math.sqrt(ak**2-b**2)
            cpk=ck**2/ak
            hk=cpk*bp
            self.out_a.setText(str(ak))
            self.out_b.setText(str(b))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bp))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(hk))
        if b>0 and cp>0:
            print('updating...')
        if c>0 and h>0:
            cpk=math.sqrt(c**2-h**2)
            ak=c**2/cpk
            bpk=h**2/cpk
            bk=math.sqrt(ak*bpk)
            self.out_a.setText(str(a))
            self.out_b.setText(str(bk))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bp))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(hk))
        if c>0 and bp>0:
            print('updating..')
        if c>0 and cp>0:
            hk=math.sqrt(c**2-cp**2)
            ak=c**2/cp
            bk=math.sqrt(ak**2-c**2)
            bpk=bk**2/ak
            self.out_a.setText(str(ak))
            self.out_b.setText(str(bk))
            self.out_c.setText(str(c))
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cp))
            self.out_h.setText(str(hk))
        if h>0 and bp>0:
            cpk=h**2/bp
            ak=cpk+bp
            bk=math.sqrt(ak*bp)
            ck=math.sqrt(ak*cpk)
            self.out_a.setText(str(ak))
            self.out_b.setText(str(bk))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bp))
            self.out_cp.setText(str(cpk))
            self.out_h.setText(str(h))
        if h>0 and cp>0:
            bpk=h**2/cp
            ak=cp+bpk
            bk=math.sqrt(ak*bpk)
            ck=math.sqrt(ak*cp)
            self.out_a.setText(str(ak))
            self.out_b.setText(str(bk))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bpk))
            self.out_cp.setText(str(cp))
            self.out_h.setText(str(h))
        if bp>0 and cp>0:
            ak=bp+cp
            bk=math.sqrt(ak*bp)
            ck=math.sqrt(ak*cp)
            hk=math.sqrt(bp*cp)
            self.out_a.setText(str(ak))
            self.out_c.setText(str(ck))
            self.out_bp.setText(str(bp))
            self.out_cp.setText(str(cp))
            self.out_h.setText(str(hk))
        import sys

        def excepthook(type, value, traceback):
            print(type, value, traceback)

        sys.excepthook = excepthook




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


