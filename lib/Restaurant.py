from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship("Review", back_populates="restaurant")

    def __str__(self):
        return self.name

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)

    def customers(self):
        customer_list = []
        for review in self.reviews:
            customer_list.append(review.customer)
        return list(set(customer_list))
