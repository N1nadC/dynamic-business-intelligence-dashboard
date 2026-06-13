import pandas as pd
from sqlalchemy import create_engine

# =====================================================
# SQLITE CONNECTION
# =====================================================

engine = create_engine(
    "sqlite:///data/superstore.db"
)

# =====================================================
# LOAD CLEANED DATASET
# =====================================================

df = pd.read_csv(
    r"data\processed\superstore_cleaned.csv"
)

print("Dataset loaded successfully!")

# =====================================================
# CUSTOMERS TABLE
# =====================================================

customers_df = (
    df[['customer_id', 'customer_name', 'segment']]
    .groupby('customer_id')
    .first()
    .reset_index()
)

customers_df.to_sql(
    'customers',
    con=engine,
    if_exists='replace',
    index=False
)

print("Customers table created")

# =====================================================
# PRODUCTS TABLE
# =====================================================

products_df = (
    df[['product_id', 'product_name', 'category', 'sub_category']]
    .groupby('product_id')
    .first()
    .reset_index()
)

products_df.to_sql(
    'products',
    con=engine,
    if_exists='replace',
    index=False
)

print("Products table created")

# =====================================================
# LOCATIONS TABLE
# =====================================================
locations_df = (
    df[['country', 'city', 'state', 'postal_code', 'region']]
    .drop_duplicates()
    .reset_index(drop=True)
)

locations_df.insert(
    0,
    "location_id",
    range(1, len(locations_df) + 1)
)

locations_df.to_sql(
    'locations',
    con=engine,
    if_exists='replace',
    index=False
)

print("Locations table created")

# =====================================================
# LOCATION IDS
# =====================================================

locations_sql = pd.read_sql(
    "SELECT * FROM locations",
    con=engine
)

df = df.merge(
    locations_sql,
    on=['country', 'city', 'state', 'postal_code', 'region'],
    how='left'
)

# =====================================================
# ORDERS TABLE
# =====================================================

orders_df = (
    df[
        [
            'order_id',
            'order_date',
            'ship_date',
            'ship_mode',
            'customer_id',
            'location_id'
        ]
    ]
    .groupby('order_id')
    .first()
    .reset_index()
)

orders_df.to_sql(
    'orders',
    con=engine,
    if_exists='replace',
    index=False
)

print("Orders table created")

# =====================================================
# SALES TABLE
# =====================================================

sales_df = df[
    [
        'order_id',
        'product_id',
        'sales',
        'quantity',
        'discount',
        'profit',
        'shipping_days',
        'sales_per_unit',
        'profit_margin'
    ]
]

sales_df.to_sql(
    'sales',
    con=engine,
    if_exists='replace',
    index=False
)

print("Sales table created")

print("\nSQLite database created successfully!")