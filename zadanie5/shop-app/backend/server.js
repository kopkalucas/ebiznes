const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 5001;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Przykładowe produkty
let products = [
  { id: 1, name: 'Produkt 1', price: 100 },
  { id: 2, name: 'Produkt 2', price: 200 },
  { id: 3, name: 'Produkt 3', price: 300 },
];

// Endpoint GET - zwraca produkty
app.get('/products', (req, res) => {
  res.json(products);
});

// Endpoint POST - przyjmuje dane płatności
app.post('/payments', (req, res) => {
  const paymentData = req.body;
  console.log('Otrzymano dane płatności:', paymentData);
  res.json({ status: 'success', message: 'Płatność została przyjęta' });
});

// Uruchomienie serwera
app.listen(PORT, () => {
  console.log(`Serwer działa na porcie ${PORT}`);
});
