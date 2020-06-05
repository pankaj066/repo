import unittest
import ordersample


class MyTestCase(unittest.TestCase):
     def test_year_gen(a):
          def test_year():
             result = ordersample.getyear(a)
             assert result == "2013"
          return test_year;

<<<<<<< HEAD
    ## suite = unittest.TestSuite()
=======
     ###suite = unittest.TestSuite()
>>>>>>> 8a0b24f66441f004905a5cd39315aae522124002
     test_cases = ["2013-05-26", "2013-08-27", "2013-09-28"]
     for case in test_cases:
            suite.addTest(
             unittest.FunctionTestCase(
                 test_year_gen(case)))
     unittest.TextTestRunner().run(suite)



#    def test_something(self):
 #       self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
