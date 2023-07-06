import React, { useState } from 'react';
import axios from 'axios';

const OrderForm = () => {
  const [customerName, setCustomerName] = useState('');
  const [selectedDishes, setSelectedDishes] = useState([]);

  const handleCustomerNameChange = event => {
    setCustomerName(event.target.value);
  };

  const handleDishSelectionChange = event => {
    const selectedOptions = Array.from(event.target.selectedOptions, option => option.value);
    setSelectedDishes(selectedOptions);
  };

  const handleSubmit = event => {
    event.preventDefault();

    const orderData = {
      customer_name: customerName,
      dishes: selectedDishes,
    };

    axios.post('http://localhost:11000/orders', orderData)
      .then(response => {
        console.log('Order placed successfully:', response.data);
      })
      .catch(error => {
        console.error('Error placing order:', error);
      });

    setCustomerName('');
    setSelectedDishes([]);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Customer Name:
        <input type="text" value={customerName} onChange={handleCustomerNameChange} />
      </label>
      <br />
      <label>
        Select Dishes (Hold Ctrl/Cmd to select multiple):
        <select multiple value={selectedDishes} onChange={handleDishSelectionChange}>
          {/* Replace this with the actual dish options */}
          <option value="dish1">Dish 1</option>
          <option value="dish2">Dish 2</option>
          <option value="dish3">Dish 3</option>
        </select>
      </label>
      <br />
      <button type="submit">Place Order</button>
    </form>
  );
};

export default OrderForm;
