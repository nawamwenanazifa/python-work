#OOP(Modeling)
#Object Oriented Programing
#has classes and objects

#Classes
# has properties/attributes

#ie student
#first name
#lastname
#reg-no
#contact
#email
#address

#creating classes
#cohort class
#it starts with a capital letter

 #class Cohort:
    #name
    #description
    #start_date
    #end_date
    
# Questions
#with in thne cohort class, add a constructor for the cohort class
#(read about construction in w3 schools)
#add a method to  the class that prints the cohort name and total number
#of students
# create a new instance/object of the cohort class



class Cohort:
    def __init__(self, name, total_students):
        self.name = name
        self.total_students = total_students

    def print_cohort_details(self):
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of Students: {self.total_students}")

# Create a new instance of the Cohort class
cohort1 = Cohort("cohort 4", 58)

# Call the method to print cohort details
cohort1.print_cohort_details()




