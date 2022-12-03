class House:
    def __init__(self, place, num_bedrooms, price):
        self.place = place
        self.num_bedrooms = num_bedrooms
        self.price = price
        
    def get_place(self):
        return f'Your house in {self.place} cost: {self.price}'
    
    def housing_tax(self,state):
        return f'Your taxes for your house at {state} is 6% the actual price is: {self.price*1.06}'

boston = House("Boston, Massachusets", 4, 830_000)
print(boston.get_place())
# print(boston.housing_tax("Virginia"))

housing_boston = House("Rockville, Maryland", 6, 550_000 )
print(housing_boston.get_place())
print(housing_boston.housing_tax("Rockville"))
    