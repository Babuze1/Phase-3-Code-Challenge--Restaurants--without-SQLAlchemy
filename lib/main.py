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

restaurant1 = Restaurant(name="Delicious Eats")
restaurant2 = Restaurant(name="Tasty Bites")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

session.add(customer1)
session.add(customer2)
session.add(restaurant1)
session.add(restaurant2)
session.commit()

restaurant = session.query(Restaurant).filter_by(name="Delicious Eats").first()
print(f"{restaurant} average star rating: {restaurant.average_star_rating()}")
print(f"{restaurant} customers: {restaurant.customers()}")

print(f"{customer1} restaurants: {', '.join(str(restaurant) for restaurant in customer1.restaurants())}")

session.close()
