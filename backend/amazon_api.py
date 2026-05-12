# backend/amazon_api.py

import requests

from preprocess import preprocess_product


API_KEY = "c9c675f415msh7699a7f4fb5af66p1ab844jsn7b6d03aad5c3"

API_HOST = "real-time-amazon-data.p.rapidapi.com"


# BAD KEYWORDS
# Used to remove accessories/noise

INVALID_KEYWORDS = [
    "cover",
    "charger",
    "cable",
    "adapter",
    "tempered glass",
    "screen protector",
    "screen guard",
    "back cover",
    "phone case",
    "watch strap",
    "laptop sleeve"
]

def is_valid_product(title):
    """
    Remove accessories and irrelevant products.
    """

    title = title.lower()

    for word in INVALID_KEYWORDS:

        if f" {word} " in f" {title} ":
            return False

    return True

def fetch_amazon_products(query):
    """
    Fetch live Amazon products.
    """

    url = (
        "https://real-time-amazon-data.p.rapidapi.com/search"
    )

    querystring = {

        "query": query,
        "page": "1",
        "country": "IN",
        "sort_by": "RELEVANCE",
        "product_condition": "ALL"
    }

    headers = {

        "x-rapidapi-key": API_KEY,

        "x-rapidapi-host": API_HOST
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=querystring
        )

        data = response.json()

        products = []

        amazon_products = (
            data
            .get("data", {})
            .get("products", [])
        )

        for item in amazon_products:

            title = item.get(
                "product_title",
                ""
            )

            # FILTER NOISY PRODUCTS
            if not is_valid_product(title):
                continue

            product = {

                "title":
                    title,

                "price":
                    extract_price(
                        item.get(
                            "product_price",
                            ""
                        )
                    ),

                "platform":
                    "Amazon",

                "rating":
                    parse_rating(
                        item.get(
                            "product_star_rating",
                            0
                        )
                    ),

                "link":
                    item.get(
                        "product_url",
                        ""
                    ),

                "image":
                    item.get(
                        "product_photo",
                        ""
                    )
            }

            # Skip invalid prices
            if product["price"] <= 0:
                continue

            products.append(
                preprocess_product(product)
            )

            # LIMIT RESULTS
            if len(products) >= 15:
                break

        return products

    except Exception as e:

        print(
            "Amazon API Error:",
            e
        )

        return []


def extract_price(price_text):
    """
    Convert:
    ₹79,900
    ->
    79900
    """

    try:

        cleaned = (
            str(price_text)
            .replace("₹", "")
            .replace(",", "")
            .strip()
        )

        return float(cleaned)

    except:

        return 0


def parse_rating(rating):

    try:
        return float(rating)

    except:
        return 0