import unittest
from src.equation_parser import *
from src.equation_parser.equations import Equations
from pathlib import Path

class Test(unittest.TestCase):
    def setUp(self):
        self.eq_obj = Equations()
        path = Path(__file__).parent
        self.filepath = path.joinpath("src","equation_parser","fixtures","equations.xlsx")
        self.eq_obj.upload_data_equations(self.filepath, 'equations', 
                        'col_var_mapping', 'values')
    
    def test_upload(self):
        self.eq_obj.upload_data_equations(self.filepath, 'equations', 
                        'col_var_mapping', 'values')
        self.assertIsNotNone(self.eq_obj.equations_df)
        self.assertIsNotNone(self.eq_obj.mappings)
        self.assertIsNotNone(self.eq_obj.df)

    def test_start(self):
        result = self.eq_obj.process_equations()
        self.assertIsNotNone(result)
        self.assertIsNotNone(self.eq_obj.lhs)
        self.assertIsNotNone(self.eq_obj.equations)
        self.assertIsNotNone(self.eq_obj.values)
        print(result)
        

if __name__ == '__main__':
    unittest.main()