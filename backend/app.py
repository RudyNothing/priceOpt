# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from relevance import (filter_relevant_products,detect_query_type)
from generator import generate_flipkart_products
from cluster import cluster_products, prepare_results

from amazon_api import fetch_amazon_products

app = Flask(__name__)

# Enable frontend-backend communication
CORS(app)


def extract_available_brands(clusters):

    brands = set()

    for cluster in clusters:

        for item in cluster["items"]:

            brand = item.get("brand")

            if brand:
                brands.add(brand.title())

    return sorted(list(brands))

@app.route("/")
def home():
    return {
        "message": "Product Price Optimiser API Running"
    }


@app.route("/search", methods=["GET"])
def search():

    try:

        # Get query parameter
        query = request.args.get("q")

        # Validation
        if not query:
            return jsonify({
                "success": False,
                "message": "Query parameter is required"
            }), 400

        # Fetch matching products
        # LIVE AMAZON PRODUCTS
        amazon_products = fetch_amazon_products(query)

        # MOCK FLIPKART PRODUCTS
        flipkart_products = (generate_flipkart_products(amazon_products))


        products = (amazon_products + flipkart_products)

        # FILTER IRRELEVANT PRODUCTS
        # products = filter_relevant_products(products,query)
        
        # No results found
        if not products:
            return jsonify({
                "success": True,
                "query": query,
                "query_type":detect_query_type(query),
                "total_clusters": 0,
                "brands": [],
                "results": []
            })

        # Create clusters
        clusters = cluster_products(products)

        # Prepare final API response
        results = prepare_results(clusters)

        return jsonify({
            "success": True,
            "query": query,
            "query_type": detect_query_type(query),
            "total_clusters": len(results),
            "brands": extract_available_brands(results),
            "results": results
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)