import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrdersTable = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = () => {
    axios.get('http://localhost:11000/orders')
      .then((response,i) => {
        console.log(response.data[1])
        setOrders(Object.values(response.data));
      })
      .catch(error => {
        console.error('Error fetching orders:', error);
      });
  };

  console.log(Object.values(orders));
  return (
    <table>
      <thead>
        <tr>
          <th>Order ID</th>
          <th>Customer Name</th>
          <th>Status</th>
          <th>Dishes</th>
        </tr>
      </thead>
       <tbody>
       {orders?.map((orders,i) => (
           <tr key={i}>
            <td>{orders?.order_id}</td>
            <td>{orders?.customer_name}</td>
            <td>{orders?.status}</td>
            <td>
              <ul>
                {orders?.dishes?.map(dish => (
                  <li key={dish?.dish_id}>{dish?.dish_name}</li>
                ))}
              </ul>
            </td>
          </tr> 
         ))}
      </tbody> 
    </table>
  );
};

export default OrdersTable;
