import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";

function ClientDetail({ match, location }) {

    const { params: { id } } = match;
    const [clientDetail, setClientDetail] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/client/documents/client/${id}`)
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            throw response;
        })
        .then(data => {
            setClientDetail(data[0]);
        })
        .catch((error) => {
            console.log(error);
        })
    }, [id]);


    return (
        <Container>
            <div className="mt-5">
                <Card>
                    {
                        <>
                            <div className="p-4">
                                <h1 className="h5">Uploaded documents:</h1>
                                <p className="text-muted">{clientDetail.document}</p>
                            </div>
                    </>
                    }
                </Card>
            </div>
        </Container>
    )
}

export default ClientDetail
