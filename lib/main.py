from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Delicious Eats")
restaurant2 = Restaurant("Tasty Bites")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

print(f"{restaurant1} average star rating: {restaurant1.average_star_rating()}")
print(f"{restaurant1} customers: {restaurant1.customers()}")
print(f"{customer1} restaurants: {', '.join(str(restaurant) for restaurant in customer1.restaurants())}")

