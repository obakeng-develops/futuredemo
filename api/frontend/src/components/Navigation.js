import React, { Component } from "react";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import { Link, NavLink } from "react-router-dom";

function Navigation() {
    return (
        <>
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="#home">FutureForex</Navbar.Brand>
                <Navbar.Toggle />
                <Navbar.Collapse className="justify-content-end">
                    <Nav className="ml-auto">
                        <Nav.Link><NavLink to="/">Home</NavLink></Nav.Link>
                        <Nav.Link><NavLink to="/notifications">Notifications</NavLink></Nav.Link>
                        <Nav.Link><Link to="/clients">Clients</Link></Nav.Link>
                        <Nav.Link><Link to="/requests">Requests</Link></Nav.Link>
                        <Nav.Link><Link to="/profile">Profile</Link></Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
        </>
    )
}

export default Navigation
