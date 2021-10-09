import Container from "react-bootstrap/esm/Container";
import Button from "react-bootstrap/Button";
import React from "react";
import { Link } from "react-router-dom";

function Home({user}) {
    return (
        <Container>
                <h1 className="mt-5 mb-3 large">Welcome Back, {user}.</h1>
                <Link to="/requests"><Button variant="primary">Create Request</Button>{' '}</Link>
                <Link to="/clients"><Button variant="success">See Clients</Button>{' '}</Link>
        </Container>
    )
}

export default Home
