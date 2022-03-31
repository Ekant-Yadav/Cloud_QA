from selenium import webdriver
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

class Automate():
    def __init__(self, fname, lname, Phnumber, email, gender, dob, country, hobby):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phnumber = Phnumber
        self.gender = gender.lower()
        self.dob = dob
        self.country = country
        self.hobby = hobby
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get('http://app.cloudqa.io/home/AutomationPracticeForm')
        time.sleep(1)

    def fill_form(self):
        fname_column = self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/input')
        fname_column.send_keys(self.fname)

        lname_column = self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[3]/input')
        lname_column.send_keys(self.lname)

        gender = self.driver.find_element_by_id(self.gender)
        gender.click()

        dob = self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[5]/input')
        dob.send_keys(self.dob)

        country = self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[8]/input')
        country.send_keys(self.country)
        state_drop = Select(self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[9]/select'))
        state_drop.select_by_visible_text(self.country)

        mobile = self.driver.find_element_by_xpath('//*[@id="mobile"]')
        mobile.send_keys(self.phnumber)

        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(self.email)

        self.driver.find_element_by_id(self.hobby).click()

        self.driver.find_element_by_xpath('//*[@id="Agree"]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/button[1]').click()


if __name__=="__main__":
    auto = Automate("Ekant","Yadav", "60000", "test@gmail.com", 'Male', '2001-03-11', 'India', 'Reading')
    auto.fill_form()