from flask import Flask
from flask_sqlarlchemy import flask_sqlarlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///recept_fl.db'
db = SQLAlchemy(app)

class recept(db.Model):
    id = db.Column(db.Integer,primary_key=True)    
    naam = db.Column(db.String(20), unique=True, nullable = False)
    hoeveel = db.Column(db.String(100))
    foto = db.Column(db.String(100))
    typegerecht = db.Column(db.String(100))
    bereidingstijd = db.Column(db.String(100))
    landvanherkomst = db.Column(db.String(100))
    is_vegetarish = db.Column(db.Boolean)
    datum = db.Column(db.Datetime)
    ingridienten = db.relationship('ingridient', backref='nodig')
    bereidingstappen = db.relationship('bereidingsstap', backref='volg')
    apparatuur = db.relationship('extra', backref='gebruik')


class ingridient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    hoevelheid = db.Column(db.String(10))
    naam = db.Column(db.String(40))
    recept_id = db.Column(db.Integer, db.ForeignKey('recept'))


class bereidingsstap(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teksten = db.Column(db.String(200))
    recept_id = db.Column(db.Integer, db.ForeignKey('recept'))

class extra(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teksten = db.Column(db.String(200))
    recept_id = db.Column(db.Integer, db.ForeignKey('recept'))
    

    

