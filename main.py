from flask import Flask
from flask_cors  import CORS
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import UniqueConstraint
import requests




app = Flask(__name__)

# connect to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main' # format --> 'type_of_db://db_user:db_password@db_name/table'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configure CORS
CORS(app)

# instantiate DB
db = SQLAlchemy(app)


# create models
# @dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


# @dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/')
def index():
    return 'Hello'




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 