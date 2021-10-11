import Container from "react-bootstrap/esm/Container";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import FloatingLabel from "react-bootstrap/esm/FloatingLabel";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function Home({user}) {

    // State variables
    const [show, setShow] = useState(false);
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

    // handle Modal opening and closing
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    // handle Select Change
    const handleSelectChange = event => {
        setClient(event.target.value);
    };

    // handle Request Note Change
    const handleRequestChange = event => {
        setRequestNote(event.target.value);
    }

    // handle Form submit
    const handleSubmit = event => {
        event.preventDefault();
        
        const url = "http://127.0.0.1:8000/api/manager/requests"

        // request options
        const requestOptions = {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                manager: 4,
                client,
                request_notes: requestNote
            })
        };

        fetch(url, requestOptions)
        .then((response => alert("Submitted successfully.")))
        .catch(error => console.log("Could not submit: ", error))

    };

    return (
        <Container>
                <h1 className="mt-5 mb-3 large">Welcome Back, {user}.</h1>
                
                {/* Modal starts here */}
                <Button variant="primary" onClick={handleShow} className="ml-2">
                    Create Request
                </Button>{' '}
                <Modal show={show} onHide={handleClose}>
                    <Modal.Header closeButton>
                    <Modal.Title>Create new request</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Form className="p-4" onSubmit={handleSubmit}>
                            <Form.Group className="mb-3" controlId="clientSelect">
                                <Form.Label>Clients</Form.Label>
                                <Form.Select aria-label="Default select example" onChange={handleSelectChange}>
                                    <option value="0" key="190">Choose a client</option>
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
                                    <Form.Control as="textarea" placeholder="Write your request note here." onChange={handleRequestChange} />
                                </FloatingLabel>
                            </Form.Group>
                            <Button variant="primary" type="submit">Send</Button>
                        </Form>
                    </Modal.Body>
                    <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={handleClose}>
                        Save Changes
                    </Button>
                    </Modal.Footer>
                </Modal>
                {/* Modal ends here */}

                <Link to="/clients"><Button variant="success">See Clients</Button>{' '}</Link>
        </Container>
    )
}

export default Home
