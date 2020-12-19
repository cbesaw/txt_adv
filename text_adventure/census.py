# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:03:47 2020

@author: Claytonious
"""
#class object and manipulation example
#classes are blueprints for other objects of the same type
class Person:
    age = 15
    name = "Rolf"
    favorite_foods = ['beets', 'turnips', 'weisswurst']
    
    def birth_year():
        return 2020 - age
    
    
    
people = [Person(), Person(), Person()]

sum_ = 0
for person in people:
    sum_ = sum_ + person.age

print("The average age is: " + str(sum_ / len(people)))

#changing class object characteristics 
people = [Person(), Person(), Person()]

people[0].name = "Ed"
people[0].age = "11"
people[0].favorite_foods = ["hotdogs", "jawbreakers"]
people[1].name = "Edd"
people[1].age = "11"
people[1].favorite_foods = ["broccoli"]
people[2].name = "Eddy"
people[2].age = "12"
people[2].favorite_foods = ["chunky puffs", "jawbreakers"]

sum_ = 0
for person in people:
    sum_ = sum_ + int(person.age)

print("The average age is: " + str(sum_ / len(people)))

#above is pretty tedious, we can make objects more generalizable 
class Person:
    def __init__(self, name, age, favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods
        
    def birth_year(self):
        return 2020 - self.age
    
    #__str__ is for printing class object information with print()
    def __str__(self):
        return "Name: {}, Age: {}, Favorite food: {}".format(
            self.name, self.age, self.favorite_foods[0])
        
        
people = [Person("Ed", 11, ["hotdogs", "jawbreakers"]),
          Person("Edd", 11, ["broccoli"]),
          Person("Eddy", 12, ["chunky puffs", "jawbreakers"])]


age_sum = 0
year_sum = 0
for person in people:
    age_sum = age_sum + person.age
    year_sum = year_sum + person.birth_year()
    

print("The average age is: " + str(age_sum / len(people)))
print("The average birth year is: " + str(int(year_sum / len(people))))        

for person in people:
    print(person)
        
