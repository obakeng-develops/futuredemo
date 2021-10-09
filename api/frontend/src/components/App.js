import React, { useEffect, useState } from "react";
import { render } from "react-dom";
import Navigation from "./Navigation";
import Home from "./Home";
import Clients from "./Clients";
import Request from "./Request";
import Notifications from "./Notifications";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

export default function App() {

    const [user, setUser] = useState([]);

    const getUser = async () => {
        try {
            const user = await fetch(`http://127.0.0.1:8000/api/user/profile/4`)
            const data = await user.json();

            setUser(data);
        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        getUser();
    }, []);

    return (
        <>
        <Router>
        <Navigation/>
        <div className="section">
            <Route exact path="/">
                    <Home user={user.first_name}/>
            </Route>
            <Route path="/notifications">
                    <Notifications/>
            </Route>
            <Route path="/clients">
                    <Clients/>
            </Route>
            <Route path="/request">
                    <Request/>
            </Route>
        </div>
        </Router>
        </>
        )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);