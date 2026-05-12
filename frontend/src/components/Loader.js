// frontend/src/components/Loader.js

import React from "react";

import "./Loader.css";


function Loader() {

  return (

    <div className="loader-container">

      <div className="loader"></div>

      <p className="loading-text">
        Searching best deals...
      </p>

    </div>
  );
}

export default Loader;