# backend/relevance.py

from rapidfuzz import fuzz

from preprocess import (
    normalize_title,
    extract_brand
)


CATEGORY_KEYWORDS = [

    "phones",
    "mobiles",
    "laptops",
    "shoes",
    "sneakers",
    "clothes",
    "watches",
    "headphones",
    "tablets"
]


def detect_query_type(query):
    """
    Detect category vs specific query.
    """

    query = query.lower()

    for keyword in CATEGORY_KEYWORDS:

        if keyword in query:
            return "category"

    return "specific"


def is_relevant_product(product, query):
    """
    Check whether product is relevant
    to user query.
    """

    query_type = detect_query_type(query)

    query_normalized = normalize_title(query)

    product_title = normalize_title(
        product["title"]
    )

    similarity = fuzz.partial_ratio(
        query_normalized,
        product_title
    )

    # CATEGORY SEARCH
    if query_type == "category":

        return similarity >= 40

    # SPECIFIC SEARCH
    else:

        query_brand = extract_brand(query)

        product_brand = product.get(
            "brand",
            "unknown"
        )

        # BRAND MUST MATCH
        if (
            query_brand != "unknown"
            and
            query_brand != product_brand
        ):
            return False

        return similarity >= 60


def filter_relevant_products(
    products,
    query
):
    """
    Filter noisy marketplace products.
    """

    filtered = []

    for product in products:

        if is_relevant_product(
            product,
            query
        ):

            filtered.append(product)

    return filtered