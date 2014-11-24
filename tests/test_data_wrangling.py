from unittest import TestCase
import os
import paratices
class Test_Wrangling(TestCase):
    def test_init(self):
        self.assertEquals(1,1)

    def test_csv(self):
        file_name =""
        path_csv = os.path.join("CONFIG_PATH",file_name)
        path_new_csv = os.path.join("CONFIG_NEW_PATH",file_name)
        paratices.CSV_Exercise.add_full_name(path_csv,path_new_csv)
        self.assertEquals(os.path.exists(path_new_csv),True)

    def test_sql(self):
        pass

