import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";
import Form from "react-bootstrap/Form";
import FloatingLabel from "react-bootstrap/esm/FloatingLabel";
import Button from "react-bootstrap/Button";

function Requests() {

    const [clients, setClients] = useState([]);
    const [client, setClient] = useState(0);
    const [requestNote, setRequestNote] = useState('');

    // Fetch client data for select option
    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/client/membership/manager/4')
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            throw response;
        })
        .then(data => {
            setClients(data);
        })
        .catch(error => {
            console.error("Error fetching data: ", error);
        })
    }, []);

    const handleSelectChange = event => {
        setClient(event.target.value);
    };

    const handleSubmit = event => {
        event.preventDefault();
        alert(`${client}`);
    };

    return (
        <Container>
            <div className="mt-5">
                <h1 className="large">New Request</h1>
                <Card className="w-50 shadow-sm">
                    <Form className="p-4" onSubmit={handleSubmit}>
                        <Form.Group className="mb-3" controlId="clientSelect">
                            <Form.Label>Clients</Form.Label>
                            <Form.Select aria-label="Default select example" onChange={handleSelectChange}>
                                {
                                    clients.map(client => {
                                        return (
                                            <>
                                            <option value={client.client.id} key={client.client.email}>{client.client.email}</option>
                                            </>
                                        )
                                    })
                                }
                            </Form.Select>
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="textAreaNotes">
                            <FloatingLabel controlId="floatingTextarea" label="Write your request note here." className="mb-3 text-muted">
                                <Form.Control as="textarea" placeholder="Write your request note here." />
                            </FloatingLabel>
                        </Form.Group>
                        <Button variant="primary" type="submit">Send</Button>
                    </Form>

                </Card>
            </div>
        </Container>
    )
}

export default Requests
