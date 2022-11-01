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
    
    def school(self):
        """Where each person goes to school
        Side effects:
            prints for each student name
        """
        print(f"{self.name} goes to UMD")    
        
    def grad_year(self):
        """Determines in how many years a student will graduate
        Side Effects: 
            Determines years til graduation based on age and prints out 
        """
        if self.age == 18: 
            years = 4 
        elif self.age == 19:
            years = 3 
        elif self.age == 20:
            years = 2
        elif self.age == 21:
            years = 1 
        else: 
            year = 0 
            
        print(f"{self.name} will graduate in {years} years!")
        
    def student_ID(self, Student_ID):
        """Students UMD student ID number
        Side Effects:
            Prints student ID for a student
        """
        student_ID = "117220896"
        print(f"{self.student_ID} is {self.name} student ID number")