import React, { useEffect, useState } from 'react';

const Front = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = new WebSocket('ws://localhost:7000');
    newSocket.onopen = () => console.log('WebSocket connection established');
    newSocket.onmessage = (event) => {
      const message = event.data;
      setMessages((prevMessages) => [...prevMessages, message]);
    };
    newSocket.onclose = () => console.log('WebSocket connection closed');
    setSocket(newSocket);
  }, []);

  const sendMessage = () => {
    if (socket && inputValue) {
      socket.send(inputValue);
    //   setInputValue('');
    }
  };

  return (
    <div>
      <h1>Chat Frontlication</h1>
      <div>
        {messages.map((message, index) => (
          <div key={index}>{message}{index}</div>
        ))}
      </div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Front;
