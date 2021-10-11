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
                        <Link to="/" className="mx-2">Home</Link>
                        <Link to="/notifications" className="mx-2">Notifications</Link>{''}
                        <Link to="/clients" className="mx-2">Clients</Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
        </>
    )
}

export default Navigation
