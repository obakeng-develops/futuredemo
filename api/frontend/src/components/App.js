import React, { useEffect, useState } from "react";
import { render } from "react-dom";
import Navigation from "./Navigation";
import Home from "./Home";
import Container from "react-bootstrap/esm/Container";
import Button from "react-bootstrap/Button";
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';

export default function App() {

    const [user, setUser] = useState('');

    const getUser = async () => {
        try {
            const user = await fetch(`http://127.0.0.1:8000/api/user/profile/4`)
            const data = await user.json()

            setUser(data.first_name);
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
            <Switch>
                <Route path="/">
                    <Home user={user}/>
                </Route>
                <Route path="/">
                    <Home user={user}/>
                </Route>
            </Switch>
        </div>
        </Router>
        </>
        )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);