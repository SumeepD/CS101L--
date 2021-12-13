import math
import unittest
import Grades
class Grade_Test(unittest.TestCase):
    
    def test_total_returns_total_of_list(self):
       
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    
    def test_total_returns_0(self, grades):
        if(grades == 0):
            return 0
    
    def test_average_one(self, average):
        if(average == 5.3):
            return average
    
    def test_average_two(self, average):
        average = "{:.4f}".format(float)
        return average
    


    
grades = []
average = grades / len(grades)
unittest.main()