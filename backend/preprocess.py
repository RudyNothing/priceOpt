# backend/preprocess.py

import re

# Common stopwords that don't add much meaning
STOPWORDS = {
    "for",
    "and",
    "with",
    "men",
    "women",
    "the",
    "a",
    "an",
    "of",
    "in",
    "on",
    "gb",
    "cm"
}

# Supported brands
BRANDS = [
    "apple",
    "nike",
    "adidas",
    "puma",
    "samsung",
    "sony",
    "bata",
    "reebok"
]


def normalize_title(title):
    """
    Normalize product title for better fuzzy matching.

    Improvements:
    - lowercase conversion
    - special character removal
    - storage normalization
    - remove unnecessary filler words
    - remove colors
    - remove stopwords
    """

    # Convert to lowercase
    title = title.lower()

    # Standardize storage formats
    title = title.replace("128 gb", "128gb")
    title = title.replace("256 gb", "256gb")
    title = title.replace("512 gb", "512gb")

    # Remove unnecessary/filler words
    removable_words = {
        "smartphone",
        "mobile",
        "phone",
        "for",
        "men",
        "women",
        "with",
        "and",
        "the",
        "a",
        "an"
    }

    # Remove color words
    color_words = {
        "black",
        "blue",
        "midnight",
        "white",
        "red",
        "green",
        "silver",
        "gold"
    }

    # Remove special characters
    title = re.sub(r'[^a-z0-9\s]', ' ', title)

    # Split into tokens
    words = title.split()

    filtered_words = []

    for word in words:

        if word in removable_words:
            continue

        if word in color_words:
            continue

        filtered_words.append(word)

    # Join words back
    normalized = " ".join(filtered_words)

    # Remove extra spaces
    normalized = re.sub(r'\s+', ' ', normalized)

    return normalized.strip()

def extract_brand(title):
    """
    Dynamically detect brand from title.
    """

    title = title.lower()

    known_brands = [

        # Phones
        "apple",
        "iphone",
        "samsung",
        "oneplus",
        "nothing",
        "realme",
        "vivo",
        "oppo",
        "iqoo",
        "motorola",
        "redmi",
        "xiaomi",
        "poco",
        "google",
        "pixel",

        # Shoes/Fashion
        "nike",
        "adidas",
        "puma",
        "bata",
        "reebok",
        "asics",
        "new balance",

        # Laptops
        "hp",
        "dell",
        "lenovo",
        "asus",
        "acer",
        "msi",
        "macbook"
    ]

    for brand in known_brands:

        if brand in title:

            # Normalize iphone -> apple
            if brand == "iphone":
                return "apple"

            if brand == "macbook":
                return "apple"

            return brand

    # Fallback:
    # first word as probable brand
    words = title.split()

    if words:
        return words[0]

    return "unknown"

def preprocess_product(product):
    """
    Add normalized title and brand info
    to a product dictionary.
    """

    product["normalized_title"] = normalize_title(
        product["title"]
    )

    product["brand"] = extract_brand(
        product["title"]
    )

    return product