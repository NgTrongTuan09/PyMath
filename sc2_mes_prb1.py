from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HowToDraw(object):
    def setupUi(self, HowToDraw):
        HowToDraw.setObjectName("HowToDraw")
        HowToDraw.resize(605, 356)
        HowToDraw.setStyleSheet("#gta , #hsprb , #y1 , #y2 , #y3 , #y4{font-size:23px;}")
        self.groupBox_5 = QtWidgets.QGroupBox(HowToDraw)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 200, 591, 141))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.line_37 = QtWidgets.QFrame(self.groupBox_5)
        self.line_37.setGeometry(QtCore.QRect(120, 0, 20, 131))
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.groupBox_5)
        self.line_38.setGeometry(QtCore.QRect(20, 60, 551, 20))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.groupBox_5)
        self.line_39.setGeometry(QtCore.QRect(10, 120, 571, 20))
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(self.groupBox_5)
        self.line_40.setGeometry(QtCore.QRect(10, 0, 561, 20))
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.line_41 = QtWidgets.QFrame(self.groupBox_5)
        self.line_41.setGeometry(QtCore.QRect(0, 7, 16, 121))
        self.line_41.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.line_42 = QtWidgets.QFrame(self.groupBox_5)
        self.line_42.setGeometry(QtCore.QRect(570, 10, 16, 121))
        self.line_42.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.line_43 = QtWidgets.QFrame(self.groupBox_5)
        self.line_43.setGeometry(QtCore.QRect(210, 10, 20, 121))
        self.line_43.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setObjectName("line_43")
        self.line_44 = QtWidgets.QFrame(self.groupBox_5)
        self.line_44.setGeometry(QtCore.QRect(298, 10, 20, 121))
        self.line_44.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        self.line_45 = QtWidgets.QFrame(self.groupBox_5)
        self.line_45.setGeometry(QtCore.QRect(389, 10, 20, 121))
        self.line_45.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setObjectName("line_45")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(53, 27, 31, 31))
        self.label_4.setObjectName("label_4")
        self.hsprb = QtWidgets.QLineEdit(self.groupBox_5)
        self.hsprb.setGeometry(QtCore.QRect(20, 88, 101, 31))
        self.hsprb.setText("")
        self.hsprb.setObjectName("hsprb")
        self.line_46 = QtWidgets.QFrame(self.groupBox_5)
        self.line_46.setGeometry(QtCore.QRect(481, 10, 16, 121))
        self.line_46.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_46.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_46.setObjectName("line_46")
        self.y3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.y3.setGeometry(QtCore.QRect(408, 89, 71, 31))
        self.y3.setText("")
        self.y3.setObjectName("y3")
        self.y1 = QtWidgets.QLineEdit(self.groupBox_5)
        self.y1.setGeometry(QtCore.QRect(135, 88, 71, 31))
        self.y1.setText("")
        self.y1.setObjectName("y1")
        self.y2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.y2.setGeometry(QtCore.QRect(229, 86, 71, 31))
        self.y2.setText("")
        self.y2.setObjectName("y2")
        self.y4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.y4.setGeometry(QtCore.QRect(502, 90, 61, 31))
        self.y4.setText("")
        self.y4.setObjectName("y4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(340, 27, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(339, 90, 31, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(160, 28, 31, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(250, 27, 31, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(510, 25, 31, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(421, 25, 31, 31))
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(HowToDraw)
        self.label.setGeometry(QtCore.QRect(27, 120, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(HowToDraw)
        self.label_2.setGeometry(QtCore.QRect(27, 156, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(HowToDraw)
        self.label_10.setGeometry(QtCore.QRect(140, 9, 391, 61))
        self.label_10.setObjectName("label_10")
        self.bgt_2 = QtWidgets.QPushButton(HowToDraw)
        self.bgt_2.setGeometry(QtCore.QRect(440, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bgt_2.setFont(font)
        self.bgt_2.setAutoRepeat(True)
        self.bgt_2.setObjectName("bgt_2")
        self.label_11 = QtWidgets.QLabel(HowToDraw)
        self.label_11.setGeometry(QtCore.QRect(59, 61, 191, 41))
        self.label_11.setObjectName("label_11")
        self.gta = QtWidgets.QLineEdit(HowToDraw)
        self.gta.setGeometry(QtCore.QRect(299, 66, 91, 31))
        self.gta.setText("")
        self.gta.setObjectName("gta")
        self.label_12 = QtWidgets.QLabel(HowToDraw)
        self.label_12.setGeometry(QtCore.QRect(396, 64, 41, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(HowToDraw)
        self.label_13.setGeometry(QtCore.QRect(252, 61, 41, 41))
        self.label_13.setObjectName("label_13")
        self.line = QtWidgets.QFrame(HowToDraw)
        self.line.setGeometry(QtCore.QRect(10, 110, 591, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        

        self.retranslateUi(HowToDraw)
        QtCore.QMetaObject.connectSlotsByName(HowToDraw)
        self.bgt_2.clicked.connect(self.prb1)

    def prb1(self):
        ap=float(self.gta.text())

        self.hsprb.setText(str("y=") + str(self.gta.text()) + str(" x^2"))
        hsy1=ap * (2**2)
        hsy2=ap * (1**2)
       
        self.y1.setText(f"{round(hsy1, 2):.2f}")
        self.y2.setText(f"{round(hsy2, 2):.2f}")
        self.y3.setText(f"{round(hsy2, 2):.2f}")
        self.y4.setText(f"{round(hsy1, 2):.2f}")


    def retranslateUi(self, HowToDraw):
        _translate = QtCore.QCoreApplication.translate
        HowToDraw.setWindowTitle(_translate("HowToDraw", "Cách lập bảng giá trị y=ax2"))
        self.label_4.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:18pt;\">x</span></p></body></html>"))
        self.label_3.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.label_5.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.label_6.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">-2</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.label_7.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">-1</span></p></body></html>"))
        self.label_8.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">2</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.label_9.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">1</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>"))
        self.label.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">TXĐ: R</span></p></body></html>"))
        self.label_2.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">Bảng Giá Trị:</span></p><p><br/></p></body></html>"))
        self.label_10.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:18pt;\">Cách Tạo Lập Bảng Giá Trị:</span></p></body></html>"))
        self.bgt_2.setText(_translate("HowToDraw", "Enter"))
        self.label_11.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:14pt;\">Nhập Các Giá Trị:</span></p></body></html>"))
        self.label_12.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:16pt;\">x</span><span style=\" font-size:16pt; vertical-align:super;\">2</span></p></body></html>"))
        self.label_13.setText(_translate("HowToDraw", "<html><head/><body><p><span style=\" font-size:16pt;\">y=</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HowToDraw = QtWidgets.QDialog()
    ui = Ui_HowToDraw()
    ui.setupUi(HowToDraw)
    HowToDraw.show()
    sys.exit(app.exec_())
