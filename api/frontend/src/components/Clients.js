import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/esm/Container";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import { Link } from "react-router-dom";

function Clients() {

    const [clients, setClients] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/client/membership/manager/4`)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw response;
        })
        .then (data => {
            console.log(data);
            setClients(data);
        })
        .catch(error => {
            console.error("Error fetching data: ", error);
        })
    }, []);

    return (
        <>
        <div className="mt-5">
            <Container>
                <div className="">
                    <h1 className="large">Your Clients</h1>
                    {
                        clients.map(client => {
                            return (
                                <>
                                <Card className="w-50 my-3 shadow-sm">
                                    <div className="flex p-4 flex-inline">
                                        <h1 className="h3" key={client.client.id}>{client.client.email}</h1>
                                        <h1 className="h5 text-muted" key={client.group.client_group_name}>Date joined: {client.date_joined}</h1>
                                        <Link to="/client"><Button variant="primary">View</Button></Link>
                                    </div>
                                </Card>
                                </>
                            )
                        })
                    }
                </div>
            </Container>
        </div>
        </>
    )
}

export default Clients
