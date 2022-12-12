import home_value
    
def test_house():
    '''Testing that the House class has the correct parameters'''
    home = home_value.House("Rockville, Maryland", 6, 550_000)
    assert home.place == "Rockville, Maryland", "The name may not have been set correctly"
 