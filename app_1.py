import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from playsound import playsound

def window():
	app = QApplication(sys.argv)
	w = QWidget()
	b = QPushButton(w)
	b.setText("Audio Player")
	b.move(100,100)
	b.clicked.connect(showdialog)
	w.setWindowTitle("Choose an Music to Listen to")
	w.show()
	sys.exit(app.exec_())

def showdialog():
	d = QDialog()
	b1 = QPushButton("Ok", d)
	b1.move(50,50)
	d.setWindowTitle("Music List")
	d.setWindowModality(Qt.ApplicationModal)
	playsound('meek mill - YouTube.mp3'
	d.exec_()


if __name__ == '__main__':
	window()