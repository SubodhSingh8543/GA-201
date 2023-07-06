// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// const MenuTable = () => {
//   const [menu, setMenu] = useState([]);

//   useEffect(() => {
//     fetchMenu();
//   }, []);

//   const fetchMenu = () => {
//     axios.get('http://localhost:11000/menu')
//       .then(response => {
//         setMenu(response.data);
//       })
//       .catch(error => {
//         console.error('Error fetching menu:', error);
//       });
//   };

//   const deleteDish = (dishId) => {
//     axios.delete(`http://localhost:11000/menu/${dishId}`)
//       .then(response => {
//         console.log(response.data);
//         fetchMenu();
//       })
//       .catch(error => {
//         console.error('Error deleting dish:', error);
//       });
//   };

//   const updateAvailability = (dishId, newAvailability) => {
//     axios.put(`http://localhost:11000/menu/${dishId}`, { availability: newAvailability })
//       .then(response => {
//         console.log(response.data);
//         fetchMenu();
//       })
//       .catch(error => {
//         console.error('Error updating availability:', error);
//       });
//   };

//   return (
//     <table>
//       <thead>
//         <tr>
//           <th>Dish ID</th>
//           <th>Dish Name</th>
//           <th>Price</th>
//           <th>Availability</th>
//           <th>Action</th>
//         </tr>
//       </thead>
//       <tbody>
//         {menu.map(dish => (
//           <tr key={dish.dish_id}>
//             <td>{dish.dish_id}</td>
//             <td>{dish.dish_name}</td>
//             <td>{dish.price}</td>
//             <td>{dish.availability}</td>
//             <td>
//               <button onClick={() => deleteDish(dish.dish_id)}>Delete</button>
//               <button onClick={() => updateAvailability(dish.dish_id, dish.availability === 'yes' ? 'no' : 'yes')}>
//                 {dish.availability === 'yes' ? 'Set Unavailable' : 'Set Available'}
//               </button>
//             </td>
//           </tr>
//         ))}
//       </tbody>
//     </table>
//   );
// };

// export default MenuTable;


import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MenuTable = () => {
  const [menu, setMenu] = useState([]);
  const [selectedDish, setSelectedDish] = useState(null);
  const [customerName, setCustomerName] = useState('');
  const [modalOpen, setModalOpen] = useState(false);

  useEffect(() => {
    fetchMenu();
  }, []);

  const fetchMenu = () => {
    axios.get('http://localhost:11000/menu')
      .then(response => {
        setMenu(response.data);
      })
      .catch(error => {
        console.error('Error fetching menu:', error);
      });
  };

  const deleteDish = (dishId) => {
    axios.delete(`http://localhost:11000/menu/${dishId}`)
      .then(response => {
        console.log(response.data);
        fetchMenu();
      })
      .catch(error => {
        console.error('Error deleting dish:', error);
      });
  };

  const updateAvailability = (dishId, newAvailability) => {
    axios.put(`http://localhost:11000/menu/${dishId}`, { availability: newAvailability })
      .then(response => {
        console.log(response.data);
        fetchMenu();
      })
      .catch(error => {
        console.error('Error updating availability:', error);
      });
  };

  const openModal = (dish) => {
    setSelectedDish(dish);
    setModalOpen(true);
  };

  const closeModal = () => {
    setSelectedDish(null);
    setCustomerName('');
    setModalOpen(false);
  };

  const placeOrder = () => {
    if (!customerName || !selectedDish) {
      return;
    }

    const payload = {
      customer_name: customerName,
      dishes: [selectedDish.dish_id]
    };

    axios.post('http://localhost:11000/orders', payload)
      .then(response => {
        console.log(response.data);
        closeModal();
      })
      .catch(error => {
        console.error('Error placing order:', error);
      });
  };

  return (
    <>
      <h1>Menu</h1>
      <table style={{marginTop:"50px"}}>
        <thead>
          <tr>
            <th>Dish ID</th>
            <th>Dish Name</th>
            <th>Price</th>
            <th>Availability</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {menu.map(dish => (
            <tr key={dish.dish_id}>
              <td>{dish.dish_id}</td>
              <td>{dish.dish_name}</td>
              <td>{dish.price}</td>
              <td>{dish.availability}</td>
              <td>
                <button onClick={() => deleteDish(dish.dish_id)}>Delete</button>
                <button onClick={() => updateAvailability(dish.dish_id, dish.availability === 'yes' ? 'no' : 'yes')}>
                  {dish.availability === 'yes' ? 'Set Unavailable' : 'Set Available'}
                </button>
                <button onClick={() => openModal(dish)}>Place Order</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {modalOpen && (
        <div className="modal">
          <div className="modal-content">
            <h3>Place Order</h3>
            <p>Product Name: {selectedDish ? selectedDish.dish_name : ''}</p>
            <input
              type="text"
              value={customerName}
              onChange={(event) => setCustomerName(event.target.value)}
              placeholder="Enter Customer Name"
            />
            <button onClick={placeOrder}>Submit</button>
            <button onClick={closeModal}>Cancel</button>
          </div>
        </div>
      )}
    </>
  );
};

export default MenuTable;
