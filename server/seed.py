#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import car_review
from models import Car, Customer, Review, Order

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        # Delete all rows in tables
        db.session.query(car_review).delete()
        db.session.commit()
        Customer.query.delete()
        Order.query.delete()
        Car.query.delete()
        Review.query.delete()

        # Add customer data
        customer1 = Customer(first_name=fake.first_name(), last_name=fake.last_name())
        customer2 = Customer(first_name=fake.first_name(), last_name=fake.last_name())
        customer3 = Customer(first_name=fake.first_name(), last_name=fake.last_name())

        # Add car data
        car1 = Car(year=2020, make='Ford', model='Focus', customer=customer1)
        car2 = Car(year=2019, make='Toyota', model='Camry', customer=customer2)
        car3 = Car(year=2021, make='Chevrolet', model='Cruze', customer=customer3)

        # Add Order data
        order1 = Order(order_number=fake.random_int(min=1000000000, max=9999999999), customer=customer1)
        order2 = Order(order_number=fake.random_int(min=1000000000, max=9999999999), customer=customer2)
        order3 = Order(order_number=fake.random_int(min=1000000000, max=9999999999), customer=customer3)

        # Create reviews associated with customers and cars
        review1 = Review(description='Great car!')
        review1.customers.append(customer1)

        review2 = Review(description='Smooth ride.')
        review2.customers.append(customer2)

        review3 = Review(description='Powerful engine.')
        review3.customers.append(customer3)

        # Add objects to the session
        db.session.add_all([customer1, customer2, customer3, car1, car2, car3, order1, order2, order3, review1, review2, review3])

        # Commit the session to the database
        db.session.commit()


print("Seed completed!")
