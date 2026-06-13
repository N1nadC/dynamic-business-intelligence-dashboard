import pandas as pd
from sqlalchemy import create_engine

# =====================================================
# DATABASE CONNECTION
# =====================================================

engine = create_engine(
    "mysql+pymysql://root:8766805582@localhost:3306/superstore_db"
)

# =====================================================
# LOAD CLEANED DATASET
# =====================================================

df = pd.read_csv(
    r"D:\Projects\Dynamic Business Intelligence Dashboard\data\processed\superstore_cleaned.csv"
)

print("Dataset loaded successfully!")

# =====================================================
# CUSTOMERS TABLE
# =====================================================

customers_df = df[
    ['customer_id', 'customer_name', 'segment']
]

# Keep unique customers only
customers_df = customers_df.groupby(
    'customer_id'
).first().reset_index()

print(
    "Duplicate customer IDs:",
    customers_df['customer_id'].duplicated().sum()
)

# Import into SQL
customers_df.to_sql(
    'customers',
    con=engine,
    if_exists='append',
    index=False
)

print("Customers table imported!")

# =====================================================
# PRODUCTS TABLE
# =====================================================

products_df = df[
    ['product_id', 'product_name', 'category', 'sub_category']
]

# Keep unique products only
products_df = products_df.groupby(
    'product_id'
).first().reset_index()

print(
    "Duplicate product IDs:",
    products_df['product_id'].duplicated().sum()
)

# Import into SQL
products_df.to_sql(
    'products',
    con=engine,
    if_exists='append',
    index=False
)

print("Products table imported!")

# =====================================================
# LOCATIONS TABLE
# =====================================================

locations_df = df[
    ['country', 'city', 'state', 'postal_code', 'region']
]

# Keep unique locations only
locations_df = locations_df.drop_duplicates().reset_index(drop=True)

print(
    "Duplicate locations:",
    locations_df.duplicated().sum()
)

# Import into SQL
locations_df.to_sql(
    'locations',
    con=engine,
    if_exists='append',
    index=False
)

print("Locations table imported!")

# =====================================================
# LOAD LOCATIONS TABLE FROM SQL
# =====================================================

locations_sql = pd.read_sql(
    "SELECT * FROM locations",
    con=engine
)

# =====================================================
# MAP LOCATION IDs
# =====================================================

df = df.merge(
    locations_sql,
    on=['country', 'city', 'state', 'postal_code', 'region'],
    how='left'
)

print("Location IDs mapped successfully!")

# =====================================================
# ORDERS TABLE
# =====================================================

orders_df = df[
    [
        'order_id',
        'order_date',
        'ship_date',
        'ship_mode',
        'customer_id',
        'location_id'
    ]
]

# Keep unique orders only
orders_df = orders_df.groupby(
    'order_id'
).first().reset_index()

print(
    "Duplicate order IDs:",
    orders_df['order_id'].duplicated().sum()
)

# Import into SQL
orders_df.to_sql(
    'orders',
    con=engine,
    if_exists='append',
    index=False
)

print("Orders table imported!")

print("All imports completed successfully!")

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

# Reset index for clean insertion
sales_df = sales_df.reset_index(drop=True)

print("Sales rows:", len(sales_df))

# Import into SQL
sales_df.to_sql(
    'sales',
    con=engine,
    if_exists='append',
    index=False
)

print("Sales table imported!")