import React, { useEffect, useState } from "react";
import { render } from "react-dom";
import Navigation from "./Navigation";
import Container from "react-bootstrap/esm/Container";
import Button from "react-bootstrap/Button";
import LinkContainer from "react-router-bootstrap";

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
        <Navigation/>
        <div className="section">
            <Container>
                <h1 className="mt-5 mb-3 large">Welcome Back, {user}.</h1>
                <LinkContainer>
                    <Button variant="primary">Create Request</Button>{' '}
                </LinkContainer>
                <Button variant="success">See Clients</Button>{' '}
            </Container>
        </div>
        </>
        )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);