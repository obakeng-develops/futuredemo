import React, { Component } from "react";
import { render } from "react-dom";
import Navigation from "./Navigation";
import Container from "react-bootstrap/esm/Container";

export default function App() {
    return (
        <>
        <Navigation/>
        <div className="section">
            <Container>
                <h1 className="my-5">Welcome Back, Jane.</h1>
            </Container>
        </div>
        </>
        )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);