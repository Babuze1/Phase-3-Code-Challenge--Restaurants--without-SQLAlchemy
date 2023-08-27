from customer import Customer
from restaurant import Restaurant

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Delicious Eats")
restaurant2 = Restaurant("Tasty Bites")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

print(restaurant1.average_star_rating()) 
print(restaurant1.customers()) 

print(customer1.restaurants()) 
