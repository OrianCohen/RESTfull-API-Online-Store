from datetime import datetime

from flask_restful import Resource

from models import persistence_reports


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