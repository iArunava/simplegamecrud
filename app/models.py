from app import db
from sqlalchemy.sql import func

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    url = db.Column(db.String(128), index=True, nullable=False)
    published = db.Column(db.Boolean, default=False)
    time_created = Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = Column(db.DateTime(timezone=True), onupdate=func.now())
