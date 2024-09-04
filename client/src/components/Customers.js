import React from "react"

function Customers({customer, onDeleteCustomer}){

    function handleDeleteCustomer() {
        fetch(`http://127.0.0.1:5555/customer${customer.id}`, {
          method: "DELETE",
        })
          .then((r) => r.json())
          .then(() => onDeleteCustomer(customer.id))
          .catch((error) => console.log('Error:', error));

          console.log('Request Delete:', customer.id);
      };


return(
<section className = "cards">
    <div>
        <h3>{customer.first_name} {customer.last_name}</h3>
        <button onClick={handleDeleteCustomer}>Remove Customer</button>
    </div>
</section>
);    
}

export default Customers;