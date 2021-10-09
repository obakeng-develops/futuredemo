import React, { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";

function Notifications() {

    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/manager/requests`).then(response => {
            if (response.ok) {
                return response.json();
            }
            throw response;
        })
        .then (data => {
            setNotifications(data);
        })
        .catch(error => {
            console.error("Error fetching data: ", error);
        })
    }, []);

    return (
        <>
        <Container>
            <div className="mt-5">
                <h1 className="large">Notifications</h1>
                <Card>
                    <div className="p-4">
                        {
                            notifications.map(notification => {
                                return (
                                    <>
                                <div className="">
                                    <h3 className="h4" key={notification.client.id}>Your client - <strong>{notification.client.email}</strong> has uploaded their documents.</h3>
                                    <Button variant="primary" key={notification.client.role}>View</Button>
                                </div>
                                </>
                                )
                            })
                        }
                    </div>
                </Card>
            </div>
        </Container>
        </>
    )
}

export default Notifications
