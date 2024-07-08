from PyQt5 import QtWidgets

import sys
import sc1_dths1 , sc1_gtgv , sc1_htl , sc1_hpt1 , sc1_menu ,sc1_ptb2 ,sc1_start ,sc1_tslg ,sc2_mes_dt1 , sc2_mes_prb1
ui=''
app=QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
Dialog = QtWidgets.QMainWindow()
HowToDraw = QtWidgets.QMainWindow()
app.setQuitOnLastWindowClosed(False)

def startUi():
    global ui
    ui=sc1_start.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.start.clicked.connect(menuUi)
    MainWindow.show()

def menuUi(): 
    global ui
    ui=sc1_menu.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_dothi.clicked.connect(dthsUi)
    ui.button_htluong.clicked.connect(htlUi)
    ui.button_ptb2.clicked.connect(ptb2Ui)
    ui.button_hept.clicked.connect(hptUi)
    ui.button_tslgiac.clicked.connect(tslg)
    ui.button_gtgv.clicked.connect(gtgvUi)
    ui.button_backmenu.clicked.connect(startUi)
    MainWindow.show()

def dthsUi():
    global ui
    ui=sc1_dths1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back_dths.clicked.connect(menuUi)
    ui.cachve.clicked.connect(dt)
    ui.cachve_2.clicked.connect(prb)
    MainWindow.show()

def htlUi():
    global ui
    ui=sc1_htl.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back_htl.clicked.connect(menuUi) 
    MainWindow.show()

def ptb2Ui():
    global ui
    ui=sc1_ptb2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back_ptb2.clicked.connect(menuUi) 
    MainWindow.show()

def hptUi():
    global ui
    ui=sc1_hpt1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back_hpt.clicked.connect(menuUi) 
    MainWindow.show()

def tslg():
    global ui
    ui=sc1_tslg.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back_tslg.clicked.connect(menuUi) 
    MainWindow.show()

def gtgvUi():
    global ui
    ui=sc1_gtgv.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_back_gtgv.clicked.connect(menuUi) 
    MainWindow.show()    

def dt():
    global ui
    ui=sc2_mes_dt1.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

def prb():
    global ui
    ui=sc2_mes_prb1.Ui_HowToDraw()
    ui.setupUi(HowToDraw)
    HowToDraw.show()



startUi()
sys.exit(app.exec())

#35 50 40
