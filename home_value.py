class House:
    def __init__(self, place, num_bedrooms, price):
        self.place = place
        self.num_bedrooms = num_bedrooms
        self.price = price
        
    def get_place(self):
        return f'Your house in {self.place} cost: ${self.price}'
    
    def housing_tax(self,state):
        return f'Your taxes for your house at {state} is 6% the actual price is: ${self.price*1.06}'
    
class dwelling(House):
    def __init__(self, bathrooms = int, sqrt = 1_875, condition = 'good', location = 'city'):
        self.bathrooms = bathrooms
        self.sqrt_ft = sqrt
        self.condition = condition
        self.location = location
    
    def location_estimator(location):
        suburbs = 440_000
        city = 650_000
        if location == "suburbs":
            return f'your house will cost less than ${suburbs}'
        else:
            return f'Your house will cost more than ${city}'
def main(): 
    print(housing_boston.get_place())
    print(housing_boston.housing_tax("Rockville"))
    print(housing_location_estimator.location_estimator("city"))
    
if __name__ =='__main__':
    housing_boston = House("Rockville, Maryland", 6, 550_000 )
    housing_location_estimator = dwelling
    main()
