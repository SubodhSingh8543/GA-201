import logo from './logo.svg';
import './App.css';
import MenuTable from './Components/MenuTable';
import OrderForm from './Components/OrderForm';
import OrdersTable from './Components/OrdersTable';
import AddProductForm from './Components/AddProduct';

function App() {
  return (
    <div className="App">
      <h1>Zesty Zomato Menu</h1>
      <AddProductForm/>
      <MenuTable />
      {/* <h1>Place an Order</h1> */}
      {/* <OrderForm /> */}
      <h1>All Orders</h1>
      <OrdersTable/>
    </div>
  );
}

export default App;
