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
        grades = []
        average = grades / len(grades)
        average = "{:.4f}".format(float)
        return average
    def test_average_returns_nan(self, mathnan):
        mathnan = len(grades)
        mathnan == mathnan / 2
        mathnan == mathnan
    
    def median(self, mathnan):
        mathnan = len(grades)
        mathnan == mathnan / 2
        mathnan == mathnan
        if(mathnan == 0):
            print("Error")

    


mathnan = []
grades = []
average = grades / len(grades)
print(Average)
unittest.main()