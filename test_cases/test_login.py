#https://github.com/Shishir08/nopcommerceApp.git
# git remote add origin https://github.com/Shishir08/nopcommerceApp.git
# git config --global user.name "Shishir08"
# git config --global user.email "shishir8march@gmail.com"
# git add .
from page_objects.LoginPage import LoginPage
from time import sleep
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
import pytest


class Test_001_Login:
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_home_page_title(self,setup):

        self.logger.info("*******Test_001_Login*******")
        self.logger.info("*******Verifying Home page Title*******")
        self.driver=setup
        self.driver.get(self.base_url)
        sleep(2)
        act_title=self.driver.title

        if act_title=="nopCommerce demo store. Login":
            self.logger.info("*******Home page title test case is passed*******")
            self.driver.close()
            assert True


        else:
            self.driver.save_screenshot("../Screenshots/test_home_title.png")
            self.logger.info("*******Home page title test case is Failed*******")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_markers(self):
        print("Regressions")
        assert True




    # def test_login(self,setup):
    #
    #     self.driver=setup
    #     self.driver.get(self.base_url)
    #     sleep(2)
    #     self.lp=LoginPage(self.driver)
    #     self.lp.set_user_name(self.username)
    #     self.lp.set_password(self.password)
    #     self.lp.click_login()
    #     sleep(2)
    #     act_title=self.driver.title
    #
    #
    #     if act_title=="Dashboard / nopCommerce administration":
    #         self.logger.info("*******Login test case is passed*******")
    #         assert True
    #     else:
    #         self.driver.save_screenshot("../Screenshots/test_login_title.png")
    #         self.driver.close()
    #         self.logger.info("*******Login test case is failed*******")
    #         assert False










