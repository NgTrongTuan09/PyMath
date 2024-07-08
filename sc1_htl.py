from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1312, 750)
        MainWindow.setStyleSheet("#button_back_htl{\n"
"font-family:century gothic;\n"
"font-size:18px;\n"
"background:rgba(170, 170, 131,0.6);\n"
"border-radius:15px;}\n"
"#button_back_htl:hover{\n"
"background-color: rgb(135, 124, 255);}\n"
"#button_enter{\n"
"background:rgb(80, 255, 130);\n"
"border-radius:15px;}\n"
"#button_enter:hover{\n"
"background-color: rgb(0, 255, 0);}\n"
"#inp_a , #inp_b , #inp_c , #inp_bp , #inp_cp , #inp_h , #out_a , #out_b , #out_c , #out_bp , #out_cp , #out_h {\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(0, 0, 255);\n"
"border-bottom:1px solid #717072;\n"
"font-size: 22px;\n"
"font-weight: 700;}\n"
"#inp_a:hover , #inp_b:hover , #inp_c:hover , #inp_bp:hover , #inp_cp:hover , #inp_h:hover , #out_a:hover , #out_b:hover , #out_c:hover , #out_bp:hover , #out_cp:hover , #out_h:hover{border-bottom:1px solid rgb(0, 255, 255);}\n"
"#error{font-size: 17px;}\n"
"#cg{font-size: 22px;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 1041, 551))
        self.label.setStyleSheet("border-image: url(:/picture/htl_new.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(142, 645, 161, 41))
        self.label_3.setObjectName("label_3")
        self.error = QtWidgets.QLineEdit(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(320, 650, 851, 31))
        self.error.setText("")
        self.error.setObjectName("error")
        self.inp_a = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_a.setGeometry(QtCore.QRect(680, 308, 121, 20))
        self.inp_a.setText("")
        self.inp_a.setObjectName("inp_a")
        self.inp_b = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_b.setGeometry(QtCore.QRect(680, 348, 121, 20))
        self.inp_b.setObjectName("inp_b")
        self.inp_c = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_c.setGeometry(QtCore.QRect(680, 386, 121, 20))
        self.inp_c.setText("")
        self.inp_c.setObjectName("inp_c")
        self.inp_bp = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_bp.setGeometry(QtCore.QRect(680, 435, 121, 20))
        self.inp_bp.setObjectName("inp_bp")
        self.inp_cp = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_cp.setGeometry(QtCore.QRect(680, 480, 121, 20))
        self.inp_cp.setObjectName("inp_cp")
        self.inp_h = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_h.setGeometry(QtCore.QRect(680, 530, 121, 20))
        self.inp_h.setObjectName("inp_h")
        self.out_a = QtWidgets.QLineEdit(self.centralwidget)
        self.out_a.setGeometry(QtCore.QRect(990, 313, 121, 20))
        self.out_a.setText("")
        self.out_a.setObjectName("out_a")
        self.out_b = QtWidgets.QLineEdit(self.centralwidget)
        self.out_b.setGeometry(QtCore.QRect(990, 350, 121, 20))
        self.out_b.setObjectName("out_b")
        self.out_c = QtWidgets.QLineEdit(self.centralwidget)
        self.out_c.setGeometry(QtCore.QRect(990, 390, 121, 20))
        self.out_c.setObjectName("out_c")
        self.out_bp = QtWidgets.QLineEdit(self.centralwidget)
        self.out_bp.setGeometry(QtCore.QRect(990, 431, 121, 20))
        self.out_bp.setObjectName("out_bp")
        self.out_cp = QtWidgets.QLineEdit(self.centralwidget)
        self.out_cp.setGeometry(QtCore.QRect(990, 485, 121, 20))
        self.out_cp.setObjectName("out_cp")
        self.out_h = QtWidgets.QLineEdit(self.centralwidget)
        self.out_h.setGeometry(QtCore.QRect(990, 530, 121, 20))
        self.out_h.setObjectName("out_h")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(280, 430, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_enter.setFont(font)
        self.button_enter.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/.icon_enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_enter.setIcon(icon)
        self.button_enter.setIconSize(QtCore.QSize(60, 60))
        self.button_enter.setObjectName("button_enter")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(980, 50, 231, 141))
        self.label_4.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.label_4.setObjectName("label_4")
        self.button_back_htl = QtWidgets.QPushButton(self.centralwidget)
        self.button_back_htl.setGeometry(QtCore.QRect(30, 20, 160, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.button_back_htl.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/.icon_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back_htl.setIcon(icon1)
        self.button_back_htl.setIconSize(QtCore.QSize(35, 35))
        self.button_back_htl.setObjectName("button_back_htl")
        self.cg = QtWidgets.QLineEdit(self.centralwidget)
        self.cg.setGeometry(QtCore.QRect(320, 600, 861, 31))
        self.cg.setText("")
        self.cg.setObjectName("cg")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 590, 161, 41))
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1020, 10, 271, 31))
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
        self.button_enter.clicked.connect(self.htluong)

    def err(self):
        self.error.setText("Bạn đã nhập sai các hệ số của tam giác vuông !")
        self.out_a.setText("")
        self.out_c.setText("")
        self.out_b.setText("")
        self.out_bp.setText("")
        self.out_cp.setText("")
        self.out_h.setText("")
        self.cg.setText("")
  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hệ Thức Lượng"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Thông Báo Lỗi:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Hãy Nhập Đúng Các</span></p><p><span style=\" font-size:14pt;\">Hệ Số Để Có Kết Quả</span></p><p><span style=\" font-size:14pt;\">Đúng Nhất!!</span></p></body></html>"))
        self.button_back_htl.setText(_translate("MainWindow", "Back"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Cách Tính:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">dev: Nguyen Trong Tuan</span></p></body></html>"))

    def htluong(self):
        import math
        a=0 ; b=0 ; c=0 ; bp=0 ; cp=0 ; h=0
        if self.inp_a.isModified():
            try: a=float(self.inp_a.text())
            except: a=0
        if self.inp_b.isModified():
            try: b=float(self.inp_b.text())
            except: b=0
        if self.inp_c.isModified():
            try: c=float(self.inp_c.text())
            except: c=0
        if self.inp_bp.isModified():
            try: bp=float(self.inp_bp.text())
            except: bp=0
        if self.inp_cp.isModified():
            try: cp=float(self.inp_cp.text())
            except: cp=0
        if self.inp_h.isModified():
            try: h=float(self.inp_h.text())
            except: h=0
        

        try:
            text_cls=str("")
            self.error.setText(text_cls)
            if a>0 and b>0 and self.inp_a.isModified() and self.inp_b.isModified() :
                try:
                    ck=(math.sqrt(a**2-b**2))
                    bpk=(b**2/a)
                    cpk=(ck**2/a)
                    hk=(math.sqrt(bpk*cpk))
                    self.out_a.setText((f"{round(a, 2):.2f}"))
                    self.out_b.setText((f"{round(b, 2):.2f}"))
                    self.out_c.setText((f"{round(ck, 2):.2f}"))
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText((f"{round(cpk, 2):.2f}"))
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính a(3), Tính b'(1), Tính c'(2), Tính h(5)"))
                except: self.err()
            if a>0 and c>0 and self.inp_a.isModified() and self.inp_c.isModified():
                try:
                    bk=math.sqrt(a**2-c**2)
                    bpk=bk**2/a 
                    cpk=c**2/a
                    hk=math.sqrt(bpk*cpk)
                    self.out_a.setText((f"{round(a, 2):.2f}"))
                    self.out_b.setText((f"{round(bk, 2):.2f}"))
                    self.out_c.setText(f"{round(c, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính b(3), Tính b'(1), Tính c'(2), Tính h(5)"))
                except: self.err()
            if a>0 and h>0 and self.inp_a.isModified() and self.inp_h.isModified():
                try:
                    delta1=float(a**4-(4*((a*h)**2)))
                    bk=math.sqrt((a**2+math.sqrt(delta1))/2)
                    ck=math.sqrt(a**2-bk**2)
                    bpk=ck**2/a
                    cpk=a-bpk
                    self.out_a.setText((f"{round(a, 2):.2f}"))
                    self.out_b.setText((f"{round(bk, 2):.2f}"))
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(h, 2):.2f}")
                    self.cg.setText(str("Trường Hợp Đặc Biệt"))
                except: self.err()
            if a>0 and bp>0 and self.inp_a.isModified() and self.inp_bp.isModified():
                try:
                    bk=math.sqrt(a*bp)
                    ck=math.sqrt(a**2-bk**2)
                    cpk=a-bp
                    hk=math.sqrt(cpk*bp)
                    self.out_a.setText(f"{round(a, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bp, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính b(1), Tính c(3), Tính c'(a-b'), Tính h(5)"))
                except: self.err()
            if a>0 and cp>0 and self.inp_a.isModified() and self.inp_cp.isModified():
                try:
                    ck=math.sqrt(a*cp)
                    bk=math.sqrt(a**2-bk**2)
                    bpk=a-cp
                    hk=math.sqrt(bpk*cp)
                    self.out_a.setText(f"{round(a, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cp, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính c(2), Tính b(3), Tính b'(a-c'), Tính h(5)"))
                except: self.err()
            if b>0 and c>0 and self.inp_b.isModified() and self.inp_c.isModified():
                try:
                    ak=math.sqrt(b**2+c**2) ; 
                    bpk=b**2/ak
                    cpk=c**2/ak
                    hk=math.sqrt(bpk*cpk)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(b, 2):.2f}")
                    self.out_c.setText(f"{round(c, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính a(3), Tính bp(1), Tính c'(2), Tính h(5)"))
                except : self.err()
            if b>0 and h>0 and self.inp_b.isModified() and self.inp_h.isModified():
                try: 
                    bpk=math.sqrt(b**2-h**2)
                    ak=b**2/bpk
                    cpk=ak-bpk
                    ck=math.sqrt(ak*cpk)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(b, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(h, 2):.2f}")
                    self.cg.setText(str("Tính b'(pytago), Tính a(1), Tính c'(a-b'), Tính c(2)"))
                except: self.err()
            if b>0 and bp>0 and self.inp_b.isModified() and self.inp_bp.isModified():
                try:
                    ak=b**2/bp
                    ck=math.sqrt(ak**2-b**2)
                    cpk=ck**2/ak
                    hk=math.sqrt(bp*cpk)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(b, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bp, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính a(1), Tính c(3), Tính c'(2), Tính h(5)"))
                except: self.err()
            if b>0 and cp>0 and self.inp_b.isModified() and self.inp_cp.isModified():
                try:
                    delta_bcp=cp**2+4*b**2
                    bpk=((-cp+math.sqrt(delta_bcp))/2)
                    ak=cp+bpk
                    hk=math.sqrt(bpk*cp)
                    ck=math.sqrt(ak*cp)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(b, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cp, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Trường Hợp Đặc Biệt"))
                except: self.err()
            if c>0 and h>0 and self.inp_c.isModified() and self.inp_h.isModified():
                try:
                    cpk=math.sqrt(c**2-h**2)
                    ak=c**2/cpk
                    bpk=h**2/cpk
                    bk=math.sqrt(ak*bpk)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(c, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(h, 2):.2f}")
                    self.cg.setText(str("Tính c'(pytago), Tính a(2), Tính b'(5), Tính b(1)"))
                except: self.err()
            if c>0 and bp>0 and self.inp_c.isModified() and self.inp_bp.isModified():
                try:
                    delta_cbp=(bp**2+4*c**2)
                    cpk=((-bp+math.sqrt(delta_cbp))/2)
                    hk=math.sqrt(cpk*bp)
                    ak=cpk+bp
                    bk=math.sqrt(bp*ak)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(c, 2):.2f}")
                    self.out_bp.setText(f"{round(bp, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Trường Hợp Đặc Biệt"))
                except: self.err()  
            if c>0 and cp>0 and self.inp_c.isModified() and self.inp_cp.isModified():
                try:
                    hk=math.sqrt(c**2-cp**2)
                    ak=c**2/cp
                    bk=math.sqrt(ak**2-c**2)
                    bpk=bk**2/ak
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(c, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cp, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính h(pytago), Tính a(2), Tính b(3), Tính b'(1)"))
                except: self.err()
            if h>0 and bp>0 and self.inp_h.isModified() and self.inp_bp.isModified():
                try:
                    cpk=h**2/bp
                    ak=cpk+bp
                    bk=math.sqrt(ak*bp)
                    ck=math.sqrt(ak*cpk)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bp, 2):.2f}")
                    self.out_cp.setText(f"{round(cpk, 2):.2f}")
                    self.out_h.setText(f"{round(h, 2):.2f}")
                    self.cg.setText(str("Tính c'(5), Tính a(b'+c'), Tính h(1), Tính c(2)"))
                except: self.err()
            if h>0 and cp>0 and self.inp_h.isModified() and self.inp_cp.isModified():
                try:
                    bpk=h**2/cp
                    ak=cp+bpk
                    bk=math.sqrt(ak*bpk)
                    ck=math.sqrt(ak*cp)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bpk, 2):.2f}")
                    self.out_cp.setText(f"{round(cp, 2):.2f}")
                    self.out_h.setText(f"{round(h, 2):.2f}")
                    self.cg.setText(str("Tính b'(5), Tính a(b'+c'), Tính b(1), Tính c(2)"))
                except: self.err()
            if bp>0 and cp>0 and self.inp_bp.isModified() and self.inp_cp.isModified():
                try:
                    ak=bp+cp
                    bk=math.sqrt(ak*bp)
                    ck=math.sqrt(ak*cp)
                    hk=math.sqrt(bp*cp)
                    self.out_a.setText(f"{round(ak, 2):.2f}")
                    self.out_b.setText(f"{round(bk, 2):.2f}")
                    self.out_c.setText(f"{round(ck, 2):.2f}")
                    self.out_bp.setText(f"{round(bp, 2):.2f}")
                    self.out_cp.setText(f"{round(cp, 2):.2f}")
                    self.out_h.setText(f"{round(hk, 2):.2f}")
                    self.cg.setText(str("Tính a(b'+c'), Tính b(1), Tính c(2), Tính h(5)"))
                except: self.err()
        except: self.err()
import sys
def excepthook(type, value, traceback):
    print(type, value, traceback)
import image_rc
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
