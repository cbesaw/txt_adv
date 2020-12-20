# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:46:54 2020

@author: Claytonious
"""

class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        
    def calories(self):
        kcal = ((self.carbs*4) +
                (self.protein*4) +
                (self.fat*9))
        return kcal
    
    
burger = Food("Double Good Times Burger",
              47,
              25,
              44)

burger.calories()