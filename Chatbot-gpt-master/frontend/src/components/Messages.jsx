import React from "react";
import default_avatar from "../assets/profiles/1.jpg";
import animation from "../assets/icons/waiting-message.gif";

const create_messages = (messages, isTyping) => {
  let containers = messages.map((message) => {
    if (message.role === "user") {
      return (
        <li className="me" key={"me"}>
          <div className="mssg-me" key={"message_list_from_me"}>
            <div className="other-mssg" key={"me"}>
              <p>{message.content}</p>
            </div>
          </div>
        </li>
      );
    } else {
      return (
        <li className="other" key={"other"}>
          <div className="other-avatar">
            <img
              src={
                message.profile !== undefined ? message.profile : default_avatar
              }
            />
            {/* message.time */}
          </div>
          <div className="list-messages">
            <div className="other-mssg" key={"other"}>
              <p>{message.content}</p>
            </div>
          </div>
        </li>
      );
    }
  });
  if (isTyping) {
    containers.push(
      <li className="other" key={"other"}>
        <div className="list-messages">
          <div className="other-mssg" key={"other"}>
            <img src={animation} alt="" id="waiting-message" />
          </div>
        </div>
      </li>
    );
  }
  return containers;
};

function Messages({ msgList, isTyping }) {
  return <ul>{msgList.length > 0 && create_messages(msgList, isTyping)}</ul>;
}

export default Messages;
