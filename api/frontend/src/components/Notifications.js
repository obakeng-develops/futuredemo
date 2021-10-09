import React, { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";

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
            console.log(data);
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
                        {/* {
                            notifications.map(notification => {
                                return <h1>{notification.title}</h1>
                            })
                        } */}
                    </div>
                </Card>
            </div>
        </Container>
        </>
    )
}

export default Notifications
