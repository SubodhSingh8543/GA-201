import logo from './logo.svg';
import './App.css';
import MenuTable from './Components/MenuTable';
import OrdersTable from './Components/OrdersTable';
import AddProductForm from './Components/AddProduct';
import Front from './Components/front';

function App() {
  return (
    <div className="App">
      <h1>Zesty Zomato Menu</h1>
      <AddProductForm/>
      <MenuTable />
      <Front/>
      <h1>All Orders</h1>
      <OrdersTable/>
    </div>
  );
}

export default App;
