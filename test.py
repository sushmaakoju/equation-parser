import unittest
from src.equation_parser import *
from src.equation_parser.equations import Equations
from pathlib import Path

class Test(unittest.TestCase):
    def setUp(self):
        self.eq_obj = Equations()
        self.assertIsNotNone(self.eq_obj)
    
    def test_upload(self):
        path = Path(__file__).parent
        filepath = path.joinpath("src","equation_parser","fixtures","equations.xlsx")
        self.eq_obj.upload_data_equations(filepath, 'equations', 'values', 'col_var_mapping')
        self.assertIsNotNone(self.eq_obj.equations_df)
        self.assertIsNotNone(self.eq_obj.mappings)
        self.assertIsNotNone(self.eq_obj.df)

    def test_evaluate_with_upload(self):
        path = Path(__file__).parent
        filepath = path.joinpath("src","equation_parser","fixtures","equations.xlsx")
        self.eq_obj.upload_data_equations(filepath, 'equations', 'values','col_var_mapping')
        result = self.eq_obj.process_equations()
        self.assertIsNotNone(result)
        self.assertIsNotNone(self.eq_obj.lhs)
        self.assertIsNotNone(self.eq_obj.equations)
        self.assertIsNotNone(self.eq_obj.values)
        print(result)

    def test_evaluate_without_upload(self):
        path = Path(__file__).parent
        filepath = path.joinpath("src","equation_parser","fixtures","equations_without_colmappings.xlsx")
        self.eq_obj.upload_data_equations(filepath, 'equations', 'values','')
        result = self.eq_obj.process_equations()
        self.assertIsNotNone(result)
        self.assertIsNotNone(self.eq_obj.lhs)
        self.assertIsNotNone(self.eq_obj.equations)
        self.assertIsNotNone(self.eq_obj.values)
        print(result)

    def test_edge_cases(self):
        path = Path(__file__).parent
        filepath = path.joinpath("src","equation_parser","fixtures","equations_without_colmappings.xlsx")
        self.failUnlessRaises(Exception, self.eq_obj.upload_data_equations, "", '', '','')
        self.failUnlessRaises(Exception, self.eq_obj.upload_data_equations, filepath, '', '','')


if __name__ == '__main__':
    unittest.main()