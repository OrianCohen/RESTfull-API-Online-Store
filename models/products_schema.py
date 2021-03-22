from marshmallow import Schema, fields, EXCLUDE


# Represent products schema database
class ProductsSchema(Schema):
    id = fields.Integer(allow_none=True)
    name = fields.Str(required=True, error_messages={"required": "A product needs at least a name"})
    amount = fields.Integer(allow_none=True)
    category = fields.Str(allow_none=True, error_messages={"required": "A Category needs at least one category"})
    class Meta:
        unknown = EXCLUDE
