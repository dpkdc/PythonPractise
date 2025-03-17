class Order:
    def __init__(self,item, price):
        self.item= item
        self.price= price
    def __gt__(self,odr2):
        return self.price>odr2.price

odr1= Order("Potato", 30)
odr2=Order("Tomato", 25)
print(odr1>odr2)
#
# import json
#
# # Assuming you have a JSON file named 'data.json'
# # with the following contents:
# # {"name": "John", "age": 30, "city": "New York"}
#
# # Open the JSON file and parse its content
# with open('data.json', 'r') as file:
#     data = json.load(file)
#
# # Access data
# print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
# print(data['name'])  # Output: John
