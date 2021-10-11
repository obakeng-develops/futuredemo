import React, { useEffect, useState } from "react";
import { render } from "react-dom";
import Navigation from "./Navigation";
import Home from "./Home";
import Clients from "./Clients";
import ClientDetail from "./ClientDetail";
import Notifications from "./Notifications";
import { BrowserRouter as Router, Route } from 'react-router-dom';

export default function App() {

    // user state variable
    const [user, setUser] = useState([]);

    return (
        <>
        <Router>
        <Navigation/>
        <div className="section">
            <Route exact path="/">
                    <Home user="Vuyo"/>
            </Route>
            <Route path="/notifications" component={Notifications}/>
            <Route path="/clients" component={Clients}/>
            <Route path="/client/:id" component={ClientDetail}/>
        </div>
        </Router>
        </>
        )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);