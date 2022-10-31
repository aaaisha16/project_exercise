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
        
    def enrollment(self):
        """ Determines if a parent/guardian signature is required.
        
        Side effects:
            Prints and notifies user about required signatures.
        """
        if self.age < 18:
            print("Parent and student signatures are required.")
        else:
            print("Student signature required.")
    