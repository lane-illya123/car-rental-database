import {useState, useEffect} from 'react'
import NavBar from './NavBar';
import Customers from './Customers'
import CustomerForm from './CustomerForm'


function CustomerList(){
    const [customers, setCustomers] = useState([])

    useEffect(() =>{
    fetch("http://127.0.0.1:5555/customer")
      .then(r => r.json())
      .then(costumers => setCustomers(costumers))
      .catch(error => console.error(error));
  }, []);

  function handleNewCustomer(newCustomer) {
    setCustomers([...customers, newCustomer]);
  }

  function handleDeleteCustomer(deletedCustomer) {
    const rmCustomer = customers.filter((item) => item.id !== deletedCustomer.id);
    setCustomers(rmCustomer);
  }

    return(
    <>
    <div className="list-link">
      COSTUMERS:
      {customers.map((customer, index) => (
  <Customers key ={index} customer={customer} onDeleteCustomer={handleDeleteCustomer}/>
    ))}
  <CustomerForm handleNewCustomer={handleNewCustomer}/>  
</div>
</>
);

}

export default CustomerList;