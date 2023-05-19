import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class Connection(QObject):
    receive_message = pyqtSignal(str)
    send_message = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.connect()

    def connect(self):
        pass
    def disconnect(self):
        pass

    def send(self, message):
        self.send_message.emit(message)
    def receive(self):
        message = "Sample message received from server"
        self.receive_message.emit(message)


class ChatClient(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat Client')

        self.status_label = QLabel(self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setText('Not Connected')
        self.message_display = QTextEdit(self)
        self.message_display.setReadOnly(True)
        self.message_input = QLineEdit(self)

        # Send button
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)
        hbox = QHBoxLayout()
        hbox.addWidget(self.message_input)
        hbox.addWidget(self.send_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.status_label)
        vbox.addWidget(self.message_display)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.connection = Connection()
        self.connection.receive_message.connect(self.receive_message)

    def send_message(self):
        message = self.message_input.text()
        self.connection.send(message)
        self.message_input.clear()

    def receive_message(self, message):
        self.message_display.append(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = ChatClient()
    client.show()
    sys.exit(app.exec_())
