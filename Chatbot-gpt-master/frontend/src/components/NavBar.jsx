import React from "react";
import logo from "../assets/icons/logo.png";
import searchIcon from "../assets/icons/search-interface-symbol.png";
import bellIcon from "../assets/icons/bell.png";

function NavBar() {
  return (
    <nav>
      <div id="logo">
        <img src={logo} id="logo-img" alt="" />
        <div id="logo-name">
          <h4>ChatBOT</h4>
        </div>
      </div>
      <div id="links">
        <ul>
          <li>home</li>
          <li className="selected">chat</li>
          <li>contacts</li>
          <li>settings</li>
          <li>faqs</li>
          <li>terms of use</li>
          <li className="style">
            <img src={searchIcon} alt="" />
          </li>
          <li>
            <img src={bellIcon} alt="" />
            <div className="has-notif"></div>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default NavBar;
