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
