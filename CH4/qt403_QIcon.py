import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon

#1 建立一個名為Icon的視窗類別 繼承QWidget類別
class Icon(QWidget):
	def __init__(self,parent=None):
		super(Icon,self).__init__(parent)
		self.initUI()

	#2 初始化視窗	
	def initUI(self):
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('展示程試圖式範例')
		self.setWindowIcon(QIcon('./images/Doraemon.ico'))

if __name__=="__main__":
	app=QApplication(sys.argv)
	win=Icon()
	win.show()
	sys.exit(app.exec_())