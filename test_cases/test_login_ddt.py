from utilities import handle_number_data
from page_objects.LoginPage import LoginPage
from time import sleep
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_001_Login:

    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()
    row_count = handle_number_data.get_row_count()



    def test_login(self,setup):


        lst_arry=[]
        for row_no in range(1, Test_001_Login.row_count):
            self.driver = setup
            self.driver.get(self.base_url)
            self.lp = LoginPage(self.driver)

            row_val = handle_number_data.get_cell_value(row_no)
            print(row_val)

            self.username = row_val[0]
            self.password = row_val[1]
            self.exp=row_val[2]

            sleep(2)
            self.lp.set_user_name(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()

            sleep(2)
            act_title=self.driver.title


            if act_title=="Dashboard / nopCommerce administration" and self.exp=='pass':
                self.logger.info("*******passed*******")
                lst_arry.append("pass")
                


            elif act_title=="Dashboard / nopCommerce administration" and self.exp=='fail':
                self.logger.info("*******failed*******")
                lst_arry.append("fail")


            elif act_title!="Dashboard / nopCommerce administration" and self.exp=='pass':
                self.logger.info("*******failed*******")
                lst_arry.append("fail")


            elif act_title != "Dashboard / nopCommerce administration" and self.exp =='fail':
                self.logger.info("*******passed*******")
                lst_arry.append("pass")
            print(lst_arry)



        if 'fail' not in lst_arry:
            self.logger.info("Login DDT test passed")

            assert True
        else:
            self.logger.info("Login DDT test failed")

            assert False




















