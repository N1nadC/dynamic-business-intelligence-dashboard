def build_where_clause(filters):

    conditions = []

    if filters["years"]:
        years = ",".join(map(str, filters["years"]))
        conditions.append(
            f"CAST(strftime('%Y', o.order_date) AS INTEGER) IN ({years})"
        )

    if filters["regions"]:
        regions = "', '".join(filters["regions"])
        conditions.append(
            f"l.region IN ('{regions}')"
        )

    if filters["categories"]:
        categories = "', '".join(filters["categories"])
        conditions.append(
            f"p.category IN ('{categories}')"
        )

    if filters["subcategories"]:
        subcategories = "', '".join(filters["subcategories"])
        conditions.append(
            f"p.sub_category IN ('{subcategories}')"
        )

    if conditions:
        return "WHERE " + " AND ".join(conditions)

    return ""