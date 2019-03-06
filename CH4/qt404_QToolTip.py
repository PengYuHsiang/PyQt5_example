import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont,QIcon

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif',10))
		self.setToolTip('這是一格<b>氣泡提示</b>')
		self.setGeometry(200,300,400,400)
		self.setWindowTitle('氣泡提示demo')
		self.setWindowIcon(QIcon('./images/Doraemon.ico'))

if __name__=='__main__':
	app=QApplication(sys.argv)
	win=Winform()
	win.show()
	sys.exit(app.exec_())