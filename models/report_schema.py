from marshmallow import Schema, fields, EXCLUDE


# Represent products schema database
class ReportsSchema(Schema):
    id = fields.Integer(allow_none=True)
    date = fields.DateTime
    snapshot = fields.Url(allow_none=True)
    class Meta:
        unknown = EXCLUDE
