from unittest import TestCase
import os
import paratices
import config
class Test_Wrangling(TestCase):
    def test_init(self):
        self.assertEquals(1,1)

    # def test_csv(self):
    #     file_name =""
    #     path_csv = os.path.join("CONFIG_PATH",file_name)
    #     path_new_csv = os.path.join("CONFIG_NEW_PATH",file_name)
    #     paratices.CSV_Exercise.add_full_name(path_csv,path_new_csv)
    #     self.assertEquals(os.path.exists(path_new_csv),True)

    # def test_sql(self):
    #     file_name = "aadhaar_data.csv"
    #     path = os.path.join(config.DATA_DIR,file_name)
    #     df = paratices.SQL_Exersice.aggregate_query(path)
    #
    # def test_json_api(self):
    #     name = paratices.JSON_Exersice.api_get_request(config.URL_API)
    #     self.assertEquals(name,"Arctic Monkeys")

    def test_write_csv(self):
        file = config.DATA_DIR + '/' + 'turnstile_110528.txt'
        paratices.CSV_Exercise.fix_turnstile_data([file])
