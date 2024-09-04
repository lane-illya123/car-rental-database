import {useState, useEffect} from 'react'
import Rental from './Rental'
import RentalForm from './RentalForm'



function RentalList(){
    const [rentals, setRentals] = useState([])

    useEffect(() =>{
    fetch("http://127.0.0.1:5555/")
      .then(r => r.json())
      .then(rentals => setRentals(rentals))
      .catch(error => console.error(error));
  }, []);

  function handleNewRental(newRental) {
    setRentals([...rentals, newRental]);
  }

return(
  <div className="list-link">
      CARS:
      {rentals.map((item) => (
  <Rental key={item.id} car={item}/>
))}
<RentalForm handleNewRental={handleNewRental}/>
</div>
);
}

export default RentalList;