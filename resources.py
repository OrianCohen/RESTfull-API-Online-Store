from flask import request
from flask_restful import Resource, abort
from DAL import persistence_products, persistence_reports
from marshmallow import ValidationError
import datetime
from products_schema import ProductsSchema

class Products(Resource):
    # Get a list off all products or product by id
    def get(self, Id=None):
        if Id is None:
            return persistence_products.get_all()
        product_by_id = persistence_products.get(Id)
        if product_by_id:
            return product_by_id
        abort(404, errors={"errors": {"message": "A product with Id {} does not exist".format(Id)}})

    # Add new product to our DB
    def post(self):
        try:
            product = ProductsSchema.loads(request.json)
            if not persistence_products.create(product):
                abort(404, errors={
                    "errors": {"message": "Product with name {} already exists".format(request.json["name"])}})
        except ValidationError as e:
            abort(405, errors=e.messages)

    def put(self, Id):
        try:
            product = ProductsSchema(exclude=["id"]).loads(request.json)
            if not persistence_products.update(product, Id):
                abort(404, errors={"errors": {"message": "Product with Id {} does not exist".format(Id)}})
        except ValidationError as e:
            abort(405, errors=e.messages)

    def delete(self, Id):
        if not persistence_products.delete(Id):
            abort(404, errors={"errors": {"message": "Product with Id {} does not exist".format(Id)}})


class DataReports(Resource):
    def get(self, date=None):
        if date is None:
            all_reports = persistence_reports.get_all()
            return all_reports
        date_format = datetime(date)
        data = persistence_reports.get(date_format)
        unzipped = zip(*data.snapshot)
        unzipped_list = list(unzipped)
        return unzipped_list
