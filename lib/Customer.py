from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)

    def restaurants(self):
        restaurant_list = []
        for review in self.reviews:
            restaurant_list.append(review.restaurant)
        return list(set(restaurant_list))

    def __str__(self):
        return self.full_name()