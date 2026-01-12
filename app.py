from flask import Flask, render_template, request, redirect, url_for
from models import db, Asset, users

app = Flask(__name__)

# PostgreSQL DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:su@localhost:5432/AssetManagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    assets = Asset.query.all()
    return render_template('index.html', assets=assets)

@app.route('/addAsset', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        value = request.form['value']
        asset = Asset(name=name, category=category, value=value)
        db.session.add(asset)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_asset.html')

@app.route('/delete/<int:asset_id>')
def delete_asset(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    db.session.delete(asset)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addUsers', methods=['GET', 'POST'])
def add_users():
    if request.method == 'POST':
        id = request.form['employeeid']
        name = request.form['employeename']
        email = request.form['employeeemail']
        
        newUser = users(employeeID = id , employeeName = name , 
                      employeeEmailID = email )
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_users.html')

if __name__ == '__main__':
    app.run(debug=True)