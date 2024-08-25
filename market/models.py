from market import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)   # Changed 'column' to 'Column' and 'integer' to 'Integer'
    name = db.Column(db.String(length=30), nullable=False, unique=True)   # Changed 'string' to 'String'
    price = db.Column(db.Integer, nullable=False)   # Changed 'integer' to 'Integer'
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)   # Changed 'string' to 'String'
    description = db.Column(db.String(length=1000), nullable=False, unique=True)   # Changed 'string' to 'String'

    def __repr__(self):
        return f'Item {self.name}'




#end