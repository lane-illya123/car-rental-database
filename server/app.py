#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import jsonify, make_response, request
from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate

# Local imports
from config import app, db, api
#from config import CORS
# Add your model imports
from models import Customer, Car, Review

#app = Flask(__name__)
#CORS(app, origins=['http://localhost:3000'])
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.json.compact = False

#migrate = Migrate(app, db)
#db.init_app(app)
#api = Api(app)

# Views go here!

class Home(Resource):
    def get(self):

        rental_list = []
        
        for r in Car.query.all():
            rental_dict = {
                "year": r.year,
                "make": r.make,
                "model": r.model,
                }
            rental_list.append(rental_dict)

        response = make_response(
            jsonify(rental_list),
            200
            )

        return response
    
    def post(self):
        
        new_rental = Car(
            year= request.get_json("year"),
            make= request.get_json("make"),
            model= request.get_json("model"),
        )

        db.session.add(new_rental)
        db.session.commit()

        response_dict = new_rental.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response

api.add_resource(Home, '/')

class CustomerPage(Resource):
    
    def get(self):

        customer_list = []

        for c in Customer.query.all():
            customer_dict ={
            "first_name": c.first_name,
            "last_name": c.last_name,
            }
            customer_list.append(customer_dict)

        response = make_response(
        jsonify(customer_list),
            200
        )
        
        return response
    
    def post(self):
        print("Entering post() method")
        new_customer = Customer(
            first_name=request.get_json()["first_name"],
            last_name=request.get_json()["last_name"],
        )
        
        print("Request form data:", new_customer)
        db.session.add(new_customer)
        db.session.commit()

        response_dict = {
        "first_name": new_customer.first_name,
        "last_name": new_customer.last_name
        }  
        
        print("after commit:", response_dict )
        response = response_dict.to_dict()
        print("Exiting post() method")
        return response , 201
    

api.add_resource(CustomerPage,'/customer')

class ReviewPage(Resource):
    def get(self):

        review_list = []
        for rw in Review.query.all():
            review_dict = {
            "description": rw.description,
            "created_at": rw.created_at,
            "updated_at": rw.updated_at,
        }
            review_list.append(review_dict)

        response = make_response(
        jsonify(review_list),
            200
        )

        return response
    
    def post(self):
        
        new_review = Home(
            description=request.get_json("description"),
            created_at=request.get_json("created_at"),
            updated_at=request.get_json("updated_at"),
        )

        db.session.add(new_review)
        db.session.commit()

        response_dict = new_review.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response

api.add_resource(ReviewPage, '/review')

class CarByID(Resource):

    def get(self, id):

        response_dict = Car.query.filter_by(id=id).first().to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    
    def patch(self, id):

        updated_car = Car.query.filter(Review.id == id).first()
        for attr in request.form:
            setattr(updated_car, attr, request.form[attr])

        db.session.add(updated_car)
        db.session.commit()

        response_dict = updated_car.to_dict()

        response = make_response(
            response_dict,
            200
        )

        return response

api.add_resource(CarByID, '/rental/<int:id>')

class CustomerByID(Resource):

    def get(self, id):

        response_dict = Customer.query.filter_by(id=id).first().to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    
    def patch(self, id):

        updated_customer = Customer.query.filter(Customer.id == id).first()
        for attr in request.form:
            setattr(updated_customer, attr, request.form[attr])

        db.session.add(updated_customer)
        db.session.commit()

        response_dict = updated_customer.to_dict()

        response = make_response(
            response_dict,
            200
        )

        return response

    def delete(self, id):
        print('entering Delete')
        remove_customer = Customer.query.filter(Customer.id == id).first()

        db.session.delete(remove_customer)
        db.session.commit()
        print("removed_customer:", remove_customer)
        response_dict = {"message": "customer successfully deleted"}

        response = make_response(
            response_dict,
            200
        )

        return response
    
api.add_resource(CustomerByID, '/customer/<int:id>')

class ReviewByID(Resource):

    def get(self, id):

        response_dict = Review.query.filter_by(id=id).first().to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    
    def patch(self, id):

        updated_review = Review.query.filter(Review.id == id).first()
        for attr in request.form:
            setattr(updated_review, attr, request.form[attr])

        db.session.add(updated_review)
        db.session.commit()

        response_dict = updated_review.to_dict()

        response = make_response(
            response_dict,
            200
        )

        return response
    
    def delete(self, id):

        remove_review = Review.query.filter(Review.id == id).first()

        db.session.delete(remove_review)
        db.session.commit()

        response_dict = {"message": "review successfully deleted"}

        response = make_response(
            response_dict,
            200
        )

        return response
    
api.add_resource(ReviewByID, '/review/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

