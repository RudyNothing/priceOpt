# backend/cluster.py

from matcher import find_best_match


def create_cluster(product):
    """
    Create a new product cluster.
    """

    return {
        "representative": product,
        "items": [product]
    }


def cluster_products(products):
    """
    Group similar products together
    using greedy clustering.
    """

    clusters = []

    for product in products:

        # Find best matching cluster
        best_cluster_index, best_score = find_best_match(
            product,
            clusters
        )

        # Add to existing cluster
        if best_cluster_index != -1:
            clusters[best_cluster_index]["items"].append(
                product
            )

        # Create new cluster
        else:
            clusters.append(
                create_cluster(product)
            )

    return clusters


def get_best_deal(cluster):
    """
    Find cheapest product inside cluster.
    """

    items = cluster["items"]

    best_item = min(
        items,
        key=lambda x: x["price"]
    )

    return {
        "product_name": cluster["representative"]["title"],
        "items": items,
        "best_platform": best_item["platform"],
        "best_price": best_item["price"]
    }


def prepare_results(clusters):
    """
    Convert raw clusters into API-ready format.
    """

    results = []

    for cluster in clusters:
        results.append(
            get_best_deal(cluster)
        )

    return results