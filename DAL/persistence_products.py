import jaydebeapi
from app.products_schema import ProductsSchema


# Create the products table, will be executes before our api starts
def initialize():
    _execute(("CREATE TABLE IF NOT EXISTS products ("
              "  id INT PRIMARY KEY AUTO_INCREMENT,"
              "  name VARCHAR NOT NULL,"
              "  amount INT,"
              "  category VARCHAR NOT NULL)")
             )


# Connection string and credentials to access the database server
def _execute(query, return_result=None):
    connection = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbx:h2:tcp://localhost:5234/products",
        ["SA", ""],
        "../h2-1.4.200.jar")

    cursor = connection.cutsor()
    cursor.execute(query)
    if return_result:
        return_result = _convert_to_schema(cursor)
    cursor.close()
    connection.close()

    return return_result


def _convert_to_schema(cursor):
    # saved in the descriptions field
    column_names = [record[0].lower() for record in cursor.description]
    column_and_values = [dict(zip(column_names, record)) for record in cursor.fetchall()]

    # takes the merged result and converts them to ExoplanetSchema objects that Flask can further process.
    return ProductsSchema().load(column_and_values, many=True)


# database functions:

#Get a list of all products in products table
def get_all():
    return _execute("SELECT * FROM products", return_result=True)


#Get a product by id
def get(product_id):
    return _execute("SELECT * FROM products WHERE id = {}".format(product_id), return_result=True)


#Add new product to products table
def create(product):
    count = _execute("SELECT count(*) AS count FROM products WHERE name LIKE '{}'".format(product.get("name")),
                     return_result=True)
    if count[0]["count"] > 0:
        return

    columns = ", ".join(product.keys())
    values = ", ".join("'{}'".format(value) for value in product.values())
    _execute("INSERT INTO products ({}) VALUES({})".format(columns, values))
    return {}


# Edit existing product by id
def update(product, product_id):
    count = _execute("SELECT count(*) AS count FROM products WHERE id = {}".format(product_id), return_result=True)
    if count[0]["count"] == 0:
        return

    values = ["'{}'".format(value) for value in product.values()]
    update_values = ", ".join("{} = {}".format(key, value) for key, value in zip(product.keys(), values))
    _execute("UPDATE products SET {} WHERE id = {}".format(update_values, product_id))
    return {}


# Delete product by id
def delete(product_id):
    count = _execute("SELECT count(*) AS count FROM products WHERE id = {}".format(product_id), return_result=True)
    if count[0]["count"] == 0:
        return

    _execute("DELETE FROM products WHERE id = {}".format(product_id))
    return {}


def shuffle_results():
    return _execute("SELECT * FROM products ORDER BY random()", return_result=True)
