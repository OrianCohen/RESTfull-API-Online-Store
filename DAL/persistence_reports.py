# Create the products table, will be executes before our api starts
import jaydebeapi

from report_schema import ReportsSchema


def initialize():
    _execute(("CREATE TABLE IF NOT EXISTS reports ("
              "  id INT PRIMARY KEY AUTO_INCREMENT,"
              "  date DATETIME NOT NULL,"
              "  snapshot STRING)")
             )


# Connection string and credentials to access the database server
def _execute(query, return_result=None):
    connection = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbx:h2:tcp://localhost:5234/reports",
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
    return ReportsSchema().load(column_and_values, many=True)


def get_all():
    return _execute("SELECT * FROM reports", return_result=True)


def get(date_time):
    return _execute("SELECT * FROM reports WHERE date = {}".format(date_time), return_result=True)


def create(report_product):
    columns = ", ".join(report_product.keys())
    values = ", ".join("'{}'".format(value) for value in report_product.values())
    _execute("INSERT INTO reports ({}) VALUES({})".format(columns, values))
    return {}
