import { BrowserRouter, Route, Link, Switch } from "react-router-dom"
import NavBar from './NavBar'
import CustomerList from "./CustomerList"
import ReviewList from "./ReviewList"
import RentalList from "./RentalList"

function App(){
    return(
        <BrowserRouter>
        <header className="nav-link">
          <NavBar/>
        </header>
        <div>
          <Switch>
            <Route path="/" exact component={RentalList} />
            <Route path="/Customers" component={CustomerList} />
            <Route path="/Reviews" component={ReviewList} />
          </Switch>
        </div>
      </BrowserRouter>
    );
}

export default App;
