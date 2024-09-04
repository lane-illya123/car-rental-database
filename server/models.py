from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import MetaData
from config import db
from config import CORS


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

car_review = db.Table('car_review',
    db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'), primary_key=True),
    db.Column('review_id', db.Integer, db.ForeignKey('reviews.id'), primary_key=True),
)

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    #relationship
    reviews = db.relationship('Review', secondary=car_review, backref=db.backref('review_customers', lazy='dynamic'))
    orders = db.relationship('Order', backref='customers')

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    # Define the relationship with Customer model
    customer = db.relationship('Customer', backref='customer_orders')

    def __repr__(self):
        return f'<Order {self.id}, {self.order_number}>'

class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    make = db.Column(db.String)
    model = db.Column(db.String)
    
    # foreignKey that stores customer ID
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    #relationships
    customer = db.relationship('Customer', backref='customer_cars')

    def __repr__(self):
        return f'<Car {self.id}, {self.year}, {self.make}, {self.model}, >'

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #relationships
    customers = db.relationship('Customer', secondary=car_review, backref=db.backref('customer_reviews', lazy='dynamic'))
