import React, { useEffect, useState } from 'react';

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://localhost:5001/products'); 
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Błąd podczas pobierania produktów:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Produkty</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>{product.name} - {product.price} PLN</li>
        ))}
      </ul>
    </div>
  );
}

export default Products;
