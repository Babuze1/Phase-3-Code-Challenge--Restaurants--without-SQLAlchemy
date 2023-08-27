# Phase 3 Code Challenge: Restaurants- without SQLAlchemy
 
 Welcome to the Object Relations Code Challenge! In this challenge, we'll be working with a Yelp-style domain to build relationships between Restaurant, Customer, and Review classes. This README provides an overview of the project structure, the classes, methods, and how to test your code.

# Project Structure
The project is organized into three separate files, each containing a class definition:

customer.py: Contains the Customer class.
restaurant.py: Contains the Restaurant class.
review.py: Contains the Review class.
Additionally, there's a main.py file where you can test your code and interact with the classes.

# Class Descriptions
# Customer
Methods:
__init__(self, given_name, family_name): Initializes a customer with a given name and family name.
given_name(self): Returns the customer's given name.
family_name(self): Returns the customer's family name.
full_name(self): Returns the full name of the customer.
all(): Returns a list of all customer instances.
add_review(self, restaurant, rating): Adds a new review associated with the customer and a restaurant.
# Restaurant
Methods:
__init__(self, name): Initializes a restaurant with a name.
name(self): Returns the restaurant's name.
reviews(self): Returns a list of all reviews for the restaurant.
customers(self): Returns a list of unique customers who have reviewed the restaurant.
average_star_rating(self): Calculates and returns the average star rating for the restaurant.
# Review
Methods:
__init__(self, customer, restaurant, rating): Initializes a review with a customer, restaurant, and rating.
rating(self): Returns the rating of the review.
customer(self): Returns the associated customer object.
restaurant(self): Returns the associated restaurant object.
all(): Returns a list of all reviews.
# Testing Your Code
To test your code:

Run main.py to create instances, add reviews, and call methods.
Observe the output to verify that the methods produce the expected results.
Feel free to modify the main.py file to add more test cases and edge scenarios to thoroughly test your code.

# Conclusion
This code challenge provides an opportunity to practice working with object relationships, classes, and methods. As you build and test your code, make sure to follow good coding practices and test thoroughly to ensure its correctness.
