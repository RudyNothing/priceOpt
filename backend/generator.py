# backend/generator.py

import random

from preprocess import preprocess_product


def slightly_modify_title(title):
    """
    Create realistic platform title variations.
    """

    replacements = {

        "iphone": "Apple iPhone",

        "samsung": "Samsung Galaxy",

        "oneplus": "OnePlus",

        "nothing": "Nothing Phone",

        "shoes": "Sports Shoes",

        "laptop": "Notebook"
    }

    modified = str(title)

    for key, value in replacements.items():

        modified = modified.replace(
            key,
            value
        )

    return modified


def generate_flipkart_products(amazon_products):
    """
    Generate realistic Flipkart comparison
    products from Amazon products.
    """

    generated_products = []

    for item in amazon_products:

        try:

            title = item.get("title", "")

            price = item.get("price", 0)

            rating = item.get("rating", 0)

            image = item.get("image", "")

            # SKIP INVALID PRODUCTS
            if not title:

                continue

            if not isinstance(
                price,
                (int, float)
            ):

                continue

            if price <= 0:

                continue


            # RANDOM PRICE DIFFERENCE
            difference = random.randint(
                -3000,
                3000
            )

            new_price = max(
                100,
                float(price) + difference
            )


            # RANDOM RATING SHIFT
            new_rating = round(

                min(
                    5,

                    max(
                        3,

                        float(rating)
                        +
                        random.uniform(
                            -0.4,
                            0.4
                        )
                    )
                ),

                1
            )


            generated_product = {

                "title":
                    slightly_modify_title(
                        title
                    ),

                "price":
                    new_price,

                "platform":
                    "Flipkart",

                "rating":
                    new_rating,

                "link":
                    (
                        "https://www.flipkart.com/search?q="
                        +
                        title.replace(
                            " ",
                            "%20"
                        )
                    ),

                "image":
                    image
            }


            generated_products.append(

                preprocess_product(
                    generated_product
                )
            )

        except Exception as e:

            print(
                "Generator Error:",
                e
            )

            continue


    return generated_products