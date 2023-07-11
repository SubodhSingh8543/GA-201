import React, { useState } from 'react';
import axios from 'axios';
import "./add.css";

const AddProductForm = () => {
  const [dishId, setDishId] = useState('');
  const [dishName, setDishName] = useState('');
  const [price, setPrice] = useState('');
  const [availability, setAvailability] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const payload = {
      dish_id: parseInt(dishId),
      dish_name: dishName,
      price: parseFloat(price),
      availability: availability
    };

    // Send the POST request to the server using Axios
    axios.post('http://localhost:11000/menu', payload)
      .then(response => {
        console.log(response.data); // Handle the response from the server
      })
      .catch(error => {
        console.error('Error:', error);
      });

    // Reset the form fields
    setDishId('');
    setDishName('');
    setPrice('');
    setAvailability('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="dishId">Dish ID:</label>
        <input type="number" id="dishId" value={dishId} onChange={e => setDishId(e.target.value)} required />
      </div>
      <div>
        <label htmlFor="dishName">Dish Name:</label>
        <input type="text" id="dishName" value={dishName} onChange={e => setDishName(e.target.value)} required />
      </div>
      <div>
        <label htmlFor="price">Price:</label>
        <input type="number" id="price" value={price} onChange={e => setPrice(e.target.value)} required />
      </div>
      <div>
        <label htmlFor="availability">Availability:</label>
        <select id="availability" value={availability} onChange={e => setAvailability(e.target.value)} required>
          <option value="">Select</option>
          <option value="yes">Yes</option>
          <option value="no">No</option>
        </select>
      </div>
      <button type="submit">Add Product</button>
    </form>
  );
};

export default AddProductForm;
