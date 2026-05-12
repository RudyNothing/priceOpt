# backend/data.py

from preprocess import preprocess_product


MOCK_PRODUCTS = [

    # =========================
    # Apple Products
    # =========================

    # {
    #     "title": "Apple iPhone 14 (128GB) Blue",
    #     "price": 69999,
    #     "platform": "Amazon",
    #     "rating": 4.5,
    #     "link": "https://amazon.in/iphone14",
    #     "image": "https://m.media-amazon.com/images/I/61bK6PMOC3L._SL1500_.jpg"
    # },

    # {
    #     "title": "APPLE iPhone 14 Blue 128 GB",
    #     "price": 68499,
    #     "platform": "Flipkart",
    #     "rating": 4.4,
    #     "link": "https://flipkart.com/iphone14",
    #     "image": "https://m.media-amazon.com/images/I/61bK6PMOC3L._SL1500_.jpg"
    # },

    # {
    #     "title": "Apple iPhone 13 Midnight 128GB",
    #     "price": 58999,
    #     "platform": "Amazon",
    #     "rating": 4.4,
    #     "link": "https://amazon.in/iphone13",
    #     "image": "https://m.media-amazon.com/images/I/71GLMJ7TQiL._SL1500_.jpg"
    # },

    # {
    #     "title": "Apple iPhone 13 128 GB Black",
    #     "price": 57499,
    #     "platform": "Flipkart",
    #     "rating": 4.3,
    #     "link": "https://flipkart.com/iphone13",
    #     "image": "https://m.media-amazon.com/images/I/71GLMJ7TQiL._SL1500_.jpg"
    # },

    # =========================
    # Nike Products
    # =========================

    # {
    #     "title": "Nike Revolution Running Shoes",
    #     "price": 2499,
    #     "platform": "Amazon",
    #     "rating": 4.2,
    #     "link": "https://amazon.in/nike-shoes",
    #     "image": "https://static.nike.com/a/images/t_default/c5f9f8b4/nike-revolution-7-road-running-shoes.png"
    # },

    # {
    #     "title": "Nike Revolution Shoes",
    #     "price": 2299,
    #     "platform": "Flipkart",
    #     "rating": 4.1,
    #     "link": "https://flipkart.com/nike-shoes",
    #     "image": "https://static.nike.com/a/images/t_default/c5f9f8b4/nike-revolution-7-road-running-shoes.png"
    # },

    # =========================
    # Adidas Products
    # =========================

    # {
    #     "title": "Adidas Sports Sneakers",
    #     "price": 3199,
    #     "platform": "Amazon",
    #     "rating": 4.3,
    #     "link": "https://amazon.in/adidas",
    #     "image": "https://assets.adidas.com/images/w_600,f_auto,q_auto/adidas-shoes.png"
    # },

    # {
    #     "title": "Adidas Sneakers for Men",
    #     "price": 3049,
    #     "platform": "Flipkart",
    #     "rating": 4.2,
    #     "link": "https://flipkart.com/adidas",
    #     "image": "https://assets.adidas.com/images/w_600,f_auto,q_auto/adidas-shoes.png"
    # },

    # =========================
    # Puma Products
    # =========================

    # {
    #     "title": "Puma Sports Shoes",
    #     "price": 1999,
    #     "platform": "Amazon",
    #     "rating": 4.1,
    #     "link": "https://amazon.in/puma",
    #     "image": "https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa/global/puma-shoes.png"
    # },

    # {
    #     "title": "Puma Running Shoes",
    #     "price": 1899,
    #     "platform": "Flipkart",
    #     "rating": 4.0,
    #     "link": "https://flipkart.com/puma",
    #     "image": "https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa/global/puma-shoes.png"
    # },

    # =========================
    # Samsung Products
    # =========================

    # {
    #     "title": "Samsung Galaxy S23 Ultra",
    #     "price": 94999,
    #     "platform": "Amazon",
    #     "rating": 4.6,
    #     "link": "https://amazon.in/s23",
    #     "image": "https://images.samsung.com/is/image/samsung/p6pim/in/2302/gallery/in-galaxy-s23-s918-sm-s918bzgcins-thumb-534863401"
    # },

    # {
    #     "title": "Samsung S23 Ultra Smartphone",
    #     "price": 92999,
    #     "platform": "Flipkart",
    #     "rating": 4.5,
    #     "link": "https://flipkart.com/s23",
    #     "image": "https://images.samsung.com/is/image/samsung/p6pim/in/2302/gallery/in-galaxy-s23-s918-sm-s918bzgcins-thumb-534863401"
    # }
]


def get_all_products():
    """
    Return all products after preprocessing.
    """

    return [
        preprocess_product(product.copy())
        for product in MOCK_PRODUCTS
    ]


def detect_query_type(query):
    """
    Detect whether query is:
    - category search
    - specific product search
    """

    query = query.lower()

    category_keywords = {
        "shoes",
        "sneakers",
        "phones",
        "smartphones",
        "mobiles",
        "running shoes"
    }

    if query in category_keywords:
        return "category"

    return "specific"


def calculate_relevance(product, query_tokens):
    """
    Calculate relevance score based on
    token overlap.
    """

    title_tokens = set(
        product["normalized_title"].split()
    )

    score = 0

    for token in query_tokens:

        if token in title_tokens:
            score += 1

    return score


def search_products(query):
    """
    Intelligent product search.
    Supports:
    - category search
    - specific search
    - partial token matching
    """

    query = query.lower().strip()

    query_type = detect_query_type(query)

    query_tokens = query.split()

    products = get_all_products()

    matched_products = []

    for product in products:

        relevance_score = calculate_relevance(
            product,
            query_tokens
        )

        # CATEGORY SEARCH
        if query_type == "category":

            category_map = {
                "shoes": [
                    "shoes",
                    "sneakers",
                    "running"
                ],

                "sneakers": [
                    "sneakers",
                    "shoes"
                ],

                "phones": [
                    "iphone",
                    "samsung",
                    "galaxy"
                ],

                "smartphones": [
                    "iphone",
                    "samsung"
                ]
            }

            keywords = category_map.get(query, [])

            for keyword in keywords:

                if keyword in product["normalized_title"]:

                    matched_products.append({
                        **product,
                        "relevance_score": relevance_score
                    })

                    break

        # SPECIFIC SEARCH
        else:

            if relevance_score > 0:

                matched_products.append({
                    **product,
                    "relevance_score": relevance_score
                })

    # Sort by relevance score
    matched_products.sort(
        key=lambda x: x["relevance_score"],
        reverse=True
    )

    return matched_products