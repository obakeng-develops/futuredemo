import React, { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";

function Notifications() {

    const [notifications, setNotifications] = useState([]);

    const getUser = async () => {
        try {
            const notifications = await fetch(`http://127.0.0.1:8000/api/manager/requests`)
            const data = await notifications.json();

            data.map(user => {
                console.log(user.request_notes);
            });

            setNotifications(data);
        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        getUser();
    }, []);

    return (
        <>
        <Container>
            <div className="mt-5">
                <h1 className="large">Notifications</h1>
                <Card>
                    <div className="p-4">
                        
                    </div>
                </Card>
            </div>
        </Container>
        </>
    )
}

export default Notifications
