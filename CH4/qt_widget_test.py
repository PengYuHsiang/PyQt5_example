import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QMenuBar,QMenu

class WinForm(QMainWindow):
	def __init__(self,parent=None):
		super(WinForm,self).__init__(parent)
		self.setWindowTitle("Widget Test")
		self.resize(400,300)
		screen = QDesktopWidget().size()
		size = self.size()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
		self.menubar = QMenuBar(self)
		self.menu = QMenu('File')
		self.menubar.addAction(self.menu.menuAction())
		self.setMenuBar(self.menubar)


if __name__=='__main__':
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec_())
