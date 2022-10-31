class Practice:
    """ This class is about a student at UMD
    
    Attributes:
        name (str) = the name of the student
    
    """
    
    def information(self, name):
        """ This includes the personal information of the student such as their 
        name. 
        
        Args:
            name (str): the name of the student 
        """
        self.name = name 
        print(f"{self.name} just started attending UMD")