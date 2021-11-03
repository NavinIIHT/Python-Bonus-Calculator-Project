import unittest
import sys
sys.path.append("..")
from employee_bonus import BonusCalculator
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("../output_revised.txt","w") as f:
            pass
    def test_return_type_none(self):
        obj=BonusCalculator.calculate_bonus({"id":101,"dob":"1999-4-2"},{"id":101,"salary":8000})
        if type(obj)!=type(None):
            with open("../output_revised.txt","a") as f:
                f.write("TestReturnTypeNone=True\n")
                print("TestReturnTypeNone = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestReturnTypeNone=False\n")
                print("TestReturnTypeNone = Failed")

    def test_return_type_dict(self):
        obj=BonusCalculator.calculate_bonus({"id":101,"dob":"1999-4-2"},{"id":101,"salary":8000})
        if type(obj)==type({}):
            with open("../output_revised.txt","a") as f:
                f.write("TestReturnTypeDict=True\n")
                print("TestReturnTypeDict = Passed")
        else:
            with open("../output_revised.txt","a") as f:
                f.write("TestReturnTypeDict=False\n")
                print("TestReturnTypeDict = Failed")
