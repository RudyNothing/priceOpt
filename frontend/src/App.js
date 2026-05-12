// frontend/src/App.js

import React, { useEffect, useState } from "react";

import "./App.css";

import SearchBar from "./components/SearchBar";

import { searchProducts } from "./services/api";

import ProductCard from "./components/ProductCard";

import Loader from "./components/Loader";

import Filters from "./components/Filters";

function App() {
  const [results, setResults] = useState([]);

  const [loading, setLoading] = useState(false);

  const [searched, setSearched] = useState(false);

  const [sortOrder, setSortOrder] = useState("");

  const [selectedBrand, setSelectedBrand] = useState("");

  const [brands, setBrands] = useState([]);

  const [queryType, setQueryType] = useState("");

  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
      setDarkMode(true);

      document.body.classList.add("dark");
    }
  }, []);

  const toggleTheme = () => {
    const newMode = !darkMode;

    setDarkMode(newMode);

    if (newMode) {
      document.body.classList.add("dark");

      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark");

      localStorage.setItem("theme", "light");
    }
  };

  const handleSearch = async (query) => {
    try {
      setLoading(true);

      setSearched(true);

      const data = await searchProducts(query);

      console.log(data);

      setResults(data.results);

      setBrands(data.brands || []);

      setQueryType(data.query_type);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  let filteredResults = [...results];

  // FILTER BY BRAND
  if (selectedBrand) {
    filteredResults = filteredResults.filter((cluster) =>
      cluster.items.some((item) => item.brand === selectedBrand),
    );
  }

  // SORTING
  if (sortOrder === "lowToHigh") {
    filteredResults.sort((a, b) => a.best_price - b.best_price);
  }

  if (sortOrder === "highToLow") {
    filteredResults.sort((a, b) => b.best_price - a.best_price);
  }

  return (
    <div className="app">
      <button className="theme-toggle" onClick={toggleTheme}>
        {darkMode ? "☀️ Light" : "🌙 Dark"}
      </button>

      <h1 className="title">PriceOpt</h1>

      <p className="subtitle">Intelligent Cross-Platform Product Comparison</p>

      <div className="search-section">
          <SearchBar onSearch={handleSearch} />

        <div className="filters-row">
          <Filters
            sortOrder={sortOrder}
            setSortOrder={setSortOrder}
            selectedBrand={selectedBrand}
            setSelectedBrand={setSelectedBrand}
            brands={brands}
          />
        </div>

        {!loading && searched && (
          <div className="results-info">
            <div className="results-count">
              Total Clusters: {filteredResults.length}
            </div>

            {queryType && (
              <div className={`query-badge ${queryType}`}>
                {queryType === "category"
                  ? "Category Search"
                  : "Specific Search"}
              </div>
            )}
          </div>
        )}
      </div>

      {!loading && searched && results.length === 0 && (
        <div className="no-results">No products found.</div>
      )}

      <div className="results-container">
        {filteredResults.map((cluster, index) => (
          <ProductCard key={index} cluster={cluster} />
        ))}
      </div>
    </div>
  );
}

export default App;
