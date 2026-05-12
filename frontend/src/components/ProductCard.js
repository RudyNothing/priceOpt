// frontend/src/components/ProductCard.js

import React from "react";

import "./ProductCard.css";

function ProductCard({ cluster }) {
  const prices = cluster.items.map((item) => item.price);

  const highestPrice = Math.max(...prices);

  const savings = highestPrice - cluster.best_price;

  return (
    <div className="product-card">
      <div className="product-header">
        <img
          src={cluster.items[0].image}
          alt={cluster.product_name}
          className="product-image"
        />

        <div>
          <h2 className="product-title">{cluster.product_name}</h2>
        </div>
      </div>

      <div className="best-deal">
        Best Deal: <span>{cluster.best_platform}</span> at ₹{cluster.best_price}
        {savings > 0 && <div className="savings">Save ₹{savings}</div>}
      </div>

      <div className="comparison-list">
        {cluster.items.map((item, index) => (
          <div key={index} className="comparison-item">
            <div className="platform">{item.platform}</div>

            <div className="price">₹{item.price}</div>

            <div className="rating">⭐ {item.rating}</div>

            <a
              href={item.link}
              target="_blank"
              rel="noreferrer"
              className="view-link"
            >
              View
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductCard;
