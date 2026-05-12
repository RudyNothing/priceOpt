# priceOpt
An intelligent full-stack product comparison web application that fetches real-time Amazon product data, generates cross-platform price comparisons, clusters similar products, and helps users identify the best deals across platforms.

---

# Features

* Real-time Amazon product search using RapidAPI
* Simulated Flipkart comparison engine
* Intelligent product clustering
* Brand-based filtering
* Price sorting
* Query classification

  * Category Search
  * Specific Search
* Dark / Light mode
* Responsive premium UI
* Product comparison cards
* Price difference calculation
* Search result optimisation
* Cross-platform product matching

---

# Tech Stack

## Frontend

* React.js
* CSS3
* Axios

## Backend

* Flask
* Python
* RapidAPI Amazon API

---

# Project Structure

```bash id="l5dhbn"
priceOpt/
│
├── backend/
│   ├── app.py
│   ├── amazon_api.py
│   ├── cluster.py
│   ├── generator.py
│   ├── preprocess.py
│   ├── relevance.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.js
│   │   └── App.css
│   │
│   └── package.json
│
└── README.md
```

---

# Installation Guide

# 1. Clone the Repository

```bash id="54ih9y"
git clone https://github.com/yourusername/product-price-optimiser.git
```

```bash id="d0czmz"
cd product-price-optimiser
```

---

# 2. Backend Setup

Move into backend folder:

```bash id="83u3kj"
cd backend
```

Create virtual environment:

## Windows

```bash id="n8o8j5"
python -m venv venv
```

Activate virtual environment:

## Windows

```bash id="4s9g1y"
venv\Scripts\activate
```

Install dependencies:

```bash id="1lswj6"
pip install -r requirements.txt
```

---

# 3. Add RapidAPI Key

Open:

```bash id="1rjlwm"
amazon_api.py
```

Replace:

```python id="rbh87n"
API_KEY = "YOUR_API_KEY"
```

with your RapidAPI key.

---

# 4. Run Flask Backend

```bash id="smc5tv"
py app.py
```

Backend runs on:

```bash id="7n4h4t"
http://127.0.0.1:5000
```

---

# 5. Frontend Setup

Open a new terminal.

Move into frontend folder:

```bash id="v8bf6g"
cd frontend
```

Install dependencies:

```bash id="09bf50"
npm install
```

Start React app:

```bash id="thg1bx"
npm start
```

Frontend runs on:

```bash id="lfjlwm"
http://localhost:3000
```

---

# API Used

## Amazon Real-Time Data API

Source:

* RapidAPI

Features used:

* Product search
* Product title
* Price extraction
* Ratings
* Product images

---

# How It Works

1. User searches for a product
2. Flask backend fetches Amazon product data
3. Flipkart comparison products are generated dynamically
4. Products are preprocessed and normalised
5. Similar products are clustered together
6. Results are sent to React frontend
7. User can:

   * Sort by price
   * Filter by brand
   * Toggle dark/light mode
   * Compare platform prices

---

# Available Commands

## Backend

Run Flask server:

```bash id="sp2y0v"
py app.py
```

Install backend dependencies:

```bash id="a5ww4q"
pip install -r requirements.txt
```

---

## Frontend

Install dependencies:

```bash id="3pv52v"
npm install
```

Run React development server:

```bash id="5xw2bi"
npm start
```

Create production build:

```bash id="vc2gtu"
npm run build
```

---

# Future Improvements

* Real Flipkart API integration
* MongoDB search history
* AI-based recommendations
* Wishlist system
* User authentication
* Product price history graphs
* Email alerts for price drops
* Multi-platform comparison
