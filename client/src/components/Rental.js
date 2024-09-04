import React from "react"

function Rental({car}){

return(
    <section className = "cards">
    <div>
        <h3>{car.year}</h3>
        <h3>{car.make} {car.model}</h3>
    </div>
    </section>
);    
}

export default Rental;