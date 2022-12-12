class Person:
    """
    Person class used as example on Sept 29 INST326 class
    
    ...
    
    Attribtes
    ---------
    x : int
        x position
    y : int
        y position
    name : str
        Person name
    age : int
        Person age
    school : str
        School attended
    distance_walked : int
        The distance that the person has walked
        
    Methods
    -------
    is_adult()
        Determines if the person is an adult
        
    walk(distance)
        Add the distance that the person walked
        
    """
    def __init__(self, name="Default Name", age=18) -> None:
        self.x = 0
        self.y = 0
        self.name = name
        self.age = age
        self.school = "UMD"
        self.distance_walked = 0
        
    def is_adult(self):
        """Calculates whether a person is an adult

        Returns:
            bool: True if the person is an adult
        """
        if self.age >= 18:
            return True
        else:
            return False
        
    def walk(self, distance):
        """_summary_

        Args:
            distance (int): the distance in steps that the person walked
        """
        self.distance_walked += distance
        
    def __repr__(self)->str:
        return f"Hi my name is {self.name} and I walked {self.distance_walked} steps."
        
if __name__ == "__main__":
    player1 = Person("George", 51)
    player1.walk(10)
    player1.walk(30)
    print(player1)