import React, { useState } from 'react';

function Payments() {
  const [paymentData, setPaymentData] = useState({
    name: '',
    amount: ''
  });

  const handleChange = (e) => {
    setPaymentData({
      ...paymentData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5001/payments', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(paymentData)
      });
      const result = await response.json();
      console.log('Odpowiedź z serwera:', result);
    } catch (error) {
      console.error('Błąd podczas wysyłania płatności:', error);
    }
  };

  return (
    <div>
      <h2>Płatności</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Imię:</label>
          <input
            type="text"
            name="name"
            value={paymentData.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Kwota:</label>
          <input
            type="number"
            name="amount"
            value={paymentData.amount}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Wyślij płatność</button>
      </form>
    </div>
  );
}

export default Payments;
