import React, { Component } from "react";
import { render } from "react-dom";
import Navigation from "./Navigation";

export default function App() {
    return (
        <Navigation/>
        )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);