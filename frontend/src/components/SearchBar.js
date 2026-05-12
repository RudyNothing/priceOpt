import React, { useState } from "react";

function SearchBar({ onSearch }) {

  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {

    e.preventDefault();

    if (!query.trim()) return;

    onSearch(query);
  };

  return (

    <form
      className="search-form"
      onSubmit={handleSubmit}
    >

      <input
        type="text"
        placeholder="Search products..."
        className="search-input"
        value={query}
        onChange={(e) =>
          setQuery(e.target.value)
        }
      />

      <button
        type="submit"
        className="search-btn"
      >
        Search
      </button>

    </form>
  );
}

export default SearchBar;