import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    w.move(300, 300)
    w.resize(500,500)
    w.setWindowTitle('第一个PyQt5的桌面应用')
    w.show()
    sys.exit(app.exec_())