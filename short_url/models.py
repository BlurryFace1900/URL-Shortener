from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from short_url import app
import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class urlbase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200), nullable=False)
    new_url = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self, new_url, original_url):
        self.original_url = original_url
        self.new_url = new_url

@app.before_first_request
def create_tables():
    db.create_all()