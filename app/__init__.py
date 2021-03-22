import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_restful import Api
from app.report_schema import ReportsSchema
from DAL import persistence_products, persistence_reports
from .resources import DataReports, Products

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

cron = BackgroundScheduler(daemon=True)
cron.add_job(check_report_products, 'interval', minutes=5)
cron.start()
