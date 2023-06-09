# chat-info
A simple chat script

pip install PyQt5

pip install PyQtWebEngine

```
fuck you editor 
```

## javascript
```javascript
        import React, { useState } from 'react';

function ChatApp() {
  const [messages, setMessages] = useState([]);
  const [currentMessage, setCurrentMessage] = useState('');

  function handleSendMessage() {
    setMessages([...messages, currentMessage]);
    setCurrentMessage('');
  }

  return (
    <div>
      <div>
        {messages.map(message => <div>{message}</div>)}
      </div>
      <div>
        <input type="text" value={currentMessage} onChange={e => setCurrentMessage(e.target.value)} />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatApp;

```

## python
```python 
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
```

## python
```python 
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
```

## python
```python 
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
```
