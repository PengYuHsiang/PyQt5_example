import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.resize(400,200)
		self.status=self.statusBar()
		self.status.showMessage("這是狀態列提示",5000)
		self.addToolBar(QtCore.Qt.TopToolBarArea)
		self.setWindowTitle("PyQt MainWindow範例")

if __name__=="__main__":
	app=QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/cartoon1.ico"))
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())