import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Modal from './Modal'; // Import your Modal component

const OrdersTable = () => {
  const [orders, setOrders] = useState([]);
  const [selectedOrderId, setSelectedOrderId] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [selectedStatus, setSelectedStatus] = useState('');

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = () => {
    axios
      .get('http://localhost:11000/orders')
      .then(response => {
        setOrders(Object.values(response.data));
      })
      .catch(error => {
        console.error('Error fetching orders:', error);
      });
  };

  const updateStatus = (orderId, status) => {
    const payload = {
      status: status,
    };

    axios
      .put(`http://localhost:11000/orders/${orderId}`, payload)
      .then(response => {
        console.log(response.data); // Handle the response from the server
        fetchOrders(); // Fetch updated orders after status update
      })
      .catch(error => {
        console.error('Error updating status:', error);
      });
  };

  const openModal = (orderId) => {
    setSelectedOrderId(orderId);
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
    setSelectedStatus('');
  };

  return (
    <table>
      <thead>
        <tr>
          <th>Order ID</th>
          <th>Customer Name</th>
          <th>Status</th>
          <th>Dishes</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {orders.map(order => (
          <tr key={order.order_id}>
            <td>{order.order_id}</td>
            <td>{order.customer_name}</td>
            <td>{order.status}</td>
            <td>
              <ul>
                {order.dishes.map(dish => (
                  <li key={dish.dish_id}>{dish.dish_name}</li>
                ))}
              </ul>
            </td>
            <td>
              <button onClick={() => updateStatus(order.order_id, 'dispatched')}>
                Dispatched
              </button>
              <button onClick={() => updateStatus(order.order_id, 'received')}>
                Received
              </button>
            </td>
          </tr>
        ))}
      </tbody>

      {modalOpen && (
        <Modal closeModal={closeModal}>
          <h2>Update Status</h2>
          <div>
            <button onClick={() => setSelectedStatus('dispatched')}>Dispatched</button>
            <button onClick={() => setSelectedStatus('received')}>Received</button>
          </div>
        </Modal>
      )}
    </table>
  );
};

export default OrdersTable;
