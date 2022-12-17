class House:
     # Create __init__ method 
    # Set eight attributes place, bathrooms, num_bedrooms, location, price, house_type, condition
    def __init__(self, name =str, place = str,  num_bedrooms = int, location = str, price = float, house_type = str, condition = str):

        self.place = place
        self.num_bedrooms = num_bedrooms
        self.location = location
        self.price = price
        self.house_type = house_type
        self.condition = condition
        self.name = name
        
    # In this function we will get input from the user
    def house_info(self):
        self.name = str(input("What is your name: "))
        self.place = str (input(f'Hello {self.name}, what place in Maryland do you want to buy a house ? '))
        self.location = str(input(' Are you looking for a house in suburbs or city ? : '))
        self.house_type = str(input(' What type of house are you looking for (condo or single house) ? : '))
        self.condition = str(input('What condition of the house are you looking for (good or excellent) ? : '))
        self.num_bedrooms = int(input('How many bedrooms do you want in your house ? '))
        
        return self.location, self.house_type
        
        
class dwelling(House):
    #We will call the House class in the init method
    def __init__(self, name, place,  num_bedrooms = int, location = str, price = float, house_type =str, condition = str):
        super().__init__(name, place,  num_bedrooms = int, location = str, price = float, house_type =str, condition = str)
  
    #Calculate the house price based on the location
    def location_estimator(self):
        suburbs = 150_000 
        city = 250_000 
        
        if self.location == "suburbs":
            self.price = suburbs
        elif self.location == "city":
            self.price = city
    
            
        return self.price
    
    #Calculate the house price based on the home type
    def house_type_estimator (self):
        condo = 325_000
        single_house = 500_000
        if self.house_type == "condo":
            self.price += condo
        elif self.house_type == "single house":
            self.price += single_house
        return self.price
    
    #Calcualte the house price based on the condition of the house
    def condition_estimator (self):
        good = 50_000
        excellent = 75_000
        
        if self.condition == "good":
            self.price += good
            
        elif self.condition == "excellent":
            self.price += excellent
            
        return self.price
    
    #Calculate the house price based on the number of bedrooms 
    def bedroom_estimator (self):
        two_bed = 5000
        three_bed = 10000
        
        if self.num_bedrooms <= 2:
            self.price += two_bed
            
        elif self.num_bedrooms > 2 :
            self.price += three_bed
            
        return self.price
              
    #Calculate the house tax based on the total price of the house    
    def housing_tax(self):
        
        total = float(self.price*1.06)
        
        return f'The tax rate for the {self.house_type} in {self.place}, Maryland is 6%. The total price with taxes is: ${total}'
    

 # main() function print out all the methods       
def main():  
   
    dwelling_housing.house_info()
    dwelling_housing.location_estimator()
    dwelling_housing.house_type_estimator()
    dwelling_housing.condition_estimator()
    dwelling_housing.bedroom_estimator()
    print("\n")
    print(dwelling_housing.housing_tax())
    print("\n")
  
    
        
#Create instance of House class and Dwelling Class
#Call the main function
if __name__ =='__main__':
    dwelling_housing = dwelling(name = str, place = str, num_bedrooms = int, location = str, price = float,  condition = str)
    housing_location_estimator = House(name = str, place = str, num_bedrooms = int, location = str, price = float)
    main()