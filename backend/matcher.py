# backend/matcher.py

import re
from rapidfuzz import fuzz


SIMILARITY_THRESHOLD = 75


def similarity_score(title1, title2):
    """
    Calculate similarity score between two titles
    using token sort ratio.
    """

    return fuzz.token_sort_ratio(title1, title2)


def is_brand_match(product1, product2):
    """
    Check if brands are compatible.

    Rules:
    - Same brand → valid
    - Unknown brand → allow comparison
    - Different known brands → reject
    """

    brand1 = product1.get("brand", "unknown")
    brand2 = product2.get("brand", "unknown")

    if brand1 == "unknown" or brand2 == "unknown":
        return True

    return brand1 == brand2


def token_overlap_score(title1, title2):
    """
    Calculate token overlap percentage.
    """

    tokens1 = set(title1.split())
    tokens2 = set(title2.split())

    common = tokens1.intersection(tokens2)

    if not tokens1 or not tokens2:
        return 0

    overlap = (
        len(common) /
        max(len(tokens1), len(tokens2))
    ) * 100

    return overlap



def extract_numbers(title):
    """
    Extract all numbers from title.
    Example:
    'iphone 14 128gb'
    -> ['14', '128']
    """

    return re.findall(r'\d+', title)


def products_match(product1, product2):
    """
    Advanced product matching using:
    - brand validation
    - model number validation
    - fuzzy score
    - token overlap
    """

    # Brand validation
    if not is_brand_match(product1, product2):
        return False, 0

    title1 = product1["normalized_title"]
    title2 = product2["normalized_title"]

    # =========================
    # MODEL NUMBER VALIDATION
    # =========================

    numbers1 = extract_numbers(title1)
    numbers2 = extract_numbers(title2)

    # Compare first model number only
    if numbers1 and numbers2:

        if numbers1[0] != numbers2[0]:
            return False, 0

    # =========================
    # FUZZY MATCHING
    # =========================

    fuzzy_score = similarity_score(
        title1,
        title2
    )

    overlap_score = token_overlap_score(
        title1,
        title2
    )

    final_score = (
        (0.7 * fuzzy_score) +
        (0.3 * overlap_score)
    )

    is_match = final_score >= 70

    return is_match, round(final_score, 2)

def find_best_match(product, clusters):
    """
    Find best matching cluster for a product.

    Instead of stopping at first match,
    compare against all clusters and
    choose the highest scoring one.
    """

    best_cluster_index = -1
    best_score = 0

    for index, cluster in enumerate(clusters):

        representative = cluster["representative"]

        match, score = products_match(
            product,
            representative
        )

        if match and score > best_score:
            best_score = score
            best_cluster_index = index

    return best_cluster_index, best_score