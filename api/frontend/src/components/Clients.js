import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/esm/Container";

function Clients() {

    const [clients, setClients] = useState([]);

    const getClients = async () => {
        try {
            const clients = await fetch(`http://127.0.0.1:8000/client/membership/manager/4`)
            const data = await clients.json();

            setClients(data);
        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        getClients();
    }, []);

    return (
        <>
        <div className="mt-5">
            <Container>
                <div className="">
                    <h1 className="large">Clients</h1>
                </div>
            </Container>
        </div>
        </>
    )
}

export default Clients
