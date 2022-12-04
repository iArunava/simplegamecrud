from app import db
from sqlalchemy.sql import func
from sqlalchemy.orm import validates

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    url = db.Column(db.String(128), index=True, nullable=False)
    author = db.Column(db.String(64), index=True, nullable=False)
    published = db.Column(db.Boolean, default=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @validates('url')
    def validate_url(self, key, value):
        print (value, not value.startswith('https://'))
        if not value.startswith('https://'):
            raise ("Validation Error")
        return value
