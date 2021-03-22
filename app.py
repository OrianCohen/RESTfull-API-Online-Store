from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
from flask_restful import Resource, Api, abort
from models import persistence_products, persistence_reports
import datetime
from databases_schema.report_schema import ReportsSchema
from resources.products import Products
from resources.reports import DataReports

app = Flask(__name__)
api = Api(app)


@app.before_first_request
def initialize_database():
    persistence_products.initialize()


@app.before_first_request
def initialize_database():
    persistence_reports.initialize()


def check_report_products():
    all_products = persistence_products.shuffle_results()
    zipped = zip(all_products)
    date = datetime.datetime.now()
    report_schema = ReportsSchema.loads(date, zipped)
    persistence_reports.create(report_schema)


api.add_resource(Products, "/products", "/products/<int:Id>")
api.add_resource(DataReports, "/reports", "/reports/<int:date>")

if __name__ == "__main__":
    cron = BackgroundScheduler(daemon=True)
    cron.add_job(check_report_products, 'interval', minutes=5)
    cron.start()
    app.run()
