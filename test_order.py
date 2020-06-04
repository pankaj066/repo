import unittest
import ordersample
import pandas as pd

class MyTestCase(unittest.TestCase):
    def test_datatype(self):
        result = dict(ordersample.df.dtypes)
        ordersample.df.printSchema
        lst = ['test', '1']

        df = pd.DataFrame(lst)

        expect_result = expected_result = {'order_id': 'int', 'order_date': 'date', 'amount': 'double',
                                           'status': 'string',
                                           'year': 'string', 'month': 'string'}
        self.assertEqual(result, expect_result)


    def test_dataframe(self):
        import pandas as pd
      #  data_pandas = pd.DataFrame({'make':['Jaguar', 'MG', 'MINI', 'Rover', 'Lotus'],
     #  'registration':['AB98ABCD', 'BC99BCDF', 'CD00CDE', 'DE01DEF', 'EF02EFG'],
      #      'year':[1998, 1999, 2000, 2001, 2002]})
      #  data_spark = self.spark.createDataFrame(data_pandas)
       # print(data_spark)



if __name__ == '__main__':
    unittest.main()
