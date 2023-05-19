from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Chat Window')

        button = QPushButton('Send Message', self)
        button.move(100, 150)

if __name__ == '__main__':
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec_()
