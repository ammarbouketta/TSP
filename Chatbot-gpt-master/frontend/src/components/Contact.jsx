import React from "react";
import default_avatar from "../assets/profiles/1.jpg";
import plusIcon from "../assets/icons/plus.png";

const create_contacts = (contacts, loadMessages) => {
  return (
    <ul>
      {contacts.map((contact) => {
        return (
          <li
            className="message"
            onClick={() => {
              loadMessages(contact.messages);
            }}
          >
            <div className="avatar">
              <img
                src={contact.avatar ? contact.avatar : default_avatar}
                alt=""
              />
              <div className="connected"></div>
            </div>
            <div className="name-lastMssg">
              <h4>{contact.name}</h4>
              <p>
                {contact.messages.length > 0 &&
                  (contact.messages[contact.messages.length - 1].role == "user"
                    ? "you: "
                    : "him: ")}
                {contact.messages.length > 0 &&
                  contact.messages[contact.messages.length - 1].content.slice(
                    0,
                    15
                  )}
                ...
              </p>
            </div>
            <div className="time">
              <h4>{contact.time}</h4>
            </div>
          </li>
        );
      })}
    </ul>
  );
};

function Contact({ updateVisibility, contactList, loadMessages }) {
  return (
    <div id="contacts">
      <div id="add_user">
        <button onClick={updateVisibility}>
          <img src={plusIcon} alt="" />
        </button>
      </div>
      {create_contacts(contactList, loadMessages)}
    </div>
  );
}

export default Contact;
