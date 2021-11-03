import unittest
import sys
sys.path.append("..")
from employee_bonus import BonusCalculator
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("../output_exception_revised.txt","w") as f:
            pass
    def test_value_error_for_id(self):
        try:
            BonusCalculator.calculate_bonus({"id":"101","dob":"1999-4-2"},{"id":101,"salary":8000})
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestValueErrorForId=False\n")
                print("TestValueErrorForId = Failed")
        except ValueError:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestValueErrorForId=True\n")
                print("TestValueErrorForId = Passed")

    def test_value_error_for_salary(self):
        try:
            BonusCalculator.calculate_bonus({"id":101,"dob":"1999-4-2"},{"id":101,"salary":"8000"})
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestValueErrorForSalary=False\n")
                print("TestValueErrorForSalary = Failed")
        except ValueError:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestValueErrorForSalary=True\n")
                print("TestValueErrorForSalary = Passed")


    def test_value_error_for_dob(self):
        try:
            BonusCalculator.calculate_bonus({"id":101,"dob":1999-4-2},{"id":101,"salary":8000})
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestValueErrorForDob=False\n")
                print("TestValueErrorForDob = Failed")
        except ValueError:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestValueErrorForDob=True\n")
                print("TestValueErrorForDob = Passed")
