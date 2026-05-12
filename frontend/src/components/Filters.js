// frontend/src/components/Filters.js

import React from "react";

import "./Filters.css";

function Filters({
  sortOrder,
  setSortOrder,

  selectedBrand,
  setSelectedBrand,

  brands,
}) {
  return (
    <div className="filters-container">
      {/* SORT */}

      <select
        value={sortOrder}
        onChange={(e) => setSortOrder(e.target.value)}
        className="glass-select"
      >
        <option value="">Sort By</option>

        <option value="lowToHigh">Price: Low to High</option>

        <option value="highToLow">Price: High to Low</option>
      </select>

      {/* DYNAMIC BRANDS */}

      <select
        value={selectedBrand}
        onChange={(e) => setSelectedBrand(e.target.value.toLowerCase())}
        className="glass-select"
      >
        <option value="">All Brands</option>

        {brands.map((brand, index) => (
          <option key={index} value={brand.toLowerCase()}>
            {brand}
          </option>
        ))}
      </select>
    </div>
  );
}

export default Filters;
