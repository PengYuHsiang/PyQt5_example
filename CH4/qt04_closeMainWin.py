from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget
import sys

class WinForm(QMainWindow):
	def __init__(self,parent=None):
		super(WinForm,self).__init__(parent)
		self.setWindowTitle('關閉主視窗範例')
		self.resize(400,150)
		self.button1 = QPushButton('關閉視窗')
		self.button1.clicked.connect(self.onButtonClick)

		layout = QHBoxLayout()
		layout.addWidget(self.button1)

		main_frame = QWidget()
		main_frame.setLayout(layout)
		self.setCentralWidget(main_frame)

	def onButtonClick(self):
		#sender 是傳送訊號的物件
		sender = self.sender()
		print(sender.text() + ' 被按下了')
		qapp = QApplication.instance()
		qapp.quit()

if __name__=="__main__":
	app = QApplication(sys.argv)
	form = WinForm()
	form.show()
	sys.exit(app.exec_())