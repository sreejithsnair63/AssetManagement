from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'AssetManagement'}

    employeeID = db.Column(db.String(100), primary_key=True)
    employeeName = db.Column(db.String(100), nullable=True)
    employeeEmailID = db.Column(db.String(100), nullable=True)
    employeePhone = db.Column(db.String(100), nullable=True)  
 


class Asset(db.Model):
    __tablename__ = 'assets'
    __table_args__ = {'schema': 'AssetManagement'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    value = db.Column(db.Float, nullable=True)
    assignedTo  = db.Column(db.String, db.ForeignKey('AssetManagement.users.employeeID'), nullable=True)
    assignedUser = db.relationship('users', backref='assets', lazy=True)    
    



    

