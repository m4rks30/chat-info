from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit, QMessageBox
from PyQt5.QtGui import QIcon

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat Window')
        self.setWindowIcon(QIcon('icon.png'))

        self.message_list = QListWidget()

        message_box = QTextEdit()
        message_box.setMaximumHeight(50)

        send_button = QPushButton('Send')
        send_button.clicked.connect(lambda: self.send_message(message_box))

        hbox = QHBoxLayout()
        hbox.addWidget(message_box)
        hbox.addWidget(send_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.message_list)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def send_message(self, message_box):
        message = message_box.toPlainText()
        if message:
            self.message_list.addItem(message)
            message_box.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a message')

if __name__ == '__main__':
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec_()
