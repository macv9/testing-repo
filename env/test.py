import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class Test_the_website(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.thesparksfoundationsingapore.org/")

    def test_global_web(self):
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[4]/ul/li[1]/a').click()
    
    def test_contact_page(self):
        self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[6]/a')

    def test_the_logo(self):
        self.driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img')

    def test_the_navigation_bar(self):
        self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul')

    def test_fb_page(self):
        a = self.driver.find_element_by_class_name('fa-facebook')
        a.click()
        time.sleep(5)
    
    def test_page1(self):
        #grip internship page

        a = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[1]/a")
        a.click()

    def test_page2(self):
        a = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[2]/a")
        a.click()
  
    def test_page3(self):
        a = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[3]/a")
        a.click()

      
    def test_page4(self):
        a = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[4]/a")
        a.click()

    def test_page_and_send_info(self):
        a = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/div[2]/ul/li[5]/a")
        a.click()
        
        time.sleep(2)
        name = self.driver.find_element_by_xpath('//input[@name="Name"]')
        name.send_keys('Tejas')
        email = self.driver.find_element_by_name("Email")
        email.send_keys('tejas@gmail.com')
        select = Select(self.driver.find_element_by_class_name("form-control"))
        select.select_by_visible_text('Student')
        self.driver.find_element_by_xpath("//*[@value='Submit']").click()

    
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()