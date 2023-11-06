#!/usr/bin/python3
""" This module has two classes Person and student, the student inherits from person """

class Person:
    """ This class defines a person """

    def __init__(self, first_name, last_name, age):
        """ initializes the peson class """

        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_age(age)

    def get_age(self):
        """ Accessor for age """
        
        return self.age

    def set_age(self, value):
        """ Mutator for age """

        self.age = value
    
    def get_fist_name(self):
        """ Accessor for first_name """
        
        return sefl.first_name

    def set_first_name(self, value):
        """ Mutator for fist_name """

        self.first_name = value

    def get_last_name(self):
        """ Accesor for last_name """

        return self.last_name

    def set_last_name(self, value):
        """ Mutator for last_name """

        self.last_name = value

    def __str__(self):
        """ Overides the __str__() method to return a string representation of a Person instance """

        return f"My name is {self.first_name} {self.last_name} and I am {self.age} years old."


class Student(Person):
    """ A student class tha inherits from Person """

    def __init__(
                self,
                first_name,
                last_name,
                age,
                registration_number,
                department,
                hostel,
                mean_score
               ):
        """ Initializes an instance of a Student """

        super().__init__(first_name, last_name, age)

        self.set_registration_number(registration_number)
        self.set_department(department)
        self.set_hostel(hostel)
        self.set_mean_score(mean_score)

    def get_registration_number(self):
        """ Accessor for registration number """

        return self.registration_number

    def set_registration_number(self, value):
        """ Mutator for registration number """

        self.registration_number = value

    def get_department(self):
        """ Accessor for department """

        return self.department

    def set_department(self, value):
        """ Mutator for department """

        self.department = value
        
    def get_hostel(self):
        """ Accessor for hostel """

        return self.hostel

    def set_hostel(self, value):
        """ Mutator for hostel """

        self.hostel = value

    def get_mean_score(self):
        """ Accessor for mean_score """

        return self.mean_score

    def set_mean_score(self, value):
        """ Mutator for mean_score """

        self.mean_score = value
        
    def __str__(self):
        
        return super().__str__() + f" I am a student, my registration number is {self.registration_number} I am from {self.department} department I stay in {self.hostel} My mean score is {self.mean_score}"

person_1 = Person("Holland", "Naftali", 19)
student_1 = Student("Teddy", "Kochwa", 23, "COM/B/01-00164/2021", "Computer Sciece", "Hall 4", 75.23)

print(person_1)
print(student_1)
