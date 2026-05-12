// frontend/src/services/api.js

import axios from "axios";


const BASE_URL = "http://127.0.0.1:5000";


export const searchProducts = async (query) => {

  try {

    const response = await axios.get(
      `${BASE_URL}/search?q=${query}`
    );

    return response.data;

  } catch (error) {

    console.error(
      "API Error:",
      error
    );

    throw error;
  }
};