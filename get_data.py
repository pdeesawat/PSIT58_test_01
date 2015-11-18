import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

win = QWidget()

win.resize(320, 240) #กำหนดขนาดของหน้าต่างโปรแกรม
win.setWindowTitle("Hello, World!") #กำหนดชื่อตรงหัวโปรแกรม
win.show() #แสดง

app.exec_()