from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from review import Review

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    
    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def __str__(self):
        return self.full_name()

    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, rating=rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)

    def restaurants(self):
        restaurant_list = []
        for review in self.reviews:
            restaurant_list.append(review.restaurant)
        return list(set(restaurant_list))
