class Practice:
    """ This class is about a student at UMD
    
    Attributes:
        name (str) = the name of the student
    
    """
    
    def __init__(self, name, age):
        """ This includes the personal information of the student such as their 
        name. 
        
        Args:
            name (str): the name of the student 
        """
        self.name = name 
        print(f"{self.name} just started attending UMD")
        
        self.age = age 
        print(f"{self.name} is {self.age} years old!")
        
    