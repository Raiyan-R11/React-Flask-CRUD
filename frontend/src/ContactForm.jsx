import { useState } from "react";

const ContactForm = ({ existingContact = {}, updateCallback }) => {
    const [firstName, setFirstName] = useState(existingContact.firstName || "");
    const [lastName, setLastName] = useState(existingContact.lastName || "");
    const [email, setEmail] = useState(existingContact.email || "");

    const updating = Object.entries(existingContact).length !== 0
    //if there is existing data that means we are updating
    //if not, then that means we are creating

    const onSubmit = async (e) => {
        e.preventDefault()//so page does not refresh automatically

        const data = {//data looked for in api to create contact
            firstName,
            lastName,
            email
        }
        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
        //^defining url endpoint                 ^if updating then update_contact path otherwise create
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"//let API know that json data is abt to be submitted
            },
            body: JSON.stringify(data)//converts data javascript to json
        }
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {//check if wasnt valid resp
            const data = await response.json()
            alert(data.message)//msg contains error msg
        } else {
            updateCallback()
            //^tells app.jsx component that a update/create operation
            //was done and close the modal
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="firstName">First Name:</label>
                <input
                    type="text"
                    id="firstName"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="lastName">Last Name:</label>
                <input
                    type="text"
                    id="lastName"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input
                    type="text"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <button type="submit">{updating ? "Update" : "Create"}</button>
        </form>
    );
};

export default ContactForm