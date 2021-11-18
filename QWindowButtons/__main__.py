import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from QWindowButtons import QWindowCloseButton, QWindowMinimizeButton


class Form(QMainWindow):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		self.resize(600, 400)
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setStyleSheet("QMainWindow {background-color: rgb(40, 40, 40);}")
		exit_button = QPushButton("Exit", self)
		exit_button.move(20, 350)
		exit_button.resize(exit_button.sizeHint())
		exit_button.clicked.connect(self.close)
		close_button = QWindowCloseButton(self)
		close_button.move(self.width() - close_button.width(), 0)
		close_button.clicked.connect(self.close)
		minimize_button = QWindowMinimizeButton(self)
		minimize_button.move(self.width() - close_button.width() - minimize_button.width(), 0)
		minimize_button.clicked.connect(self.showMinimized)
		self.show()


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
