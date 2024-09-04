import { NavLink } from "react-router-dom";

/* define the NavBar component */
function NavBar() {
    return (
      <nav>
        <NavLink
          to="/"
          /* add styling to Navlink */
          className="nav-link"
        >
          Home
        </NavLink>
        <NavLink
        to="/Customers"
        className="nav-link">
        Customer
        </NavLink>
        <NavLink
        to="/Reviews"
        className="nav-link">
        Reviews  
        </NavLink>
       
      </nav>
    );
  };
  
  export default NavBar;