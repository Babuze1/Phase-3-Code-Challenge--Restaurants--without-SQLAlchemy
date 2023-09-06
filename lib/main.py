from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from customer import Customer
from restaurant import Restaurant
from review import Review

DATABASE_URI = "sqlite:///myrestaurant.db"
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


customer1 = Customer(given_name="John", family_name="Doe")
customer2 = Customer(given_name="Jane", family_name="Smith")

session.add(customer1)
session.add(customer2)


restaurant1 = Restaurant(name="Delicious Eats")
restaurant2 = Restaurant(name="Tasty Bites")

session.add(restaurant1)
session.add(restaurant2)


review1 = Review(customer=customer1, restaurant=restaurant1, rating=4)
review2 = Review(customer=customer1, restaurant=restaurant2, rating=5)
review3 = Review(customer=customer2, restaurant=restaurant1, rating=3)

session.add(review1)
session.add(review2)
session.add(review3)

session.commit()
session.close()